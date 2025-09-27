Movie Recommendation System (Content-Based Filtering) --

1. Project Overview

A Streamlit-based movie recommender app using The Movie Database (TMDb) datasets, designed to recommend top 5 most similar titles along with their posters.
The system recommends movies similar to a selected title using content-based filtering.


2. Data Preparation
  Loading datasets: Read movies.csv and credits.csv into pandas DataFrames.
  
  Merging: Joined on the common id field to consolidate metadata (genres, overview) with cast & crew information.
  
  Handling missing data: Filled or dropped nulls to ensure completeness before feature extraction.

3. Feature Engineering
  Parsing JSON columns:
  
  genres, keywords, cast, crew are JSON-encoded strings.
  
  Extracted only the names (e.g., genre names, top 3 cast members, director).
  
  Text preprocessing:
  
  Converted all text to lowercase.
  
  Removed spaces within multi-word tags (e.g., "science fiction" → "sciencefiction") to treat each as a single token.
  
  Combined “tags”:
  
  Concatenated genres + keywords + cast + crew + overview into a single string per movie.

4. Vectorization & Similarity
  CountVectorizer:
  
  Fitted on the combined “tags” corpus (max features ≈ 5000).
  
  Transformed each movie’s tags into a vector of token counts.
  
  Cosine Similarity:
  
  Computed pairwise cosine similarity matrix on the CountVectorizer output.
  
  Stored as a NumPy array for fast lookups.

5. Model Persistence
  Pickle serialization:
  
  Saved the DataFrame of movie metadata, the similarity matrix, and the fitted CountVectorizer to disk.
  
  Enables instant loading in the Streamlit app without reprocessing.

6. Streamlit App
  Interface:
  
  Dropdown menu lists all movie titles.
  
  User selects a movie and clicks “Recommend.”
  
  Backend logic:
  
  Loads pickled objects.
  
  Finds the index of the selected title.
  
  Retrieves similarity scores for that index, sorts them, and picks the top 5.
  
  Dynamically fetches poster URLs using TMDb’s image base URL and the recommended movie IDs.

7. Technologies & Libraries
Python 3.x, pandas, NumPy

scikit-learn’s CountVectorizer & cosine_similarity

pickle for serialization

Streamlit for front-end

TMDb API for poster images

