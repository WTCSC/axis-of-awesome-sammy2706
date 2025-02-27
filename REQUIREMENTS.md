# Requirements

In this assignment, you'll find or create a dataset about something that interests you (the weirder, the better) and apply your plotting skills to reveal insights.

## Overview

For this assignment, you'll become a data detective exploring the unexpected. Find or create a dataset about something unusual or amusing, then analyze and visualize it using Matplotlib.

### Step 1 - Find or Create Your Dataset

Choose ONE of the following approaches:

- **Collect your own data:**
    - The speed at which different flavors of ice cream melt
    - The number of times people say "like" or "um" during class presentations
    - The distribution of letters in a can of Alphabet Soup
    - The time it takes different flavors of Hot Pockets to cool to an edible temperature
    - The frequency of different emojis used in your text messages based on who you're talking to
    - The distribution of colors in a bag of Skittles
- **Use existing quirky data (here are a few suggestions):**
    - https://www.kaggle.com/datasets/NUFORC/ufo-sightings
    - https://www.kaggle.com/datasets/unsdsn/world-happiness
    - https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
    - https://www.kaggle.com/datasets/thedevastator/unlocking-mysteries-of-bigfoot-through-sightings
    - https://en.wikipedia.org/wiki/Nathan's_Hot_Dog_Eating_Contest
    - https://www.statista.com/statistics/266292/number-of-pirate-attacks-worldwide-since-2006/
    - https://www.ssa.gov/oact/babynames/index.html

### Step 2 - Clean and Prepare Your Data

Once you have your data, organize it into a pandas DataFrame. You might need to:

- Clean up any inconsistencies or missing values
- Group or categorize your data appropriately
- Calculate any additional metrics that might be interesting

### Step 3 - Create at Least Two Different Visualizations

Using Matplotlib, create at least TWO different types of visualizations for your data. Get creative with your plots! Consider using:

- Bar charts (vertical or horizontal)
- Pie charts
- Line graphs
- Scatter plots
- Bubble charts

Make sure to add appropriate titles, labels, and any other elements (average lines, best fit lines, etc) that enhance understanding.

### Step 4 - Find the Absurd Insight

Analyze your visualization and identify at least one "insight" from your data. You may need to compare to additional datasets in order to find a [Spurious Correlation](https://tylervigen.com/spurious-correlations). The most ridiculous or entertaining “insight” will be awarded a trip to the **Swag Shelf**™️.

- "UFO sightings increase dramatically on national pizza day."
- "The number of times I say 'um' in class increases 250% when talking about data science."
- "Skittles bags advertised as 'containing the rainbow' actually contain 37% more red than any other color."
- "The average Hot Pocket requires exactly 3 minutes and 42 seconds to cool down to an edible temperature, regardless of flavor—defying both physics and common sense."

## Deliverables

In order to receive credit for this assignment, you must submit the following to the **Create Axis of Awesome** assignment in Google Classroom:

- A link to your GitHub repository (as created by GitHub Classrooms) containing:
    - Your code
    - Your dataset
    - A comprehensive README
    - Screenshots of your TWO visualizations
- A brief (100-200 word) write-up in Google Docs explaining:
    - What data you collected/found and why
    - Your "absurd insight" from the visualization
    - One legitimate observation about how Matplotlib helped you understand your data

## Evaluation

### Code Completeness - 50 pts possible

This score will be determined by the result of running a series of automated tests on your code. The tests check whether your code implements the tasks we ask you to implement in the assignment and, thus, are a good measure of how complete your code is.

#### 50 pts

Code met all defined acceptance criteria and all automated tests pass.

#### 30 pts

Either some defined acceptance criteria was not met, or some automated tests did not pass.

#### 0 pts

None of the defined acceptance criteria was met and none of the automated tests passed.

### Code Readability - 25 pts possible

This score will be determined by qualities, many of which are intangible, that don’t have to do with (and exist to some extent independently of) the correct operation of your code.

#### 25 pts
The code is well-structured and easy to read. Variables were appropriately named, and whitespace was used to clearly separate logical concepts.

#### 15 pts

Improvement could be made to the structure and readability of the code. Variables were unclear, whitespace wasn't effectively utilized, or other issues made the code difficult to parse.

#### 0 pts

Code followed non-standard formatting or uses inappropriate variable names.

#### Code Correctness - 25 pts possible

This score encompasses issues with your code that, while not explicitly captured by the tests, could lead to incorrect behavior (or simply neglect to implement something we told you to implement). This section of the rubric will never re-penalize you for a failure that is already captured by the "Completeness" score.

#### 25 pts

There is no inadvertent behavior, problematic scale issues, or other unexpected/unnecessary operations in the code.

#### 15 pts

There is no inadvertent behavior or unexpected/unnecessary operations in the code, but the implementation will not hold up under large scale.

#### 0 pts

The code performs unnecessary operations or has problematic downstream consequences.

### Documentation Clarity - 20 pts possible

This score evaluates how well the documentation communicates the purpose and functionality of the code to the reader.

#### 20 pts

Clear, concise, and well-structured documentation. Code comments explain why key sections of code exist, not just what they do. Supplemental documentation (README, user manual) provides detailed explanations of setup, usage, and examples. Consistent formatting and language throughout.

#### 10 pts

Documentation is present but lacks clarity in some areas. Code comments are mostly what the code does, with minimal explanation of why. Supplemental documentation explains the basics but may be incomplete or unclear in certain sections. Inconsistent formatting or language in some parts.

#### 0 pts

Documentation is unclear or missing. Minimal or no code comments. Supplemental documentation, if present, is confusing or irrelevant. Poor or inconsistent structure and formatting.

### Documentation Accuracy - 20 pts possible

This score measures the correctness of the information provided in the documentation, ensuring it aligns with the actual code functionality.

#### 20 pts

Documentation accurately reflects the code’s functionality. Code comments match the behavior of the corresponding code. Supplemental documentation correctly explains setup, functionality, and output with no errors.

#### 10 pts

Documentation is mostly accurate, but with minor errors or omissions. Some code comments may not fully match the current implementation. Supplemental documentation may have minor inaccuracies or missing details.

#### 0 pts

Documentation is mostly or entirely inaccurate. Code comments misrepresent what the code does. Supplemental documentation contains significant errors or missing critical information.

### Documentation Completeness - 10 pts possible

This score assesses whether the documentation covers all necessary aspects of the code, including setup, usage, and edge cases.

#### 10 pts

Documentation is complete. All key parts of the code are commented. Supplemental documentation includes setup instructions, usage examples, and explanations of any edge cases or assumptions.

#### 5 pts

Documentation is mostly complete but may miss some minor details. Key parts of the code are commented, but less critical sections may be omitted. Supplemental documentation covers setup and basic usage but omits edge cases or assumptions.

#### 0 pts

Documentation is incomplete. Critical sections of code are uncommented. Supplemental documentation is missing or lacks key sections (e.g., setup, usage).
