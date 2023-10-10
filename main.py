import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import random as rd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def make_triage(Num, Over, Under):
    triage_list = np.zeros((Num, 2), dtype="i")
    a=0
    while Num<=1000 :
        triage_list[a][0]=rd.randint(1, 4)
        triage_list[a][1]=compare_triage(a, triage_list, Over, Under)
        Num-=1
        a+=1
    return triage_list

def compare_triage(a, compare, Over, Under) :
    dummy = rd.randint(1, 4)
    while 1:
        if dummy==compare :
            return dummy

        elif dummy<compare :
            dummy2=rd.randint(1, 101)
            if dummy2<=Under :
                return dummy
            else :
                continue

        else :
            dummy2=rd.randint(1, 101)
            if dummy2<=Over :
                return dummy
            else :
                continue

tab1, tab2, tab3 = st.tabs(['Home', '프로젝트 결과', '프로젝트 설명'])

with tab1:
    st.info('예측 및 시행은 프로젝트 결과에 있습니다.')

with tab2:
    with st.form('Form data'):
            Num = st.number_input('트리아지 수', min_value=0, max_value=1000)
            Overp = st.number_input('오버트리아지 확률(%무시)', min_value=0, max_value=100)
            Underp = st.number_input('언더트리아지 확률(%무시)', min_value=0, max_value=100)
            if st.form_submit_button('확인'):
                triage_list=np.random.randint(1, 4, size=(Num, 2))
                i = 0
                while i<Num :
                    triage_list[i, 1]=compare_triage(i, triage_list[i, 0], Overp, Underp)
                    i+=1
                st.write(triage_list)
                i=0
                percentage=100
                while i<Num :
                    if triage_list[i, 0] != triage_list[i, 1]:
                        percentage-=1/Num*100
                    i+=1
                st.write(f'실제 트리아지 적중도는 {100-Overp-Underp}%입니다.')
                st.write(f'예측된 트리아지 적중도는 {100-percentage/4}%입니다.')

with tab3:
    st.write("본 프로젝트는 트리아지를 오버트리아지, 언더트리아지 레벨을 설정하고 생성, 트리아지를 서로 구분해서 예측하고, 실제 트리아지 확률과 얼마나 차이가 나는지 확인하는 프로젝트입니다.")
    st.write("원래 실제 트리아지를 이용하여 사용하려 했으나, 트리아지 값은 따로 어디서 구할 수가 없어서 어쩔 수 없이 rand함수를 이용해서 임의로 생성했습니다.")