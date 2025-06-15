from pandas import read_csv

DATASET_DIR = "dataset"

claims = read_csv(DATASET_DIR + "/claims.csv")
print("Number of claims per label:")
print(claims['label'].value_counts())

print("Number of claims per source:")
print(claims['source'].value_counts())

tweets = read_csv(DATASET_DIR + "/tweets.csv")
print("Number of tweets per label:")
print(tweets['label'].value_counts())
