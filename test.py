import streamlit as st
import pickle

from app import recommend

st.title('Movie Recommendation System')

mov_list = pickle.load(open('movlist.pkl','rb'))
mov_list = mov_list['title'].values

mov_index = mov_list[mov_list['title'] == 'Avatar'].index[0]
print(mov_index)
# using this to show the name of movies in dropdown
# option = st.selectbox('Please select a movie', mov_list)

# st.write('You selected:', option)

# if st.button('Recommend'):
#     recommend(option)
#     st.write('Movies are being recommending similar to ', option)
