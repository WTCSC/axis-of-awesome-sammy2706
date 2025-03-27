import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

# Load and prepare data
df = pd.read_csv('bigfootdata.csv')
df = df.drop(columns=["latitude", "longitude", "title"])
df = df.drop([213, 3277])  # Removed because timesetamp incorrect
df.sort_values(by=["timestamp"], inplace=True)

# Process the 'timestamp' column to extract the year
df['timestamp'] = df['timestamp'].str.slice(0, 4)
df['year'] = df['timestamp'].astype(int)



# Line Plot (Sightings per Year)
# Count sightings per year and fill missing years with 0 sightings
year_counts = df['year'].value_counts().sort_index()
all_years = pd.RangeIndex(start=year_counts.index.min(), stop=year_counts.index.max() + 1)
year_counts = year_counts.reindex(all_years, fill_value=0)

# Compute the average sightings per year and best-fit trend line
avg_sightings = year_counts.mean()
x = year_counts.index.values
y = year_counts.values
slope, intercept = np.polyfit(x, y, 1)
trend_line = slope * x + intercept

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color='darkblue', label='Yearly Bigfoot Sightings')
ax.axhline(avg_sightings, color='green', linestyle=':', label=f'Average Sightings per Year: {avg_sightings:.1f}')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Sightings')
ax.set_title('Sightings of Bigfoot per Year with Average')
ax.xaxis.set_major_locator(MaxNLocator(nbins=10, integer=True))
ax.grid(True, linestyle='-', alpha=0.7)
ax.legend()
plt.tight_layout()



# Pie Chart (Classification Distribution)
# Count sightings per classification
classification_counts = df['classification'].value_counts()

fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(classification_counts, labels=classification_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title('Distribution of Sightings by Classification')
ax2.axis('equal')  # Ensure the pie chart is a circle
plt.tight_layout()

plt.show()
