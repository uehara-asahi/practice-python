from numpy.lib.shape_base import expand_dims
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time

st.title("streamlit 超入門")
st.write("DataFrame")

st.write("プレグレスバーの表示")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Itaretion{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

# left_column, right_column = st.columns(2)
# button_right = left_column.button("右カラムに文字を表示")
# if button_right:
#     right_column.write("ここは右カラム")

# expander = st.expander("問い合わせ")
# expander.text_input("問い合わせ内容を書く")


# option = st.selectbox(
#     "あなたの好きな数字を教えてください",
#     list(range(1,11))
# )

# "あなたの好きな数字は",option, "です"

# text = st.text_input("あなたの趣味を教えてください")
# "あなたの趣味:",text

# condition = st.slider("あなたの今の調子は?",0 ,100,50)
# "コンディション：",condition

#一括コメント→ctrl k + ctrl c
#コメント解除→ctrl k + ctrl u
# if st.checkbox("Show Image"):
#    img = Image.open("sample.jpg")
#    st.image(img, caption="shibainu", use_column_width=True)
# df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=["lat","lon"]
# )
# df2 = pd.DataFrame(
#    np.random.rand(100,2),
#    columns=["lat","lon"]
# )
# st.map(df)
# st.line_chart(df2)
# st.dataframe(df2)
