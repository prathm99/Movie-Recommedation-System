import pickle
import streamlit as st
import pandas as pd
import requests

similarity = pickle.load(open("similarity.pkl", 'rb'))
# mov_list = pickle.load(open('movlist.pkl','rb'))

# fetching the movie titles to show in the drop down
# mov_list = mov_list.title.values

# used the movie dict as it was throwing error while showing in the dropdown
movdict=pickle.load(open('movdict.pkl','rb'))
movies= pd.DataFrame(movdict)


st.title("Movie Recommendation System By Prathm!!")

selected_mov = st.selectbox("Enter the movie name", movies.title.values) 

# function to fetch poster given movie id
def fetch_poster(id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=23359d63b5cdcb6766460c886cf34f98&language=en-US")
    # so this response will give us the text in dict format we will conver it to json
    # and the poster png is saved under poster_path variable
    # https://api.themoviedb.org/3/movie/19995?api_key=23359d63b5cdcb6766460c886cf34f98&language=en-US
    # try hitting the above link to see the dict format 
    data = response.json()
    # as the poster_path is not complete we will be adding the https...
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# function to recommend movie
def recommend(mov):
    # here we are fetching the index of the movie which is selected
    mov_index = movies[movies['title'] == mov].index[0]
    # as we have similarity score already calculated we are fetching that index of the similarity
    dist = similarity[mov_index]
    # here are fetching top 5 similar movies, enumerate function will retain the index as we are sorting the
    # similarity in descending order
    result = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_mov = []
    recommended_mov_poster = []
    for i in result:
        # now as the result will be like this so we are taking the first index which is the index loc of movies
        # and we will fetch there title
        # [(12, 0.4140043409440133),
        #  (199, 0.27500954910846337),
        #  (17, 0.2533201985524494),
        #  (216, 0.20579830217101058),
        #  (3572, 0.20579830217101058)] 

        # fetching the movie id
        movie_id = movies.iloc[i[0]].movie_id
        recommended_mov.append(movies.iloc[i[0]].title)
        # fetching poster from the api and appending it.
        recommended_mov_poster.append(fetch_poster(movie_id))
    return recommended_mov, recommended_mov_poster

if st.button("Recommend"):
    names, poster = recommend(selected_mov)
    st.write('Here are your recommendation similar to ', selected_mov, ":")
    col1, col2, col3, col4, col5 = st.columns(5)

    # for i in range(5):
    #     with col1,col2,col3,col4,col5:
    #         st.text(names[i])
    #         st.image(poster[i])
    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])
    
    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])
       

    with col5:
        st.text(names[4])
        st.image(poster[4])
