import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time
import base64

plt.rc('font', family='Malgun Gothic')
mpl.rcParams['axes.unicode_minus'] = False

st.header("전략적 도시:statue_of_liberty: 매입하기",divider="rainbow")
st.write("운이 좋게도 우주여행 칸에 도착하여 :blue[원하는 도시를 하나 구입]할 수 있다.")
content2='다음 차례에 상대가 그 도시를 밟도록 하려면 :red[어느 도시를 구입]하는 것이 가장 유리할까?'
st.markdown(content2,help="상대가 각 도시에 도착할 확률은?")
st.write('(단, 구입할 수 없는 사회복지기금접수처, 황금열쇠, 우주여행은 선택할 수 없다.)')
game2 = Image.open('game2.png')
st.image(game2)

file_ = open("dice2.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

dice = [1, 2, 3, 4, 5, 6]
city = ['부에노스아이레스', '상파울루', '시드니', '부산', '하와이', '리스본', '퀸엘리자베스호', '마드리드', '도쿄']
city_N = st.selectbox("구입할 도시를 골라주세요.", city)

city_dice_N = {'사회복지기금접수처':1, '부에노스아이레스':2, '황금열쇠':3, '상파울루':4, '시드니':5, '부산':6, '하와이':7, '리스본':8, '퀸엘리자베스호':9, '마드리드':10, '우주여행':11, '도쿄':12}

container = st.container()
container.write("")

dice_container = st.empty()
with dice_container.container():
    st.write("")

if "try_n2" not in st.session_state:
    st.session_state["try_n2"] = 0

if "sucess2" not in st.session_state:
    st.session_state["sucess2"] = 0

if "end2" not in st.session_state:
    st.session_state["end2"] = False

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


def roll_dice2():
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
    if int(choice1) + int(choice2) == city_dice_N[city_N]:
        st.session_state["try_n2"] = st.session_state["try_n2"] + 1
        st.session_state["sucess2"] = st.session_state["sucess2"] + 1
        container.write("시행횟수 : {}".format(st.session_state["try_n2"]))
        container.write("맞춘횟수 : {}".format(st.session_state["sucess2"]))
        container.write("상대방이 구입한 도시에 도착했습니다.")
        st.session_state["end2"] = True
    else:
        st.session_state["try_n2"] = st.session_state["try_n2"] + 1
        container.write("시행횟수 : {}".format(st.session_state["try_n2"]))
        container.write("맞춘횟수 : {}".format(st.session_state["sucess2"]))
        container.write("상대방이 구입한 도시에 도착하지 않았습니다.")

def restart2():
    st.session_state["end2"] = False
    st.session_state["try_n2"] = 0
    st.session_state["sucess2"] = 0

st.button('주사위 굴리기', on_click=roll_dice2, disabled=st.session_state["end2"])
st.button('다시하기', on_click=restart2)

st.write("")    
st.divider()
st.write("")

try_n_2 = st.slider('시행횟수를 입력하세요.', 10, 2000, 10, 10)

choice2_list = []
choice3_list = []

for i in range(try_n_2):
    choice2 = random.choice(dice)
    choice2_list.append(choice2)

for i in range(try_n_2):
    choice3 = random.choice(dice)
    choice3_list.append(choice3)

choice_sum_list = [choice2_list_i + choice3_list_i for choice2_list_i, choice3_list_i in zip(choice2_list, choice3_list)]


a = choice_sum_list.count(1)/try_n_2
b = choice_sum_list.count(2)/try_n_2
c = choice_sum_list.count(3)/try_n_2
d = choice_sum_list.count(4)/try_n_2
e = choice_sum_list.count(5)/try_n_2
f = choice_sum_list.count(6)/try_n_2
g = choice_sum_list.count(7)/try_n_2
h = choice_sum_list.count(8)/try_n_2
i = choice_sum_list.count(9)/try_n_2
j = choice_sum_list.count(10)/try_n_2
k = choice_sum_list.count(11)/try_n_2
l = choice_sum_list.count(12)/try_n_2

right_N = [a, b, c, d, e, f, g, h, i, j, k, l]
dice_N= ['1','2','3','4','5','6','7','8','9','10','11','12']
index = np.arange(len(dice_N))

if st.button('그래프 그리기'):
    fig = plt.figure()
    plt.bar(index, right_N)
    plt.title('주사위 그래프', fontsize=18)
    plt.xlabel('두 주사위 눈의 합', fontsize=15)
    plt.ylabel('상대도수', fontsize=15)
    plt.xticks(index, dice_N, fontsize=12)
    st.pyplot(fig)