import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# Read data for Bronx
bronx_bachelor = pd.read_csv(Path("data/datausa_bronx_bachelor_concentration_2017.csv"),
                             parse_dates=True, infer_datetime_format=True)
bronx_bachelor = bronx_bachelor[['Year','Geography','CIP6','Completions']]
bronx_bachelor.rename(columns={"CIP6":"Field Of Study"}, inplace=True)
bronx_bachelor_top = bronx_bachelor.sort_values(ascending=False, by='Completions').head(10)
# Read data for Brooklyn
brooklyn_bachelor = pd.read_csv(Path("data/datausa_brooklyn_bachelor_concentration_2017.csv"),
                             parse_dates=True, infer_datetime_format=True)
brooklyn_bachelor = brooklyn_bachelor[['Year','Geography','CIP6','Completions']]
brooklyn_bachelor.rename(columns={"CIP6":"Field Of Study"}, inplace=True)
brooklyn_bachelor_top = brooklyn_bachelor.sort_values(ascending=False, by='Completions').head(10)
# Read data for Manhattan
manhattan_bachelor = pd.read_csv(Path("data/datausa_manhattan_bachelor_concentration_2017.csv"),
                             parse_dates=True, infer_datetime_format=True)
manhattan_bachelor = manhattan_bachelor[['Year','Geography','CIP6','Completions']]
manhattan_bachelor.rename(columns={"CIP6":"Field Of Study"}, inplace=True)
manhattan_bachelor_top = manhattan_bachelor.sort_values(ascending=False, by='Completions').head(10)
# Read data for Queens
queens_bachelor = pd.read_csv(Path("data/datausa_queens_bachelor_concentration_2017.csv"),
                             parse_dates=True, infer_datetime_format=True)
queens_bachelor = queens_bachelor[['Year','Geography','CIP6','Completions']]
queens_bachelor.rename(columns={"CIP6":"Field Of Study"}, inplace=True)
queens_bachelor_top = queens_bachelor.sort_values(ascending=False, by='Completions').head(10)
# Read data for Staten Island 
statenisland_bachelor = pd.read_csv(Path("data/datausa_statenisland_bachelor_concentration_2017.csv"),
                             parse_dates=True, infer_datetime_format=True)
statenisland_bachelor = statenisland_bachelor[['Year','Geography','CIP6','Completions']]
statenisland_bachelor.rename(columns={"CIP6":"Field Of Study"}, inplace=True)
statenisland_bachelor_top = statenisland_bachelor.sort_values(ascending=False, by='Completions').head(10)

def bronx_pie():
    
    bronx_pie = px.pie(bronx_bachelor_top, values='Completions', names='Field Of Study',
             title='Bronx Top Ten Fields of Study for Bachelors Degree 2017',
             hover_data=['Field Of Study'])
    
    return bronx_pie

def brooklyn_pie():
    
    brooklyn_pie = px.pie(brooklyn_bachelor_top, values='Completions', names='Field Of Study',
             title='Brooklyn Top Ten Fields of Study for Bachelors Degree 2017',
             hover_data=['Field Of Study'])
    
    return brooklyn_pie

def manhattan_pie():
    
    manhattan_pie = px.pie(manhattan_bachelor_top, values='Completions', names='Field Of Study',
             title='Brooklyn Top Ten Fields of Study for Bachelors Degree 2017',
             hover_data=['Field Of Study'])
    
    return manhattan_pie

def queens_pie():
    
    queens_pie = px.pie(queens_bachelor_top, values='Completions', names='Field Of Study',
             title='Brooklyn Top Ten Fields of Study for Bachelors Degree 2017',
             hover_data=['Field Of Study'])
    
    return queens_pie

def statenisland_pie():
    
    statenisland_pie = px.pie(statenisland_bachelor_top, values='Completions', names='Field Of Study',
             title='Brooklyn Top Ten Fields of Study for Bachelors Degree 2017',
             hover_data=['Field Of Study'])
    
    return statenisland_pie