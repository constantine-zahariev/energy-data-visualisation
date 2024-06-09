import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch
from matplotlib import style
from matplotlib import rcParams

# Use 'rcParams' module to set the font globally
plt.rcParams['font.family'] = ['Jost', 'sans-serif']

# Predefined colour theme
style.use("seaborn-v0_8-deep")

# The following are datasets for each year specified
# Data are put into lists but could also be shoved into a dictionary

# Percentages for the main bar chart wedges
overall_ratios_2020 = [0.0175, 0.0049, 0.3580, 0.0282, 0.1598, 0.4270]
# Ratios of each renewable source to the overall percentage
renewable_ratios_2020 = [0.0511221, 0.5611110, 0.0930630, 0.2940960, 0.0114540]

# Make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5)) # 10, 6
fig.subplots_adjust(wspace=-0.5)

# Pie chart parameters
pie_labels = ['Coal', 'Oil', 'Natural Gas', 'Other fuels', 'Nuclear', 'Renewable \nsources']

explode = [0, 0, 0, 0, 0, 0.1]

# Rotate so that the last wedge is split by the x-axis
angle = 180 * overall_ratios_2020[5]
wedges, labels, pct = ax1.pie(overall_ratios_2020, autopct='%2.2f%%', startangle=angle,
                              labels=pie_labels, explode=explode, textprops={'fontfamily': 'Jost', 'fontsize': 12})


# THIS WORKS:
# The function below takes the wedges objects returned by 'ax1.pie' function as well as a radius percentage
# and uses these to calculate new x and y coordinates for both the wedge labels and the percentages in the chart
def get_label_coordinates(pie_wedge, pct_radius):
    # The angle at which text is normally positioned
    angle = (pie_wedge.theta2 + pie_wedge.theta1) / 2.
    # New distance to the center
    x = pie_wedge.r * pct_radius * np.cos(angle * np.pi / 180)
    y = pie_wedge.r * pct_radius * np.sin(angle * np.pi / 180)
    return x, y


for patch, txt in zip(wedges, pct):
    if (patch.theta2 - patch.theta1) <= 5:

        # Call function
        x, y = get_label_coordinates(patch, 1.05)

        # Move text to new position
        txt.set_position((x, y))
        # Set colour
        txt.set_color('black')

    elif 5 < (patch.theta2 - patch.theta1) <= 10:

        # Call function
        x, y = get_label_coordinates(patch, 0.50)

        # Move text to new position
        txt.set_position((x + 0.1, y))
        # Set colour
        txt.set_color('black')


for patch, lbls in zip(wedges, labels):
    if (patch.theta2 - patch.theta1) <= 5:

        # Call function
        x, y = get_label_coordinates(patch, 1.15)

        # Move text to new position
        lbls.set_position((x - 0.1, y))
        lbls.set_color('black')
    elif 5 < (patch.theta2 - patch.theta1) <= 10:

        # Call function
        x, y = get_label_coordinates(patch, 0.65)

        # Move text to new position
        lbls.set_position((x, y))
        lbls.set_color('black')

# colors=['#4f4f4f', '#6e3701', '#0062a8', '#de0000', '#7300de', '#006117']

# Bar chart parameters
renewable_ratios = [0.11352657, 0.398550725, 0.001207729, 0.387681159, 0.099033816]
renewables_labels = ['Hydro \n(natural flow)', 'Wind', 'Solar', 'Thermal \nrenewables', 'Pumped \nstorage']
bottom = 1.01
width = 0.2
height = 2

# colours = ['#abffbe', '#00fa3a', '#00d131', '#00ad28', '#016e1a']

# Add bars from the top so that they match the legend
for j, (height, label) in enumerate(reversed([*zip(renewable_ratios_2020, renewables_labels)])):
    bottom -= height
    bar_chart = ax2.bar(0, height, width, bottom=bottom, label=label, color='#006482',  # '#006482'
                        alpha=0.27 + 0.18 * j)
    ax2.bar_label(bar_chart, labels=[f"{height:.2%}"], label_type='center')
    # print(j) # For debugging purposes

ax2.set_title('Breakdown of renewable sources', fontfamily='Jost', fontsize='14')
ax2.legend(loc='center right', fontsize='11')
ax2.axis('off')
ax2.set_xlim(-2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[5].theta1, wedges[5].theta2
center, r = wedges[5].center, wedges[5].r
bar_height = sum(renewable_ratios_2020)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)

con.set_color('#8c8c8c')
con.set_linewidth(1)
ax2.add_artist(con)

# Draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)

con.set_color('#8c8c8c')
ax2.add_artist(con)
con.set_linewidth(1)

ax1.set_title('Share of Electricity Generated in 2020', fontsize='14')

# The 'tight_layout' method spaces out subplots evenly within the figure
fig.tight_layout()

plt.savefig("pie_chart_2020.png", dpi=600, transparent=False, bbox_inches="tight")

plt.show()
