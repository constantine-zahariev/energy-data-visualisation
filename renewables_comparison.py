# Import required libraries
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as font_manager

# Open and read columns from spreadsheet
var = pd.read_excel("renewables_trends_data.xlsx")
# print(var) # For debugging purposes

# Create an instance of the module which can then be used in the
# 'legend' method. The font family, size and style are defined
# in this instance
legendfont = font_manager.FontProperties(family='Jost',
                                   weight='normal',
                                   style='normal', size=12)

# Access Excel columns and import data, then convert each dataset to a Python list
# Data is read from top to bottom in columns and saved in a list
years = list(var["Year"])
solar_data = list(var["Solar"])
thermal_renewables = list(var["Thermal Renewables"])
pumped_storage_hydro = list(var["Pumped Storage Hydro"])
natural_flow_hydro = list(var["Hydro (natural flow)"])
onshore_wind = list(var["Onshore Wind"])
offshore_wind = list(var["Offshore Wind"])
other_fuels = list(var["Other fuels"])

# Create a list with values ranging from 0 to 50,000 in steps of 5,000
# This is used for the y-axis labels
energy_ticks = list(range(0, 50000, 5000))

fig, ax = plt.subplots(layout="constrained")    # Create a figure with a single set of axes

# Plot all the different renewable sources data
ax.plot(years, solar_data, label='Solar (PV)', marker="o", markersize="3")
ax.plot(years, thermal_renewables, label='Thermal Renewables', marker="o", markersize="3")
ax.plot(years, pumped_storage_hydro, label="Pumped Storage Hydro", marker="o", markersize="3")
ax.plot(years, natural_flow_hydro, label="Natural Flow Hydro", marker="o", markersize="3")
ax.plot(years, onshore_wind, label="Onshore Wind", marker="o", markersize="3")
ax.plot(years, offshore_wind, label="Offshore Wind", marker="o", markersize="3")

# Add axes labels
ax.set_xlabel('Year', fontfamily="Jost", fontsize="15")
ax.set_ylabel('Electricity Generated (GWh)', fontfamily="Jost", fontsize="15")

# Add graph title
ax.set_title("UK renewable energy generation from 2008 to 2022", fontfamily="Jost", fontsize="16")

# Add legend and set the 'prop' parameter to the 'legendfont' instance defined earlier
ax.legend(prop=legendfont)

# Use the 'energy_ticks' list to create new y-axis data ticks
plt.yticks(energy_ticks, [f"{x}" for x in energy_ticks], fontfamily="Jost", fontsize="10")

# Save figure as a PNG image in the project root directory
plt.savefig("renewables_comparison.png", dpi=600, transparent=False, bbox_inches="tight")

# Show graph
plt.show()
