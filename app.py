import pandas as pd
import streamlit as st
import pickle
import requests
st.title('Movie Recommender System')

# fetching pickle dump files
movieDict = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# fetching movie items
movies = pd.DataFrame(movieDict)

# function for fetch poster
def fetchPoster(movieId):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=195e3d35294310616a256eced2eb9520&language=en-US'.format(movieId))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']

# function for recommendation
def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieIndex]
    movieList = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movieList:
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetchPoster(movies.iloc[i[0]].movie_id))
    return recommend_movies, recommend_movies_posters

# Movie fields
selectedMovieName = st.selectbox(
'Select a movie to get Five more movie recommended',
movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selectedMovieName)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])




