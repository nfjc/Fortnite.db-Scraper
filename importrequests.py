import requests
import streamlit as st
import json

# print(response.status_code)\
st.title("Fortnite Island Code Lookup")
islandCode = st.text_input("Enter an island code:")
outputtedJSON = None
while not islandCode:
    st.warning("Please enter an island code to continue.")
    st.stop()
response = None
if islandCode:
    response = requests.get(
        url="https://api.fortnite.com/ecosystem/v1/islands/" + islandCode,
        headers={'accept': 'application/json'}
    )
if response.status_code == 200:
    data = response.json()
    st.write(response.json())
    st.write("Code: " + data.get('code'))
    st.write("Creator Code: " + data.get('creatorCode'))
    st.write("Name: " + data.get('title'))
    st.write("Created In: " + data.get('createdIn'))
    st.write("Tags: " , data.get('tags'))

elif response.status_code == 404:
    st.write("The island with the specified code was not found.")
else:
    st.write("Error: Unable to reach the API.")
