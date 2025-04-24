import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('My demo app')

st.header('This is a header')

st.subheader('A subheader')

st.write('plain text')
df = pd.read_csv('tips.csv')

st.dataframe(df, width=600, height=200)

st.markdown('---')
st.markdown('[NY Times](https://www.nytimes.com)')
st.markdown('''
            * item 1
            * item 2
            * item 3
''')

# Image 
st.image('image.png', caption='my image', width=400)

st.latex(r'''\frac{x}{y^2}''')

t1, t2 = st.tabs(['Tips', 'Bill'])

with t1:
    fig = plt.figure()
    plt.hist(df['tip'], bins=20)
    st.pyplot(fig)

with t2:
    fig = plt.figure()
    plt.hist(df['total_bill'], bins=20)
    st.pyplot(fig)

c1, c2 = st.columns(2)

with c1:
    fig = plt.figure()
    plt.hist(df['tip'], bins=20)
    st.pyplot(fig)

with c2:
    fig = plt.figure()
    plt.hist(df['tip'], bins=20)
    st.pyplot(fig)

status = st.radio("Select your enrollment status",
                  ('Full time', 'Part time'))
if status == 'Full time':
    st.write('You selected full time')
else:
    st.write('You selected part time')

major = st.selectbox('Select your major',
                        ('ACC', 'CS', 'DS', 'CHE'))
if major == 'ACC':
    st.write('you selected accounting')
elif major == 'CS':
    st.write('you selected computer science')


options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)

price = st.slider("Enter price range", 1, 100, (20, 40))
st.write(price)

