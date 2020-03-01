import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
import plotly.graph_objects as go
import panel as pn

# Bar plots scripts
from barplots import jobtype_barchart as jb
from barplots import malefemale_comp_earnings_barchart as mceb
from barplots import educational_attainment_barchart as eab
# Line plots scripts
from lineplots import line_amount_software_overlay as laso
from lineplots import line_amount_finance_overlay as lafo
# Pie plots scripts 
from pieplots import bronx_pie 
from pieplots import brooklyn_pie 
from pieplots import manhattan_pie 
from pieplots import queens_pie 
from pieplots import statenisland_pie 
# Scatter plots scripts
from scatterplots import age_income_by_borough as aibb
from scatterplots import software_age_annual_overlay as saao
from scatterplots import software_age_county_overlay as saco
from scatterplots import software_household_income_annual_overlay as shiao
from scatterplots import software_household_income_county_overlay as shico
from scatterplots import software_percap_income_annual_overlay as spiao
from scatterplots import software_percap_income_county_overlay as spico
from scatterplots import software_poverty_annual_overlay as spao
from scatterplots import software_poverty_county_overlay as spco
# Parallel plots scripts
from parallelplots import parallel_coordinates_software_female as pcsf
from parallelplots import parallel_coordinates_software_male as pcsm
from parallelplots import parallel_categories_index as pci

# Summary of visualizations related to education 
edu_tab = pn.Column(pn.Row(pn.Column( 
                       "# Eduactional attainment and top degrees in the labor force by county", 
                       "## Summary of visualizations reflecting educational stats in NYC in 2017"), eab()), 
                       pn.Row(bronx_pie(), brooklyn_pie()),
                       pn.Row(manhattan_pie(), queens_pie()), 
                       statenisland_pie())

pci_tab = pn.Row("## In the parallel categories visualization, we were able to use the census data to map out the population size, income range and poverty level of each borough, giving deep insight on economic outlook for job hunters. ",pci())

jobtype_tab = pn.Column(pn.Row(pn.Column("# This graph is depicting the rising trends of Female’s in the Business Operations job type.",
                               "## It has an interactive feature and allows to choose between various job titles."), jb()),
                        pn.Row(pn.Column("# Those parallel graphs reveal socio-ecomomic stats for Software Development/Finance fields.",
                               "## Categorized by gender too."), pn.Column(pcsf(), pcsm()))
                       )

demographics_tab = pn.Row(pn.Column("# This graph shows the trend by the median age of the borough and the household income.",
                                    "## We noticed that there is a general trend of rising age in the various boroughs with the exception of Staten Island."),
                                aibb())

soft_devs_tab1 = pn.Column(pn.Row(pn.Column("# While focused on Computer Occupation:", 
                                           "## men outearn women in Manhattan, Brooklyn and Queens… with Manhattan showing the most disparity."),
                          mceb()),
                         pn.Row("## This graph shows the amount of people employed as Software Devs categorized by gender and county.",
                          laso()))

soft_devs_tab2 = pn.Column("## Those graphs reveal Software Devs median age vs. county's median age:", saao(),
                           "## and Software Devs median age by County.", saco())

#soft_devs_tab3 = pn.Column("## Those graphs reveal amount of Software Devs employed vs. Per Capita Income:", spiao(),
#                          "## and categorized by County too.", spico())

dashboard = pn.Tabs(
    ("Demographics", demographics_tab),
    ("Education", edu_tab),
    ("Job Type Stats", jobtype_tab),
    ("Software Devs Employed/Earnings", soft_devs_tab1),
    ("Software Devs Age", soft_devs_tab2)
)

dashboard.servable()    