# Bigfoot Sightings

This repository contains code for analyzing and visualizing Bigfoot sightings data. The project provides insights into the temporal distribution of sightings and the classification of reported events through visualizations.

## Features

- **Line Plot**: Visualize the number of sightings per year with average lines.
- **Pie Chart**: Display the distribution of sightings by classification.

## Requirements

- Python 3
- Packages:
  - [pandas](https://pandas.pydata.org/)
  - [matplotlib](https://matplotlib.org/)
  - [numpy](https://numpy.org/)

## Installation

Install the required packages using pip:

```bash
python3 install pandas matplotlib numpy
```

## Usage

1. Ensure your dataset `bigfootdata.csv` is in the project directory.
2. Run the file:


This will generate two figures:
- A line plot with the yearly sightings (if you want a specific year, point your mouse over the desired year and look at the x-axis number at the top right of your screen), trend line, and average line.
- A pie chart showing the distribution of sightings by classification.

## Classfication Key
**Class A:**
Class A reports involve clear sightings in circumstances where misinterpretation or misidentification of other animals can be ruled out with greater confidence.

**Class B:**
Incidents where a possible sasquatch was observed at a great distance or in poor lighting conditions and incidents in any other circumstance that did not afford a clear view of the subject are considered Class B reports.

**Class C:**
Most second-hand reports, and any third-hand reports, or stories with an untraceable sources, are considered Class C, because of the high potential for inaccuracy.


## References
1. [Classes](https://www.bfro.net/gdb/classify.asp)
2. [Information](https://www.kaggle.com/datasets/thedevastator/unlocking-mysteries-of-bigfoot-through-sightings?resource=download)