# -*- coding: utf-8 -*-
import pandas as pd 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager as fm
fpath = os.path.join(os.getcwd(), "S-Core-Dream_OTF/SCDream9.ttf")
prop = fm.FontProperties(fname=fpath)
@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df

def main():
    st.title("그냥", fontproperties=prop)   
    tips = load_data()

    # 데이터가공
    m_tips = tips.loc[tips['sex'] == '남성', :]
    f_tips = tips.loc[tips['sex'] == '여성', :]

    # 시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x = m_tips['total_bill'], y = m_tips['tip'])
    ax[0].set_title('남성', fontproperties=prop)
    ax[1].scatter(x = f_tips['total_bill'], y = f_tips['tip'])
    ax[1].set_title('여성', fontproperties=prop)

    # 중요포인트
    # plt.show()
    st.pyplot(fig)

if __name__ == "__main__":
    main()