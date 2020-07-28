import pandas as pd
# import matplotlib.pyplot as plt
import datetime


# Date of Birth
# Date of Measurement
# Height, Weight, or Head Circumference
# Current measure
# plot chart
# pounds or kilos

def baby_chart(dict):
    # Date of Birth and Date of Measurement
    dob = f"{dict['dob_month']}/{dict['dob_day']}/{dict['dob_year']}"
    dom = f"{dict['dom_month']}/{dict['dom_day']}/{dict['dom_year']}"

    # Converting strings to date format
    dob = datetime.datetime.strptime(dob, '%m/%d/%Y')
    dom = datetime.datetime.strptime(dom, '%m/%d/%Y')

    # Subtracting dates
    age = dom - dob
    age = int(age.total_seconds() / (60 * 60 * 24))

    url = 'https://www.cdc.gov/growthcharts/html_charts/statage.htm#males'

    gender = dict['gender']

    # Assigning files
    if gender == 'female':
        heightfile = 'babysize/static/babysize/assets/lhfa_girls_p_exp.txt'
        weightfile = 'babysize/static/babysize/assets/wfa_girls_p_exp.txt'
        chart_title = 'Girl'
    else:
        heightfile = 'babysize/static/babysize/assets/lhfa_boys_p_exp.txt'
        weightfile = 'babysize/static/babysize/assets/wfa_boys_p_exp.txt'
        chart_title = 'Boy'

    # Transforming files into dataframes
    heightdata = pd.read_csv(heightfile, sep='\t')  # lineterminator='\r')
    weightdata = pd.read_csv(weightfile, sep='\t')

    # Transforming weight into Pounds if necessary

    if dict['weight_format'] == 'pounds':

        weightdata['P50'] = weightdata['P50'] * 2.20462
        weightdata['P5'] = weightdata['P5'] * 2.20462
        weightdata['P95'] = weightdata['P95'] * 2.20462
        w_y_label = 'Weight in Pounds (lb)'
    else:
        w_y_label = 'Weight in Kilos (kg)'

    # Transforming height in Inches if necessary

    if dict['height_format'] == 'inches':
        heightdata['P50'] = heightdata['P50'] * 0.393701
        heightdata['P5'] = heightdata['P5'] * 0.393701
        heightdata['P95'] = heightdata['P95'] * 0.393701
        h_y_label = 'Height in Inches (in)'
    else:
        h_y_label = 'Height in Centimeters (cm)'

    # Filtering the rows to get only 30 days before and 30 days after baby's current age
    n = 30
    if age <= n:
        agebegin = 0
        ageend = n * 2
    else:
        agebegin = age - n
        ageend = age + n

    heightdata = heightdata.loc[agebegin:ageend]
    weightdata = weightdata.loc[agebegin:ageend]
    return heightdata, weightdata, chart_title, age, w_y_label, h_y_label
