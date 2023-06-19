
import streamlit as st
import pandas as pd
from repo_complexity import find_most_complex_repository

# streamlit framework
st.title('Github Automated Analysis | Most Technically Complex And Challenging Repo')
github_url=st.text_input("Please Enter The GitHub User's URL For Analysis")


# Example github_url = 'https://github.com/vksmadheshiya'
most_complex_repository, complexity_report = find_most_complex_repository(github_url)


if github_url:
    if most_complex_repository :
        st.write(f" # The most technically complex repository from user '{github_url}' is '{most_complex_repository}'.")
        st.write('Below is a Complexity Report:', pd.DataFrame(complexity_report))

    else:
        st.write("Some Error Occured")
    
