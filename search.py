"""
Implements the search functionality for the website
- Entering text into the search box searches for substrings in charity names and descriptions
- The results can be sorted by rating or sorted in alphabetic order
"""

import pandas as pd
import numpy as np
from enum import Enum

from flask import Flask, render_template
# Enum class for 'sort by' filter
class Sorting(Enum):
    RATING_DESC = 1  # Sort first by rating from highest to lowest, then by most to least reviews
    RATING_ASC = 2  # Sort first by rating from lowest to highest, then by most to least reviews
    ALPHA_AZ = 3  # Sort in alphabetic order, A to Z
    ALPHA_ZA = 4  # Sort in reverse alphabetic order, Z to A

def sort_results(results: pd.DataFrame, sort_by: Sorting):
    if sort_by == Sorting.RATING_DESC:
        # Sort first by rating from highest to lowest, then by most to least reviews
        results.sort_values(by=["Rating", "Rating_count"], ascending=False, inplace=True)

    elif sort_by == Sorting.RATING_ASC:
        # Sort first by rating from lowest to highest, then by most to least reviews
        results.sort_values(by=["Rating", "Rating_count"], ascending=[True, False], inplace=True)

    else:
        a_to_z = True if sort_by == Sorting.ALPHA_AZ else False
        results.sort_values(by=["Charity_Legal_Name"], ascending=a_to_z, inplace=True)


charities = pd.read_csv("FinalCharity1.csv")

# Arbitrarily add RNG Rating and Num_Reviews column for demonstration/testing


search = input("Search: ")
names = charities["Charity_Legal_Name"]
results = charities.loc[names.str.contains(search, case=False, regex=False)].copy()

sort_by = Sorting.RATING_DESC  # What to sort results by
sort_results(results, sort_by)

print(results)
app = Flask(__name__)

@app.route('/')
def index():
    numb = len(results)
    return render_template('result.html', number=numb)

if __name__ == '__main__':
    app.run()



