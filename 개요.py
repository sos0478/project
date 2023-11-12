import streamlit as st
from streamlit_extras.switch_page_button import switch_page

page = "상황_1.py"
image = 'game.png'

st.title(":game_die: Welcome to 부루마불 :game_die:")
st.image(image)
if st.button("Game Start"):
    switch_page("상황_1")