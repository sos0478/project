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

file_ = open("dice2.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


st.header(":desert_island:무인도 탈출하기",divider="rainbow")
st.write("운이 나쁘게도 무인도에 갇혀버렸다.")
st.write("무인도를 탈출하려면 :blue[주사위 2개를 동시에 던져서 나온 두 눈의 수가 같아야 한다].")
content3='몇 번만에 :red[무인도를 탈출]할 수 있을까?'
st.markdown(content3,help="무인도를 탈출할 확률은?")
container = st.container()
container.write("")

dice = [1, 2, 3, 4, 5, 6]

dice_container = st.empty()
with dice_container.container():
    st.write("")


whitedice1 = Image.open('whitedice1.png')
whitedice2 = Image.open('whitedice2.png')
whitedice3 = Image.open('whitedice3.png')
whitedice4 = Image.open('whitedice4.png')
whitedice5 = Image.open('whitedice5.png')
whitedice6 = Image.open('whitedice6.png')
blackdice1 = Image.open('blackdice1.png')
blackdice2 = Image.open('blackdice2.png')
blackdice3 = Image.open('blackdice3.png')
blackdice4 = Image.open('blackdice4.png')
blackdice5 = Image.open('blackdice5.png')
blackdice6 = Image.open('blackdice6.png')

if "try_n3" not in st.session_state:
    st.session_state["try_n3"] = 0

if "end3" not in st.session_state:
    st.session_state["end3"] = False


def roll_dice3():
    with dice_container.container():
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">', unsafe_allow_html=True)
    time.sleep(1.5)
    dice_container.empty()
    choice1 = random.choice(dice)
    choice2 = random.choice(dice)
    if choice1 == 1:
        container.image(whitedice1, width=100)   
    elif choice1 == 2:
        container.image(whitedice2, width=100)
    elif choice1 == 3:
        container.image(whitedice3, width=100)
    elif choice1 == 4:
        container.image(whitedice4, width=100)
    elif choice1 == 5:
        container.image(whitedice5, width=100)
    else:
        container.image(whitedice6, width=100)
    if choice2 == 1:
        container.image(blackdice1, width=100)   
    elif choice2 == 2:
        container.image(blackdice2, width=100)
    elif choice2 == 3:
        container.image(blackdice3, width=100)
    elif choice2 == 4:
        container.image(blackdice4, width=100)
    elif choice2 == 5:
        container.image(blackdice5, width=100)
    else:
        container.image(blackdice6, width=100)
    if int(choice1) != int(choice2):
        st.session_state["try_n3"] = st.session_state["try_n3"] + 1
        container.write("시행횟수 : {}".format(st.session_state["try_n3"]))
        container.write("무인도를 탈출하지 못했습니다.")
    else:
        st.session_state["try_n3"] = st.session_state["try_n3"] + 1
        container.write("시행횟수 : {}".format(st.session_state["try_n3"]))
        container.write("{}번 만에 무인도를 탈출했습니다.".format(st.session_state["try_n3"]))
        st.session_state["end3"] = True

def restart3():
    st.session_state["end3"] = False
    st.session_state["try_n3"] = 0

st.button('주사위 굴리기', on_click=roll_dice3, disabled=st.session_state["end3"])
st.button('다시하기', on_click=restart3)

st.write("")    
st.divider()
st.write("")

st.write("무인도 탈출을 성공한 횟수를 설정하고, 성공을 할 때마다 무인도를 탈출할 때까지 주사위를 던진 횟수의 상대도수를 그래프로 확인해봅시다.")
try_n_2 = st.slider('시행횟수를 입력하세요.', 10, 10000, 10, 10)

try_list = []
success_list = []
try_list2 = []
success_list2 = []
try_dic = {}

def get_counts(seq): 
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts




if st.button('그래프 그리기'):
    try_n_3 = 1
    while try_n_2 >= try_n_3 :
        dice1 = random.choice(dice)
        dice2 = random.choice(dice)
        n = 1
        while int(dice1) != int(dice2):
            n = n + 1
            dice1 = random.choice(dice)
            dice2 = random.choice(dice)
        try_list.append(n)
        n = 0
        try_n_3 = try_n_3 + 1
    try_list.sort()
    try_dic = get_counts(try_list)
    try_list2 = list(try_dic.keys())
    success_list = list(try_dic.values())
    
    index = np.arange(len(try_list2))
    for i in success_list:
        i = i/sum(success_list)
        success_list2.append(i)
    fig = plt.figure()
    plt.bar(index, success_list2)
    plt.title('주사위 그래프', fontsize=18)
    plt.xlabel('성공까지 걸린 횟수', fontsize=15)
    plt.ylabel('상대도수', fontsize=15)
    plt.xticks(index, try_list2, fontsize=5)
    st.pyplot(fig)






