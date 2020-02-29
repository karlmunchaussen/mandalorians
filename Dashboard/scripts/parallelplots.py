import numpy as np
import pandas as pd
import plotly.express as px
from pathlib import Path

data_pickle = pd.read_pickle("../data/census_2010_2018_panel_df.pickle").reset_index()

def parallel_coordinates_software_female():

    parallel_coordinates_software_female = px.parallel_coordinates(data_pickle,
        dimensions=['Software_devops_female', 'Median Age', 'Poverty Rate', 'Household Income', 'Per Capita Income', 'Financial_specialists_female'],
        color='Median Age',
        color_continuous_scale=px.colors.sequential.Inferno,
        title='Parallel Coordinates on Female Software Developers',
        labels={
            "Software_devops_female": "Number of Full-Time Female Software Developers (k)",
            "Median Age": "Median Age",
            'Poverty Rate': 'Poverty Rate',
            "Household Income": "Household Income",
            'Per Capita Income': 'Per Capita Income', 
            'Financial_specialists_female' : "Number of Full-Time Female Financial Specialists (k)"
            
        }
    )
    
    return parallel_coordinates_software_female

def parallel_coordinates_software_male():

    parallel_coordinates_software_male = px.parallel_coordinates(data_pickle,
        dimensions=['Software_devops_male', 'Median Age', 'Poverty Rate', 'Household Income', 'Per Capita Income', 'Financial_specialists_male'],
        color='Median Age',
        color_continuous_scale=px.colors.sequential.Inferno,
        title='Parallel Coordinates on Male Software Developers',
        labels={
            "Software_devops_male": "Number of Full-Time Male Software Developers (k)",
            "Median Age": "Median Age",
            'Poverty Rate': 'Poverty Rate',
            "Household Income": "Household Income",
            'Per Capita Income': 'Per Capita Income', 
            'Financial_specialists_female' : "Number of Full-Time Female Financial Specialists (k)"
            
        }
    )

    return parallel_coordinates_software_male

data_csv = pd.read_csv(Path('../data/census_data.csv'),infer_datetime_format=True, parse_dates= True)

data_csv = data_csv.drop(columns=["Employed_age16+_civilian","Employed_male",
                                      "Financial_managers_male","Male_business_operations",
                                      "Financial_specialists_male","Accountants_&_auditors_male",
                                      "Computer_male","Male_data_scientits","Software_devops_male",
                                      "Database_&_system_male","Employed_female",
                                      "Financial_managers_female","Female_business_operations",
                                      "Financial_specialists_female","Accountants_&_auditors_female",
                                      "Computer_female","Female_data_scientits","Software_devops_female",
                                      "Database_&_system_female","Information_age16+_total",
                                      "Finance_and_insurance","Real_estate","Unemployment Rate",
                                      "Male Business Operations","Male Data Scientits","Female Business  Operations","Female Data Scientits"])

pop_bins = [300000,1000000,1700000,2700000]
hincome_bins = [25000,60000,70000,90000]
povert_bins = [0,200000,300000,600000]
pop_group_names = ["Small POP <100k","Medium POP", "Large POP >1.7mil"]
hincome_group_names = ["Low Income <60K","Middle Income","Large Income >70k"]
povert_group_names = ["Low <200k","Medium","High >300k"]
data_csv["Population Size"] = pd.cut(data_csv["Population"], pop_bins, labels=pop_group_names)
data_csv["Income Range"] = pd.cut(data_csv["Household Income"], hincome_bins, labels=hincome_group_names)
data_csv["Poverty Level"] = pd.cut(data_csv["Poverty Count"], povert_bins, labels=povert_group_names)

data_csv["Name"] = data_csv["Name"].str.replace(", New York","")

def parallel_categories_index():

    parallel_categories_index = px.parallel_categories(census_csv, 
        dimensions=["Name","Population Size","Income Range","Poverty Level"], 
        color="Year", 
        color_continuous_scale=px.colors.sequential.Blues, 
        labels={"Name": "Borough"}, 
        width=970)

    return parallel_categories_index