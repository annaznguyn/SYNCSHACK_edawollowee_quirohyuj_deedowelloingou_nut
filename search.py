"""
Implements the search functionality for the website
- Entering text into the search box searches for substrings in charity names and descriptions
- The results can be sorted by rating or sorted in alphabetic order
"""

import pandas as pd
import numpy as np
from enum import Enum


# Enum class for 'sort by' filter
class Sorting(Enum):
    RATING_DESC = 1  # Sort first by rating from highest to lowest, then by most to least reviews
    RATING_ASC = 2  # Sort first by rating from lowest to highest, then by most to least reviews
    ALPHA_AZ = 3  # Sort in alphabetic order, A to Z
    ALPHA_ZA = 4  # Sort in reverse alphabetic order, Z to A


def search(search_string: str, charities: pd.DataFrame, sort_by: Sorting):
    names = charities["Charity_Legal_Name"]
    results = charities.loc[names.str.contains(search_string, case=False, regex=False)].copy()
    sort_results(results, sort_by)
    return results


def sort_results(results: pd.DataFrame, sort_by: Sorting):
    if sort_by == Sorting.RATING_DESC:
        # Sort first by rating from highest to lowest, then by most to least reviews
        results.sort_values(by=["Rating", "Num_Reviews"], ascending=False, inplace=True)

    elif sort_by == Sorting.RATING_ASC:
        # Sort first by rating from lowest to highest, then by most to least reviews
        results.sort_values(by=["Rating", "Num_Reviews"], ascending=[True, False], inplace=True)

    else:
        a_to_z = True if sort_by == Sorting.ALPHA_AZ else False
        results.sort_values(by=["Charity_Legal_Name"], ascending=a_to_z, inplace=True)


"""
TESTING ONLY
"""

charities = pd.read_csv("FinalCharity.csv")

# Arbitrarily add RNG Rating and Num_Reviews column for demonstration/testing
np.random.seed(0)
mean_rating = 4
sd_rating = 1
random_ratings = np.random.normal(mean_rating, sd_rating, len(charities))
charities["Rating"] = np.clip(random_ratings, a_min=0, a_max=5).round(1)

mean_num_reviews = 200
sd_num_reviews = 100
random_num_reviews = np.random.normal(mean_num_reviews, sd_num_reviews, len(charities))
charities["Num_Reviews"] = np.clip(random_num_reviews, a_min=0, a_max=1000).astype(int)

string = input("Search: ")
results = search(string, charities, Sorting.RATING_DESC)

print(results)
