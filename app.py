import streamlit as st
import pickle
import pandas as pd

# recommend function will sort the movie list and find similarity relation b/w movies and will return 5 similar movies as recommendation
def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

  recommended_movies = []
  for i in movies_list:
      movie_id = i[0]
      # fetching poster from API

      recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies

# creating the dictionary to store the movie titles
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

# selection box to select the movie for the recommendation
selected_movie_name = st.selectbox(
'How would you like to be contacted?',
      movies['title'].values
)

# loading the similarity data b/w the movies
similarity = pickle.load(open('similarity.pkl', 'rb'))

# conditional statement will recommend top 5 similar movies as per our movie selection
if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)