"""
Implements the filter functionality for the website
- Selecting a cause or multiple causes filters out all charities not containing any of the selected causes
- Selecting a need or multiple needs filters out all charities not containing any of those needs
- Thus, any results shown will contain AT LEAST ONE of the causes _AND_ AT LEAST ONE of the needs
- The results can be sorted by rating or sorted in alphabetic order
"""

import pandas as pd


charities = pd.read_csv("FinalCharity.csv")

# List of all possible categories
CAUSES = ["Animals", "Education", "Health", "Environment", "Human rights", "Aboriginal", "Adults", "Elderly",
          "Children", "LGBTQ+", "Refugees/Migrants", "Homeless", "Chronic Illness", "Disabilities", "Unemployed",
          "Veterans"]
NEEDS = ["Finance", "Food", "Clothes", "Electronics", "Blood", "Nut juice", "Slave labour"]

causes_selected = ["Education", "Disabilities"]  # Values are for testing only
needs_selected = ["Finance, Food"]  # Values are for testing only

filtered_charities = charities[charities[causes_selected].any(axis=1) & charities[needs_selected].any(axis=1)]

print(filtered_charities)


