# POLfake - Polish fake news dataset

This dataset contains CSV files that provide data on claims (statements) and related tweets that proclaim the claim to which they refer. Both the claims and tweets are written in **Polish** and come from Polish speakers.

This dataset facilitates research on detecting fake news written in Polish.

The dataset offers two challenges: _Claim-Tweet Challenge_ and _Claim-Only Challenge_.

## Challenges

### Claim-Tweet Challenge
In this challenge, the goal is to classify tweets (**tweets_test.csv**) into 1 of 5 truthfulness labels using all claims as the training data (**claims_train.csv**).
It can be done by finding the claim that the tweet refers to and using its label as the label for the tweet.
It can also be done by learning classifier on the claims and then applying it to the tweets.

To verify if the appropriate claim is found, check the `claim_id` column in the **tweets.csv** file, which links each tweet to its corresponding claim in **claims.csv**.
However, the main goal of the challenge is categorize tweets to appropriate truthfulness labels.

There is also a binary version of the challenge, where the goal is to classify tweets into two categories: *True* and *Fake*.

### Claim-Only Challenge
In this challenge, the claims were split into training (**claims_test.csv**) and test (**claims_test.csv**). 
The goal is to classify the claims into 1 of 5 truthfulness labels.

Of course, there is also a binary version of the challenge using only two labels: *True* and *Fake*.

## Structure of Claims and Tweets Files

### Claims
This claims files contains fact-checked claims by professional fact-checking platforms (demagag.org and fake_news.pl) along with metadata about their sources and accuracy assessments.

#### Columns:
- **id** – Unique identifier for the claim.
- **content** – The textual content of the claim in Polish.
- **source** – The source that fact-checked the claim: *demagog_org* or *fake_news_pl*.
- **tags** – Keywords categorizing the claim’s topic (comma-separated), e.g., "EU", "Economy", "Migration".
- **publication_date** – The date when the claim was published, in UNIX timestamp format.
- **author** – The person who made the statement (if known).
- **link** – A URL linking to the full fact-checking report.
- **label** – The truthfulness evaluation of the claim: *Prawda* (*True*), *Fałsz* (*Fake*), *Manipulacja* (*Manipulation*), *W większości prawda* (*Mostly True*), *W większości fałsz* (*Mostly Fake*).
- **label_enc** – Encoded label for the claim, where:
  - 0 = Fałsz (Fake)
  - 1 = Prawda (True)
  - 2 = Manipulacja (Manipulation)
  - 3 = W większości fałsz (Mostly Fake)
  - 4 = W większości prawda (Mostly True)

#### Number of Claims by Label
The following table summarizes the numbers of claims for each category:

| Label                                 | Number of Claims |
|---------------------------------------|-----------------|
| **Prawda** (True)                     | 3,058           |
| **Fałsz** (Fake)                      | 1,733           |
| **Manipulacja** (Manipulation)        | 852   |
| **W większości prawda** (Mostly True) | 109 |
| **W większości fałsz** (Mostly Fake)  | 22 |

### Tweets
This tweets file contains tweets that refer to claims listed in **claims.csv**. The file includes metadata related to tweet interactions and its relation to the claims.

#### Columns:
- **id** – Unique identifier for the tweet.
- **claim_id** – Identifier linking the tweet to a claim in **claims.csv**.
- **content** – The textual content of the tweet.
- **shares** – The number of times the tweet was shared (retweeted).
- **likes** – The number of likes the tweet received.
- **replies** – The number of replies to the tweet.
- **link** – URL to the tweet on *X* platform.
- **publication_date** – The date and time the tweet was published, in UNIX timestamp format.
- **label** - The truthfulness label of the tweet which is the same as the claim it refers to.
- **label_enc** - Encoded label for the tweet following the same encoding as in **claims.csv**.

#### Number of Tweets by Label
The following table summarizes the numbers of tweets for each category:

| Label                                 | Number of Tweets |
|---------------------------------------|------------------|
| **Prawda** (True)                     | 847              |
| **Fałsz** (Fake)                      | 435              |
| **Manipulacja** (Manipulation)        | 141              |
| **W większości prawda** (Mostly True) | 25               |
| **W większości fałsz** (Mostly Fake)  | 5                |

## How to Run `main.py`?

The simple `main.py` script reads CSV files and summarizes dataset. It displays:
1. The number of claims per label.
2. The number of claims per source.
3. The number of tweets per label.

### 1. Install Dependencies
Ensure you have Python installed on your system. Then, install the required library `pandas` by running:
```bash
pip install pandas
```

### 2. Run the Script
Execute the script using the following command:
```bash
python main.py
```

