######################
#
# Import World Development Indicators
# and look at the relationship between income
# and health outcomes across countries
# 
######################

import pandas as pd
import numpy as np

# Download World Development Indicators
wdi = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")

# GDP Per Capita has a REALLY long right tail, so we want to log it for readability. 
wdi['Log GDP Per Capita'] = np.log(wdi['GDP per capita (constant 2010 US$)'])

# Plot
from plotnine import *

(ggplot(wdi, 
        aes('Log GDP Per Capita', 'Mortality rate, under-5 (per 1,000 live births)')) + 
        geom_point() + 
        geom_label(aes(label='Country Name'), size=8) + 
        geom_smooth()
    )
