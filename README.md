Movie Recommendation System (Content-Based Filtering) --

A Streamlit-based movie recommender app using The Movie Database (TMDb) datasets, designed to recommend movies to users based on a selected movie, showing similar titles and fetching their posters.
The system recommends movies similar to a selected title using content-based filtering.


Approach:

Merged TMDb movie & credits datasets.

Preprocessed genres, keywords, cast, crew, and overview.

Created a combined "tags" column for each movie.

Used CountVectorizer for text vectorization and cosine similarity for similarity computation.

Stored precomputed similarity matrix and movie metadata with pickle for fast loading.

Fetched movie posters dynamically from TMDb API.

Tech Stack: Python, Pandas, CountVectorizer, Cosine Similarity, Pickle, Streamlit, TMDb API.
Filtering Type: Content-Based Filtering (metadata similarity).
Result: Given a movie, the app recommends 5 similar movies with poster previews.



