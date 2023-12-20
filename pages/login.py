import streamlit as st
import pandas as pd
import datetime as datetime

def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In"):
        user_data = pd.read_csv(USER_DATA_FILE)
        if username in user_data["username"].values and user_data.loc[user_data["username"] == username, "password"].values[0] == password:
            st.success(f"Welcome, {username}!")
            return True
        else:
            st.error("Invalid username or password. Please try again.")
    return False

def signup():
    st.subheader("Sign Up")
    new_username = st.text_input("New Username", key="signup_username")
    new_password = st.text_input("New Password", type="password", key="signup_password")

    if st.button("Sign Up"):
        user_data = pd.read_csv(USER_DATA_FILE)
        if new_username in user_data["username"].values:
            st.error("Username already exists. Please choose a different one.")
        else:
            new_user = pd.DataFrame({"username": [new_username], "password": [new_password]})
            user_data = pd.concat([user_data, new_user], ignore_index=True)
            user_data.to_csv(USER_DATA_FILE, index=False)
            st.success("Account created successfully. You can now log in.")
            return True
    return False