import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e4831aa6d53366fbabbe8ff851451a9f&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pickle.load(open("movies_dict.pkl", "rb"))
movies_df = pd.DataFrame(movies)

def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[:11]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances:
        # fetch the movie poster
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies_df.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.title('Movie Recommender System')

selected_mve_name = st.selectbox(
    "Search for a movie",
    movies_df['title'].values
)

if st.button("Recommend"):
    recommondations, poster = recommend(selected_mve_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(recommondations[0])
        st.image(poster[0])
    with col2:
        st.text(recommondations[1])
        st.image(poster[1])
    with col3:
        st.text(recommondations[2])
        st.image(poster[2])
    with col4:
        st.text(recommondations[3])
        st.image(poster[3])
    with col5:
        st.text(recommondations[4])
        st.image(poster[4])

    with col6:
        st.text(recommondations[5])
        st.image(poster[5])
    
    with col7:
        st.text(recommondations[6])
        st.image(poster[6])

    with col8:
        st.text(recommondations[7])
        st.image(poster[7])

    with col9:
        st.text(recommondations[8])
        st.image(poster[8])

    with col10:
        st.text(recommondations[9])
        st.image(poster[9])





        