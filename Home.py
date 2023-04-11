import streamlit as st
import pandas

# Set the webpage layout to wide
st.set_page_config(layout="wide")

# Set a header and some text
st.header("The Best Company")
st.write("""
Lorem ipsum dolor sit amet,Should learn how to add Lorem Ipsum text
count in Pycharm.
""")
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with company members
df = pandas.read_csv("data.csv")

# Add content to the first column

with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        # Add a member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        # Add a member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the third row
with col3:
    # Iterate over rows 8 to 12
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        # Add a member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])
