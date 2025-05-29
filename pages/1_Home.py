import streamlit as st
import pickle

# Load data
popular_df = pickle.load(open('popular.pkl', 'rb'))

st.set_page_config(page_title="Top 50 Books", layout="wide")

# Styling with adjusted text for card
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 24px;
        margin-bottom: 40px;
        color: #8fbc8f;
    }
    .card {
        background-color: #1c1c1c;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 40px;
        box-shadow: 0 8px 15px rgba(0, 166, 90, 0.3);
        text-align: center;
        height: 380px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s ease;
        overflow: hidden;
    }
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 20px rgba(0, 166, 90, 0.6);
    }
    .card img {
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .book-title {
        font-size: 18px;
        font-weight: 600;
        color: white;
        margin-bottom: 8px;
        flex-grow: 1;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .author, .votes, .rating {
        color: #a9a9a9;
        margin: 3px 0;
        font-size: 14px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<div class='title'>Top 50 Books</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore the most popular books curated just for you</div>", unsafe_allow_html=True)

# Display books in 4 columns with equal sized cards
cols = st.columns(4)

for idx, (title, author, img, votes, rating) in enumerate(zip(
        popular_df['Book-Title'].values,
        popular_df['Book-Author'].values,
        popular_df['Image-URL-M'].values,
        popular_df['num_ratings'].values,
        popular_df['avg_ratings'].values)):

    with cols[idx % 4]:
        st.markdown(f"""
            <div class='card'>
                <img src="{img}" alt="{title}" />
                <div class="book-title" title="{title}">{title}</div>
                <div class="author" title="{author}">Author: {author}</div>
                <div class="votes">Votes: {votes}</div>
                <div class="rating">Rating: {rating:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
