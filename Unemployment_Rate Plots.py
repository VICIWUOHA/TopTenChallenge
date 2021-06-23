import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.ticker as ticker
from matplotlib import rc, rcParams


# import dataset
data = pd.read_excel('Top 10 Unemployment Rates by State in Nigeria- Q4-2020.xlsx', sheet_name='Data')

# sort this data
data = data.sort_values(by=['Unemployment Rate'])
# define figure params
fig, ax = plt.subplots(figsize=(12, 8))

# ---HORIZONTAL Bar Plot

# modify x values for easy plotting and data labeling
x_values = round((data['Unemployment Rate']*100), 1)
# define colour code to enable- diverging scale application using matplotlib inbuilt colour map
my_cmap= plt.cm.get_cmap('BuGn')
# generate width lengths that will be used for colours - a loop can be used foreach item instead.
data_width = [x / max(x_values) for x in x_values]
colors = my_cmap(data_width)
hbars = ax.barh(data['State'], x_values, color=colors)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Remove x,y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
# remove x tick labels
ax.xaxis.set_major_locator(ticker.NullLocator())

# make labels bold
plt.rc('font', weight='bold')
plt.setp(ax.get_yticklabels(), fontsize=14) #weight='bold')
ax.set_xlabel('Unemployment Rate (%)', labelpad=10, weight='bold', size=12)

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# Add x,y gridlines
ax.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

# Add Plot Title
ax.set_title('Q4, 2020 - National Bureau of Statistics',
             loc='right', pad=10, style='italic')

# Add Text watermark
fig.text(0.9, 0.15, '@viciwuoha', fontsize=12, color='grey',
         ha='right', va='bottom', alpha=0.5)

# ---DATA LABELS
# Label with given captions, custom padding and annotate options
# the code below will give a regular formatting
# ax.bar_label(ax.containers[0], label_type='edge') - easier method
# Append a '% sign and format to 1dp
ax.bar_label(hbars, labels=['%.1f''%%' % v for v in x_values],
             padding=5, color='black', fontsize=11)

# Set Figure Title
fig.suptitle('Top 10 Unemployment Rates by States in Nigeria', fontsize=22, fontweight='bold', color='#006400',
             fontname='Arial Black')

plt.savefig('fig1.png', dpi=150)
# print(data)