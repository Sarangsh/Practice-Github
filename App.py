import streamlit as st


st.title('Test app for Github')


col1, col2 = st.columns(2)

with col1:
    st.image('/Users/sarangsh/Documents/GitHub/Practice-Github/Neymar-2.jpeg',caption='Neymar')

with col2:
    st.write('''Neymar is one of my favorite players in the world. I am disappointed when he is not playing.''')

st.header('Lets go')
st.subheader('Dribbling - 90')

st.sidebar.title('Neymar stats')
st.sidebar.markdown('''

-Hairstyle - WOW
- Flair - Incredible
- Hunger - Ecstatic
                    
''')