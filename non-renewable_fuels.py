# Comparing the evolution of non-renewable energy sources used for electricity generation between 2012 and 2022 in the UK
# First time experimenting with pandas to import data from a .xlsx file

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import matplotlib.font_manager as font_manager
import pandas as pd

style.use("seaborn-v0_8-deep")

years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

# Read data from spreadsheet
data = pd.read_excel("non-renewables_trends_data.xlsx")

# Put data into lists
# Access spreadsheet columns
coal = list(data["Coal"])
oil = list(data["Oil"])
gas = list(data["Gas"])
nuclear = list(data["Nuclear"])

# Create a dictionary to organise all the lists
# and make them easier to pass into the 'stackplot'
# function

energy_by_fuel = {
    'Coal': coal,
    'Oil': oil,
    'Gas': gas,
    'Nuclear': nuclear,
}

# Set the font family, style and size using the 'font_manager' library
legendfont = font_manager.FontProperties(family='Jost',
                                   weight='normal',
                                   style='normal', size=11)


# Create new figure with axes
fig, ax = plt.subplots()

# Create instance of a stacked graph using the dictionary values as data points
# and the keys as the labels
ax.stackplot(years, energy_by_fuel.values(), labels=energy_by_fuel.keys())
ax.legend(loc='upper right', prop=legendfont)
ax.set_title('Breakdown of non-renewable generation in the UK (GWh)', fontfamily='Jost', fontsize="15")
ax.set_xlabel('Year', fontsize="12", fontfamily='Jost')
ax.set_ylabel('Capacity (GWh)', fontsize="13", fontfamily='Jost')

plt.xticks(fontsize="11", fontfamily="Jost")
plt.yticks(fontsize="11", fontfamily="Jost")

plt.savefig("non-renewable-fuels.png", dpi=600, transparent=False, bbox_inches="tight")
plt.show()
