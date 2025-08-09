import pickle
import pandas as pd
import streamlit as st
# Load the dataset

data = pickle.load(open('movie_dict.pkl', mode='rb'))
data = pd.DataFrame(data)
# print(data)

similarity = pickle.load(open('similarity.pkl', mode='rb'))
# print(similarity)

# Recommendation Function

def recommend(movie):
    
    recommended_movies = []

    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies


# print(recommend('Iron Man'))


# Streamlit Web-App

st.title(':blue[Movie Recommendation System]')
selected_movie = st.selectbox("Select a movie to get similar recommendation -", list(data['title'].values))
btn = st.button('Recommend')

if btn:

    top_5_movies = recommend(selected_movie)
    
    for i in top_5_movies:
        st.write(i)