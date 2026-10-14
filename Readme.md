# POLfake - Polish fake news dataset

This dataset contains CSV files that provide data on claims (statements) and related tweets that proclaim the claim to which they refer. Both the claims and tweets are written in **Polish** and come from Polish speakers.

This dataset facilitates research on detecting fake news written in Polish.

The dataset offers two challenges: _Claim-Tweet Challenge_ and _Claim-Only Challenge_.

## Challenges

### Claim-Tweet Challenge

In this challenge, the goal is to classify tweets (**tweets-test.csv**) into 1 of 5 truthfulness labels using all claims as the training data (**claims-train.csv**).

It can be done by finding the claim that the tweet refers to and using its label as the label for the tweet. It can also be done by training a classifier on the claims and then applying it to the tweets.

To verify whether the appropriate claim was found, check the `claim_id` column in **claim-tweet-challenge/tweets-test.csv**, which links each tweet to the corresponding claim in **claim-tweet-challenge/claims-train.csv**. However, the main goal of the challenge is to categorize tweets using the appropriate truthfulness labels.

There is also a binary version of the challenge, where the goal is to classify tweets into two categories: *True* and *Fake*.

### Claim-Only Challenge

In this challenge, the claims were split into training (**claims-train.csv**) and test (**claims-test.csv**) datasets.

The goal is to classify the claims into 1 of 5 truthfulness labels.

There is also a binary version of the challenge using only two labels: *True* and *Fake*.

## Repository Structure

```text
claim-only-challenge/
├── claims-test.csv
└── claims-train.csv

claim-tweet-challenge/
├── claims-train.csv
└── tweets-test.csv

images/
├── claim_1.jpg
├── claim_2.jpg
├── tweet_1.jpg
├── tweet_2.jpg
└── ...

metadata/
├── claims_images.csv
└── tweets_images.csv

main.py
README.md
```

## Structure of Claims and Tweets Files

### Claims

The claims files contain fact-checked claims from professional fact-checking platforms (`demagog.org.pl` and `fake_news.pl`), together with metadata describing their sources and truthfulness assessments.

#### Columns

- **id** - Unique identifier for the claim.
- **content** - The textual content of the claim in Polish.
- **source** - The source that fact-checked the claim: *demagog_org* or *fake_news_pl*.
- **tags** - Keywords categorizing the claim's topic, stored as comma-separated values, for example `EU`, `Economy`, or `Migration`.
- **publication_date** - The date when the claim was published, in UNIX timestamp format.
- **author** - The person who made the statement, if known.
- **link** - A URL linking to the full fact-checking report.
- **label** - The truthfulness evaluation of the claim: *Prawda* (*True*), *Fałsz* (*Fake*), *Manipulacja* (*Manipulation*), *W większości prawda* (*Mostly True*), or *W większości fałsz* (*Mostly Fake*).
- **label_enc** - Encoded label for the claim:
  - `0` = Fałsz (*Fake*)
  - `1` = Prawda (*True*)
  - `2` = Manipulacja (*Manipulation*)
  - `3` = W większości fałsz (*Mostly Fake*)
  - `4` = W większości prawda (*Mostly True*)

#### Number of Claims by Label

| Label                                 | Number of Claims |
|---------------------------------------|-----------------:|
| **Prawda** (True)                     | 3,058            |
| **Fałsz** (Fake)                      | 1,733            |
| **Manipulacja** (Manipulation)        | 852              |
| **W większości prawda** (Mostly True) | 109              |
| **W większości fałsz** (Mostly Fake)  | 22               |

### Tweets

The tweets file contains tweets that refer to claims included in the claim dataset. It includes metadata related to tweet interactions and the relationships between tweets and claims.

#### Columns

- **id** - Unique identifier for the tweet.
- **claim_id** - Identifier linking the tweet to the corresponding claim.
- **content** - The textual content of the tweet.
- **shares** - The number of times the tweet was shared or retweeted.
- **likes** - The number of likes the tweet received.
- **replies** - The number of replies to the tweet.
- **link** - URL to the tweet on the *X* platform.
- **publication_date** - The date and time when the tweet was published, in UNIX timestamp format.
- **label** - The truthfulness label of the tweet, inherited from the claim to which it refers.
- **label_enc** - Encoded label for the tweet, following the same encoding as the claims files.

#### Number of Tweets by Label

| Label                                 | Number of Tweets |
|---------------------------------------|-----------------:|
| **Prawda** (True)                     | 847              |
| **Fałsz** (Fake)                      | 435              |
| **Manipulacja** (Manipulation)        | 141              |
| **W większości prawda** (Mostly True) | 25               |
| **W większości fałsz** (Mostly Fake)  | 5                |

## Multimodal Extension

The dataset contains an experimental multimodal extension that associates claims and tweets with automatically selected images.

The images were not originally attached to the claims or tweets and were not selected by their authors. They were retrieved and selected automatically using an AI-assisted pipeline developed for this dataset.

This extension supports research on multimodal fake news detection and multimodal credibility assessment for Polish-language content.

