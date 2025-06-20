from pandas import read_csv

CLAIM_TWEET_DIR = "claim-tweet-challenge"
CLAIM_ONLY_DIR = "claim-only-challenge"

print("------ Claim-Tweet Challenge Dataset ------")

claims = read_csv(CLAIM_TWEET_DIR + "/claims-train.csv")
print("Number of claims per label:")
print(claims['label'].value_counts())

print("\nNumber of claims per source:")
print(claims['source'].value_counts())

tweets = read_csv(CLAIM_TWEET_DIR + "/tweets-test.csv")
print("\nNumber of tweets per label:")
print(tweets['label'].value_counts())

print("\n------ Claim-Only Challenge Dataset ------")
claims_train = read_csv(CLAIM_ONLY_DIR + "/claims-train.csv")
print("Number of training claims per label:")
print(claims_train['label'].value_counts())

claims_test = read_csv(CLAIM_ONLY_DIR + "/claims-test.csv")
print("\nNumber of test claims per label:")
print(claims_test['label'].value_counts())
