import pandas as pd
def us_data():
# Retriveing US population by city
# You can download the csv file in 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2018/cities/totals/sub-est2018_all.csv'
    df_us = pd.read_csv('static/habitants/assets/sub-est2018_all.csv', usecols=['SUMLEV', 'NAME', 'STNAME', 'POPESTIMATE2018'], encoding='latin1').sort_values('POPESTIMATE2018', ascending=False)
    df_us = df_us[df_us['SUMLEV'] == 162]

    return df_us

print(us_data())