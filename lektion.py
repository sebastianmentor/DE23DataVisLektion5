import streamlit as st 
import time
# Set the app title
st.title('My First Streamlit App')
# Add a welcome message 
st.write('Welcome to my Streamlit app!') 
# Create a text input 1
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
st.write('Customized Message:', user_input)


class_names = st.text_input('Skriv ditt namn')
while True:
    try:
        with open('class_names.txt','a', encoding='utf-8') as f:
            f.write(class_names + '\n')
    except:
        time.sleep(0.01)
    else:
        break


while True:
    names = []
    try:
        with open('class_names.txt','r', encoding='utf-8') as f:
            for l in f:
                names.append(l)
    except:
        time.sleep(0.01)
    else:
        break
    

st.write(names)