### Image Naming Convention

Each image filename identifies the type and ID of the corresponding dataset record.

Images associated with claims use the following format:

```text
claim_<id>.jpg
```

For example:

```text
claim_1.jpg
```

is associated with the claim whose `id` is `1`.

Images associated with tweets use the following format:

```text
tweet_<id>.jpg
```

For example:

```text
tweet_12.jpg
```

is associated with the tweet whose `id` is `12`.

The identifiers correspond directly to the `id` columns in the relevant claims and tweets CSV files.

### Image Acquisition and Selection

The images were obtained using an automated pipeline consisting of the following stages:

1. The Polish text of a claim or tweet was analyzed by a large language model.
2. The model generated short image-search queries in Polish and English.
3. The model generated a neutral `visual_intent` describing visual content that could plausibly illustrate the record.
4. The queries were submitted to openly licensed media repositories:
   - Openverse,
   - Wikimedia Commons.
5. Search results were filtered according to license and file format.
6. Only supported raster image formats, such as JPEG, PNG, and WebP, were considered. Documents and non-raster files, including PDF, DjVu, and SVG files, were excluded.
7. Candidate image thumbnails were downloaded and compared with the claim or tweet using the multilingual SigLIP 2 vision-language model.
8. SigLIP 2 assigned an image-text matching score to each candidate.
9. Exactly one candidate with the highest matching score was selected for each successfully processed record.
10. The selected image was converted to RGB, center-cropped to a square aspect ratio, resized to `224 × 224` pixels, and saved as a JPEG file.

The truthfulness information stored in `label` and `label_enc` was not used for generating search queries or ranking candidate images. This prevents the image-selection process from directly using the target classification label.

### Image Sources and Licenses

Candidate images were retrieved from Openverse and Wikimedia Commons.

The acquisition pipeline accepted images marked with one of the following license categories:

- CC0,
- Public Domain,
- Creative Commons Attribution,
- Creative Commons Attribution-ShareAlike.

Information about the source, creator, license, original image URL, and license URL is preserved in the metadata files.

Users of the dataset should consult the corresponding metadata entry and source page before redistributing or publishing an individual image. Attribution and share-alike requirements may differ between images.

### Image Metadata Files

The `metadata` directory contains two CSV files:

```text
metadata/claims_images.csv
metadata/tweets_images.csv
```

The `claims_images.csv` file describes images associated with claims.

The `tweets_images.csv` file describes images associated with tweets.

Local filesystem paths are not stored in these files. The appropriate file in the `images` directory can be found using the `record_type` and `record_id` columns together with the filename convention described above.

#### Metadata Columns

- **record_type** - Type of the associated record:
  - `claim` for a claim,
  - `tweet` for a tweet.
- **record_id** - Identifier of the associated claim or tweet. It corresponds to the `id` column in the relevant dataset file.
- **sha256** - SHA-256 checksum of the normalized JPEG image. It can be used to verify file integrity and identify exact duplicates.
- **provider** - Repository from which the selected candidate was retrieved, for example `openverse` or `wikimedia`.
- **provider_id** - Identifier assigned to the image by the source provider.
- **title** - Title of the image provided by the source repository.
- **creator** - Author or creator of the image, if available in the source metadata.
- **source_page_url** - URL of the source page containing information about the original image.
- **image_url** - URL from which the original selected image was retrieved.
- **license** - Normalized license category of the image, for example `cc0`, `public-domain`, `by`, or `by-sa`.
- **license_url** - URL containing the terms of the image license, if provided by the source repository.
- **search_query** - Search query that returned the selected image candidate.
- **siglip_score** - Image-text matching score assigned to the selected candidate by SigLIP 2. The score is used to rank candidates within the same selection process and should not be interpreted as a calibrated probability.
- **visual_intent** - AI-generated neutral description of the expected visual content used to support image-text ranking.
- **retrieved_at** - Date and time when the image was retrieved, expressed as an ISO 8601 UTC timestamp.
- **transformation** - Description of the image preprocessing operations applied before saving the final image.

### Methodological Limitation

The included images must not be interpreted as the original images selected or published by the authors of the claims or tweets.

The relationship between the text and image was produced automatically using:

- a large language model that generated search queries and visual descriptions,
- external media search engines that returned candidate images,
- SigLIP 2 that ranked the candidates,
- deterministic selection of the candidate with the highest matching score.

Consequently, the multimodal extension introduces an additional credibility threat. The images represent plausible, automatically selected illustrations rather than verified historical evidence of how the original content was presented.

Researchers should explicitly report this limitation when using the images in experiments or publications.

## How to Run `main.py`

The simple `main.py` script reads the CSV files and summarizes the dataset. It displays:

1. The number of claims per label.
2. The number of claims per source.
3. The number of tweets per label.

### 1. Install Dependencies

Ensure that Python is installed on your system. Then install the required `pandas` library:

```bash
pip install pandas
```

### 2. Run the Script

Execute the script using the following command:

```bash
python main.py
```
