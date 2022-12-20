import streamlit as st

st.title('뱁미귀엽다')
st.text('유빈님픽뚫로 치치나오길')

from PIL import Image
image = Image.open('붸.png')

st.image(image, caption='뷉미')