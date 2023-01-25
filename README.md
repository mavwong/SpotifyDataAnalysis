# Spotify Dataset - Data Analysis

## 1. Background

Spotify is the global leader in the streaming music sector. Spotify datasets is ideal in analyzing track trends, track popularity, etc. Spotify music datasets have become one of the most prominent datasets in the data science field for learning predictive modeling.

The author created this repo for its portfolio, at the same time, to test functions relative to data analysis.
### 1.1 Data Collection

The dataset is from Kaggle. Here is the link to the [Spotify Dataset](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets). There are two (2) datasets we have used for this project - Tracks and artists dataset. The following are its column feature fromt he data:

#### Main Features
- track_id and artist_id: unique identifier for each track used by Spotify (randomly generated alphanumeric string)
- track_name and artist_name: track name
- popularity: song popularity score as of March 2021 on a normalized scale [0-100] where 100 is the most popular
- duration_ms: duration of track in milliseconds
- explicit: true or false if the song contains explicit content.
artists: name of the main artist
- release_date: when the album was released (date format: yyyy/mm/dd)

#### Sub Features
- danceability: describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- energy: measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
- key: The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is set to -1.
loudness: The overall loudness of a track in decibels (dB). Values typical range between -60 and 0 db.
mode: Mode indicates the modality (major=1 or minor=0) of a track, the type of scale from which its melodic content is derived.
- speechiness: measures from 0.0 to 1.0 and detects the presence of spoken words in a track. If the speechiness of a song is above 0.66, it is probably made of spoken words, a score between 0.33 and 0.66 is a song that may contain both music and words, and a score below 0.33 means the song does not have any speech.
- acousticness: confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic
instrumentalness: measure from 0.0 to 1.0 and represents the amount of vocals in the song. The closer it is to 1.0, the more instrumental the song is.
- liveness: likelihood measure from 0.0 to 1.0 and indicates the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live.
valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
- tempo: The overall estimated tempo of a track in beats per minute (BPM)
- time_signature: An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).


### 1.2 Questions and Hypothesis. (sample)

1. Does the price have an influence on the volume? 'Yes, the price has an influence on the volume, vice versa.'
2. Which areas consumed avocados the most from 2015 to 2021? 
3. the plu4770 being the biggest Hass variety, is it also the one consumed the most?
4. is the trend in the most consuming city a mirror image of the general trend in the U.S?

## 2. Approach and Analysis
### 2.1 Project Stages

Here, we created a workflow and project stages to make sure that our analysis is based of our target or main criteria. For this dataset, popularity is our main criteria and we will aligned our analysis relative to that feature.

| Stages | Output |
|---|---|
| 0. Basic Exploration of Dataset. | Explore the basics of pandas library; checking the information, describe, datatypes, columns, etc. |
| 1. Continue to Explore of the Dataset. | Here we explore further in-depth, given the Spotify Dataset. This includes and not limited to the following: checking the null, missing and 0 values, checking the histogram or distribution of each feature column, creating pandas-profiling html to automate exploratory data analysis.  |
| 2. Transforming the dataset. | Initial process would include converting the csv file to parquet file; this would reduce the file size by half. Removing data points that has null or 0 on the main criteria column (popularity and followings). Removing data points that is heavily skewed based on its histogram. Renaming the columns between the 2 dataset so that artist and track identifiers are separate. Merging the 2 datas based on the artist_id. Standard preprocessing such as sorting and resetting the index by the main criteria and transforming data based on its proper datatype. |
| 3. Main Criteria | The output is an analysis based on the main criteria, popularity, of the project. The analysis must be based of the main target or criteria of the project, therefore aligning all the graphs, reports and data output to the target. For the project, sample output would be... |
| 4. Feature Data | Afterwards, we focus on the other feature of the dataset - relative to the popularity. |


## 3. Result

### 3.1 Results (per stage)
Due to many results per stages, I am only going show some of the one to two images or data.

#### Exploring Dataset
#### Transforming Dataset

#### Main Column Features
#### Features

### 3.2 Takeaways and Recommendation
- Processing list of lists within pandas library is not a scalable solution, especially given a large datasets.
- Criteria should be emphasize at the early stage of the analysis. It gives the direction for the reports, datas and graphs to extract and process. In here, we emphasize on the tracks popularity; given the popularity what features are significantly higher.


## 4. Reference
- https://www.kaggle.com/code/vhtrieu/spotify-track-popularity-analysis-and-prediction