import streamlit as st
from PIL import Image
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time
import base64


import os
import matplotlib.font_manager as fm

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
plt.rc('font', family='NanumSquareRound')
mpl.rcParams['axes.unicode_minus'] = False

st.header(":face_with_cowboy_hat:선공 결정하기",divider="rainbow")
content1='게임에서 :blue[주사위 1개의 눈의 수를 맞춘 학생]이 :red[선공!]'
st.markdown(content1,help="주사위 눈의 수를 맞출 확률은?")


dice = [1, 2, 3, 4, 5, 6]
predict = st.radio("주사위 눈의 예상 숫자를 골라주세요.", ("1", "2", "3", "4", "5", "6"))

container = st.container()
container.write("")

if "try_n" not in st.session_state:
    st.session_state["try_n"] = 0

if "sucess" not in st.session_state:
    st.session_state["sucess"] = 0

if "end" not in st.session_state:
    st.session_state["end"] = False

file_ = open("dice.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

dice_container = st.empty()
with dice_container.container():
    st.write("")

whitedice1 = Image.open('whitedice1.png')
whitedice2 = Image.open('whitedice2.png')
whitedice3 = Image.open('whitedice3.png')
whitedice4 = Image.open('whitedice4.png')
whitedice5 = Image.open('whitedice5.png')
whitedice6 = Image.open('whitedice6.png')


def roll_dice():
    with dice_container.container():
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">', unsafe_allow_html=True)
    time.sleep(1.5)
    dice_container.empty()
    choice = random.choice(dice)
    if choice == 1:
        container.image(whitedice1, width=100)   
    elif choice == 2:
        container.image(whitedice2, width=100)
    elif choice == 3:
        container.image(whitedice3, width=100)
    elif choice == 4:
        container.image(whitedice4, width=100)
    elif choice == 5:
        container.image(whitedice5, width=100)
    else:
        container.image(whitedice6, width=100)
    if int(choice) == int(predict):
        st.session_state["try_n"] = st.session_state["try_n"] + 1
        st.session_state["sucess"] = st.session_state["sucess"] + 1
        container.write("시행횟수 : {}".format(st.session_state["try_n"]))
        container.write("맞춘횟수 : {}".format(st.session_state["sucess"]))
        container.write("예측이 맞았습니다.")
        st.session_state["end"] = True
    else:
        st.session_state["try_n"] = st.session_state["try_n"] + 1
        container.write("시행횟수 : {}".format(st.session_state["try_n"]))
        container.write("맞춘횟수 : {}".format(st.session_state["sucess"]))
        container.write("예측이 틀렸습니다.")

def restart():
    st.session_state["end"] = False
    st.session_state["try_n"] = 0
    st.session_state["sucess"] = 0

st.button('주사위 굴리기', on_click=roll_dice, disabled=st.session_state["end"])
st.button('다시하기', on_click=restart)

st.write("")    
st.divider()
st.write("")

st.write("시행횟수에 따라 달라지는 주사위 1개를 굴릴 때 마다 나오는 눈의 수를 그래프로 확인해봅시다.")
try_n_2 = st.slider('시행횟수를 입력하세요.', 10, 10000, 10, 10)

choice2_list = []

for i in range(try_n_2):
    choice2 = random.choice(dice)
    choice2_list.append(choice2)

a = choice2_list.count(1)/try_n_2
b = choice2_list.count(2)/try_n_2
c = choice2_list.count(3)/try_n_2
d = choice2_list.count(4)/try_n_2
e = choice2_list.count(5)/try_n_2
f = choice2_list.count(6)/try_n_2

right_N = [a, b, c, d, e, f]
dice_N= ['1','2','3','4','5','6']
index = np.arange(len(dice_N))

if st.button('그래프 그리기'):
    fig = plt.figure()
    plt.bar(index, right_N)
    plt.title('주사위 그래프', fontsize=18)
    plt.xlabel('주사위 눈', fontsize=15)
    plt.ylabel('상대도수', fontsize=15)
    plt.xticks(index, dice_N, fontsize=12)
    st.pyplot(fig)