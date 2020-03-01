import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path

data_pickle = pd.read_pickle(Path('data/census_2010_2018_panel_df.pickle')).reset_index()

def line_amount_software_overlay():
    
    fig_software_male = data_pickle.hvplot.line(
        x='Year', y='Software_devops_male', rot=45,
        title='Software Developers by County - Male', groupby='Name', 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    fig_software_female = data_pickle.hvplot.line(
        x='Year', y='Software_devops_female', rot=45,
        title='Software Developers by County - Female', groupby='Name', 
        ylabel='Software Developers (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    
    line_amount_software_overlay = fig_software_male * fig_software_female
    line_amount_software_overlay.opts(title='Software Developers by County')
    
    return line_amount_software_overlay

def line_amount_finance_overlay():
    
    fig_finance_male = data_pickle.hvplot.line(
        x='Year', y='Financial_specialists_male', rot=45,
        title='Financial Specialists by County - Male', groupby='Name', 
        ylabel='Financial Specialists (k)').opts(yformatter="%.0f",
        line_color="darkolivegreen",
        hover_line_color="black",
        bgcolor="lightblue")
    
    fig_finance_female = data_pickle.hvplot.line(
        x='Year', y='Financial_specialists_female', rot=45,
        title='Financial Specialists by County - Female', groupby='Name', 
        ylabel='Financial Specialists (k)').opts(yformatter="%.0f",
        line_color="deeppink",
        hover_line_color="darkorchid",
        bgcolor="lavender")
    
    
    line_amount_finance_overlay = fig_finance_male * fig_finance_female
    line_amount_finance_overlay.opts(title='Finance Specialists by County')
    
    return line_amount_finance_overlay