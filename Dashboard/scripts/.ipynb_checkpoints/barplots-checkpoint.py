import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path

data_csv = pd.read_csv('../data/census_pop_concat_df22.csv') 
data_consolidated = data_csv.sort_values(
            by=['County', 'Job Type']
        )
edu_data_csv = pd.read_csv('../data/educational_data.csv').dropna()
data_pickle = pd.read_pickle(Path('../dashboard/data/census_earn_pd_2018.pickle'))

def jobtype_barchart():

    jobtype_barchart = census_consolidated.hvplot.bar("County", 
                                    xlabel="County", 
                                    ylabel="Number Employed", 
                                    rot=90, 
                                    groupby=('Job Type')
        )
    return jobtype_barchart

def malefemale_comp_earnings_barchart():
    
    malefemale_comp_earnings = go.Figure(data=[
        go.Bar(name='Male', x=data_pickle['NAME'], y=data_pickle['Male Computer occupations Earnings']),
        go.Bar(name='Female', x=data_pickle['NAME'], y=data_pickle['Female Computer occupations Earnings'])
    ])
    malefemale_comp_earnings.update_layout(barmode='group', title='Male/Female Computer occupations Earnings')
    
    return malefemale_comp_earnings

def educational_attainment_barchart():

    educational_attainment = go.Figure(data=[
        go.Bar(name='Less than high school', x=educational_df['County'],
                                 y=educational_df['Less than high school graduate']),
        go.Bar(name="Some college or associate's degree", x=educational_df['County'], 
                                 y=educational_df["Some college or associate's degree"]),
        go.Bar(name="Bachelor's degree or higher", x=educational_df['County'], 
                                 y=educational_df["Bachelor's degree or higher"]),
        go.Bar(name="High school graduate (includes equivalency)", x=educational_df['County'], 
                                 y=educational_df["High school graduate (includes equivalency)"])
    ])
    educational_attainment.update_layout(barmode='group', title='Educational Attainment')
    
    return educational_attainment
