from bs4 import BeautifulSoup
import requests
import pandas as pd



def world_data():
    # Retrieve world's population by country
    url = 'https://www.worldometers.info/world-population/population-by-country/'
    path = requests.get(url)
    soup = BeautifulSoup(path.text, 'html.parser')

    table = soup.find('table',{'id':'example2'}).tbody
    rows = soup.find_all('tr')#, {'role':'row'})
    columns = [v.text for v in rows[0].find_all('th')]
    columns = columns[0:3]
    df = pd.DataFrame()

    # Filling DataFrame with Table information
    for i in range(1, len(rows)):
        tds = rows[i].find_all('td')
        values = [tds[0].text,tds[1].text,tds[2].text]
        df = df.append(pd.Series(values, index=columns), ignore_index = True)

    # Renaming Columns
    df.columns=['id','country','population']

    # Making column POPULATION becomes Integer data
    list=[]
    for i in df['population']:
         list.append(int(i.replace(',','')))
    df['pop'] = list
    df = df.drop(columns='population')

    # Setting Index column
    df = df.set_index('id')

    return df



def us_data():
# Retriveing US population by city
# You can download the csv file in 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2018/cities/totals/sub-est2018_all.csv'
    df_us = pd.read_csv('habitants/static/habitants/assets/sub-est2018_all.csv', usecols=['SUMLEV', 'NAME', 'STNAME', 'POPESTIMATE2018'], encoding='latin1').sort_values('POPESTIMATE2018', ascending=False)
    df_us = df_us[df_us['SUMLEV'] == 162]

    return df_us

def play(df, df_us,number):
    resto_min, resto_min_us = [], []
    resto_min.clear()
    resto_min_us.clear()

    pop_test = number

    for i in df['pop']:
        resto_min.append(abs(pop_test-i))

    for j in df_us['POPESTIMATE2018']:
        resto_min_us.append(abs(pop_test-j))


    minimum = min(resto_min)
    minumum_us = min(resto_min_us)

    index = resto_min.index(minimum)
    final_country = df['country'][index]
    final_pop = df['pop'][index]
    if final_country == 'United States':
        final_country = 'U.S.'
    elif final_country == 'United Kingdom':
        final_country = 'U.K.'

    city_ranking = resto_min_us.index(minumum_us)
    final_us = df_us.iloc[city_ranking]
    city_name = final_us['NAME']
    city_state = final_us['STNAME']
    city_pop = final_us['POPESTIMATE2018']


    urls = ['https://www.worldometers.info/geography/flags-of-the-world/', 'https://www.worldometers.info/geography/flags-of-dependent-territories/']
    flags={}

    for url in urls:
        path = requests.get(url)
        soup = BeautifulSoup(path.text, 'html.parser')

        table = soup.find_all('div', {'class': 'col-md-4'})


        for i in table:
            links = i.findAll('a')
            for a in links:
                flags[i.text] = 'https://www.worldometers.info/' + a['href']

        try:
            flag = flags[final_country]

        except:
            flag = '/static/habitants/assets/noflag.jpg'


    return final_pop, final_country, index, flag, city_pop, city_name, city_state, city_ranking
