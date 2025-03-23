# Polish fake news dataset

This dataset contains two CSV files that provide data on claims (statements) and related tweets that proclaim the claim to which they refer. Both the claims and tweets are written in **Polish** and come from Polish speakers.

This dataset facilitates research on detecting fake news written in Polish.

## Files and Structure

### **1. Claims (claims.csv)**
This file contains fact-checked claims by professional fact-checking platforms (demagag.org and fake_news.pl) along with metadata about their sources and accuracy assessments.

#### Columns:
- **id** – Unique identifier for the claim.
- **content** – The textual content of the claim in Polish.
- **source** – The source that fact-checked the claim: *demagog_org* or *fake_news_pl*.
- **label** – The truthfulness evaluation of the claim: *Prawda* (*True*), *Fałsz* (*False*), *Manipulacja* (*Manipulation*), *W większości prawda* (*Mostly True*), *W większości fałsz* (*Mostly False*).
- **tags** – Keywords categorizing the claim’s topic (comma-separated), e.g., "EU", "Economy", "Migration".
- **publication_date** – The date when the claim was published, in UNIX timestamp format.
- **author** – The person who made the statement (if known).
- **link** – A URL linking to the full fact-checking report.

#### Number of Claims by Label
The following table summarizes the numbers of claims for each category:

| Label                  | Number of Claims |
|------------------------|-----------------|
| **Prawda** (True)      | 3,058           |
| **Fałsz** (False)      | 1,733           |
| **Manipulacja** (Manipulation) | 852   |
| **W większości prawda** (Mostly True) | 109 |
| **W większości fałsz** (Mostly False) | 22 |

### 2. Tweets (tweets.csv)
This file contains tweets that refer to claims listed in **claims.csv**. The file includes metadata related to tweet interactions and its relation to the claims.

#### Columns:
- **id** – Unique identifier for the tweet.
- **claim_id** – Identifier linking the tweet to a claim in **claims.csv**.
- **body_text** – The textual content of the tweet.
- **shares** – The number of times the tweet was shared (retweeted).
- **likes** – The number of likes the tweet received.
- **replies** – The number of replies to the tweet.
- **link** – URL to the tweet on *X* platform.
- **time_created** – The date and time the tweet was published, in UNIX timestamp format.
- **matched** – A flag indicating whether the tweet explicitly proclaims the claim (1 = Yes, 0 = No).

## Relationships Between Files
- The **claim_id** column in **tweets.csv** corresponds to the **id** column in **claims.csv**, linking tweets to specific claims.
- If **matched = 1**, The tweet proclaims a claim to which it refers. The information contained in the tweet is identical or very close to the content of the claim.
- If **matched = 0**, The tweet does not address the claim, or proclaims a thesis contrary to the claim. The information contained in the tweet is contradictory or completely unrelated to the tweet.

## How to Run `main.py`?

The simple `main.py` script reads CSV files and summarizes dataset. It displays:
1. The number of claims per category.
2. The number of matching and mismatched tweets.

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

