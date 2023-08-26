import pandas as pd
import random

def update_review (org_df, review_df):
	for i in range (0, len(org_df)):
		org_id = org_df['_id'][i]
		org_sum = 0
		org_count = 0
		for b in range (0, len(review_df)):
			if review_df['org_id'][b] == org_id:
				org_count = org_count+1
				org_sum = org_sum + review_df['rating'][b]
		org_df['Rating'][i] = round(org_sum/org_count,2)
	org_df.set_index("_id", inplace = True)
	org_df.to_csv("chicken.csv")

