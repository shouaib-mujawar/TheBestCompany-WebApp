import streamlit as st
import pandas as pd
from send_email import send_email

st.set_page_config(layout="wide")

df=pd.read_csv("./topics.csv")

with st.form(key="contact"):
    user_email=st.text_input(label="Your Email Address")
    option=st.selectbox("What topic do you want to discuss?",df["topic"])
    raw_message=st.text_area(label="Text")
    message = f"""\
        Subject: New email from {user_email}

        From: {user_email}
        Topic: {option}
        {raw_message}
        """
    submit=st.form_submit_button("Send")
    if submit:
        send_email(message)
        st.info("Your email was sent successsfully!!!!")
