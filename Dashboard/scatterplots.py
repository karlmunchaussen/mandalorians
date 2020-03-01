import numpy as np
import pandas as pd
import plotly.express as px
from pathlib import Path
import hvplot.pandas

data_csv = pd.read_csv(Path('data/census_2010_2018_panel_df.csv'))
data_pickle = pd.read_pickle(Path('data/census_2010_2018_panel_df.pickle')).reset_index()
data_csv['Year'] =  pd.to_datetime(data_csv['Year'], format='%Y')
data_csv = data_csv.filter(['Year', 'Name', 'Median Age', 'Household Income'])

def age_income_by_borough():
    
    age_income_scatter = px.scatter(data_csv,
        x="Year", y="Median Age", color="Name",
        size='Household Income', hover_data=['Household Income'])
    
    return age_income_scatter

def software_age_annual_overlay():

    software_female_age_annual = data_pickle.hvplot.scatter(
        x='Median Age', y='Software_devops_female', rot=45,
        label='Developers vs. Age - Female', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_age_annual = data_pickle.hvplot.scatter(
        x='Median Age', y='Software_devops_male', rot=45,
        label='Developers vs. Age - Male', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    software_age_annual_overlay = software_male_age_annual * software_female_age_annual
    software_age_annual_overlay.opts(title='Developers vs. County Median Age by Year')
    
    return software_age_annual_overlay

def software_age_county_overlay():
    
    software_female_age_county = data_pickle.hvplot.scatter(
        x='Median Age', y='Software_devops_female', rot=45,
        label='Developers vs. Age - Female', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_age_county = data_pickle.hvplot.scatter(
        x='Median Age', y='Software_devops_male', rot=45,
        label='Developers vs. Age - Male', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    software_age_county_overlay = software_male_age_county * software_female_age_county
    software_age_county_overlay.opts(title='Developers vs. Median Age by County')
    
    return software_age_county_overlay

def software_household_income_annual_overlay():

    software_female_household_income_annual = data_pickle.hvplot.scatter(
        x='Household Income', y='Software_devops_female', rot=45,
        label='Developers vs. Household Income - Female', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_household_income_annual = data_pickle.hvplot.scatter(
        x='Household Income', y='Software_devops_male', rot=45,
        label='Developers vs. Household Income - Male', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    software_household_income_annual_overlay = software_male_household_income_annual * software_female_household_income_annual
    software_household_income_annual_overlay.opts(title='Developers vs. Annual Household Income')
    
    return software_household_income_annual_overlay

def software_household_income_county_overlay():
    
    software_female_household_income_county = data_pickle.hvplot.scatter(
        x='Household Income', y='Software_devops_female', rot=45,
        label='Developers vs. Household Income - Female', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_household_income_county = data_pickle.hvplot.scatter(
        x='Household Income', y='Software_devops_male', rot=45,
        label='Developers vs. Household Income - Male', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")

    software_household_income_county_overlay = software_male_household_income_county * software_female_household_income_county
    software_household_income_county_overlay.opts(title='Developers vs. Household Income by County')
    
    return software_household_income_county_overlay

def software_percap_income_annual_overlay():
    
    software_female_percap_income_annual = data_pickle.hvplot.scatter(
        x='Per Capita Income', y='Software_devops_female', rot=45,
        label='Software Developers vs. Per Capita Income - Female', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_percap_income_annual = data_pickle.hvplot.scatter(
        x='Per Capita Income', y='Software_devops_male', rot=45,
        label='Software Developers vs. Per Capita Income - Male', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    software_percap_income_annual_overlay = software_male_percap_income_annual * software_female_percap_income_annual
    software_percap_income_annual_overlay.opts(title='Developers vs. Per Capita Income by Year')
    
    return software_percap_income_annual_overlay

def software_percap_income_county_overlay():

    software_female_percap_income_county = data_pickle.hvplot.scatter(
        x='Per Capita Income', y='Software_devops_female', rot=45,
        label='Software Developers vs. Per Capita Income - Female', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_percap_income_county = data_pickle.hvplot.scatter(
        x='Per Capita Income', y='Software_devops_male', rot=45,
        label='Software Developers vs. Per Capita Income - Male', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")

    
    software_percap_income_county_overlay = software_male_percap_income_county * software_female_percap_income_county
    software_percap_income_county_overlay.opts(title='Developers vs. Per Capita Income by County')
    
    return software_percap_income_county_overlay

def software_poverty_annual_overlay():

    software_female_poverty_annual = data_pickle.hvplot.scatter(
        x='Poverty Rate', y='Software_devops_female', rot=45,
        label='Software Developers vs. Poverty Rate - Female', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_poverty_annual = data_pickle.hvplot.scatter(
        x='Poverty Rate', y='Software_devops_male', rot=45,
        label='Software Developers vs. Poverty Rate - Male', groupby=['Year'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    software_poverty_annual_overlay = software_male_poverty_annual * software_female_poverty_annual
    software_poverty_annual_overlay.opts(title='Developers vs. Poverty Rate by Year')
    
    return software_poverty_annual_overlay

def software_poverty_county_overlay():

    software_female_poverty_county = data_pickle.hvplot.scatter(
        x='Poverty Rate', y='Software_devops_female', rot=45,
        label='Software Developers vs. Poverty Rate - Female', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    software_male_poverty_county = data_pickle.hvplot.scatter(
        x='Poverty Rate', y='Software_devops_male', rot=45,
        label='Software Developers vs. Poverty Rate - Male', groupby=['Name'], 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    software_poverty_county_overlay = software_male_poverty_county * software_female_poverty_county
    software_poverty_county_overlay.opts(title='Developers vs. Poverty Rate by County')
    
    return software_poverty_county_overlay
    
