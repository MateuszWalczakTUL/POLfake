import pandas as pd
from pandas import read_csv

DATASET_DIR = "dataset"

claims = read_csv(DATASET_DIR + "/claims.csv")
print("Number of claims per label:")
print(claims['label'].value_counts())

tweets = read_csv(DATASET_DIR + "/tweets.csv")
print("Number of matched and mismatched tweets:")
print(tweets['matched'].value_counts())
