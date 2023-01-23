# Spotify Dataset - Data Analysis

- Introduction and Background
- Body
- Interpreting the data
- Conclusion, Takeaway, Recommendation



This is a compilation of some of my exploration in the course data analysis in Datacamp.

Analysis of the Spotify datasets.

## Data Collection

The dataset is from Kaggle. Here is the link to the [Spotify Dataset](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets).

---

### Project Stages

Here, we created a workflow and project stages to make sure that our analysis is based of our target or main criteria. For this dataset, popularity is our main criteria and we will aligned our analysis relative to that feature.

| Stages | Output |
|---|---|
| 0. Basic Exploration of Dataset. | Explore the basics of pandas library; checking the information, describe, datatypes, columns, etc. |
| 1. Continue to Explore of the Dataset. | Here we explore further in-depth, given the Spotify Dataset. This includes and not limited to the following: checking the null, missing and 0 values, checking the histogram or distribution of each feature column, creating pandas-profiling html to automate exploratory data analysis.  |
| 2. Transforming the dataset. | Initial process would include converting the csv file to parquet file; this would reduce the file size by half. Removing data points that has null or 0 on the main criteria column (popularity and followings). Removing data points that is heavily skewed based on its histogram. Renaming the columns between the 2 dataset so that artist and track identifiers are separate. Merging the 2 datas based on the artist_id. Standard preprocessing such as sorting and resetting the index by the main criteria and transforming data based on its proper datatype. |
| 3. Main Criteria | The output is an analysis based on the main criteria, popularity, of the project. The analysis must be based of the main target or criteria of the project, therefore aligning all the graphs, reports and data output to the target. For the project, sample output would be... |
| 4. Feature Data | Afterwards, we focus on the other feature of the dataset - relative to the popularity. |

---
## Roadmap


## Takeaways
- Processing list of lists within pandas library is not a scalable solution, especially given a large datasets.
- Criteria should be emphasize at the early stage of the analysis. It gives the direction for the reports, datas and graphs to extract and process. In here, we emphasize on the tracks popularity; given the popularity what features are significantly higher.