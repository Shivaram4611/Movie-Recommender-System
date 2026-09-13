# Content-Based Movie Recommender System

A content-based movie recommendation web application built using Python, Pandas, Scikit-learn, and Streamlit. The system recommends five similar movies based on metadata including overview, genres, keywords, top cast, and director.

---

## Features

- **Metadata Processing**: Extracts, cleans, and vectorizes genres, keywords, cast members, and directors from raw metadata formats.
- **Content Similarity**: Calculates cosine similarity across tags to determine movie relationships.
- **Interactive UI**: Streamlit web dashboard allowing users to select any movie and instantly fetch recommendations.

---

## Dataset

This project uses the TMDB 5000 dataset:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Both files should be downloaded (e.g., from Kaggle's TMDB 5000 Movie Dataset) and used during the model preprocessing stage.

---

## Project Structure

```text
├── app.py                   # Streamlit web application
├── movie_recommender.ipynb  # Data preprocessing and model creation notebook
├── requirements.txt         # Project dependencies
├── movie_dict.pkl           # Pickled dataframe dictionary (generated from notebook)
├── similarity.pkl           # Pickled similarity matrix (generated from notebook)(file is more then 100 mb)
└── README.md                # Project documentation

## Live Link
https://movie-recommender-system0101.streamlit.app/
