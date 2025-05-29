import streamlit as st
import pickle
import numpy as np

pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

st.set_page_config(page_title="Book Recommender", layout="wide")

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
        margin-bottom: 5px;
        flex-grow: 1;
    }
    .author {
        color: #a9a9a9;
        margin: 2px 0;
    }
    .recommend-section {
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📚 Recommend Books</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Find books similar to your favorites</div>", unsafe_allow_html=True)

book_list = pt.index.values
user_input = st.selectbox("Select a book to get recommendations", book_list)

if st.button("Recommend"):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]  # only 4 recommendations

    st.markdown("<div class='recommend-section'>", unsafe_allow_html=True)
    cols = st.columns(4)

    for i, item in enumerate(similar_items):
        book_title = pt.index[item[0]]
        temp_df = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')

        title = temp_df['Book-Title'].values[0]
        author = temp_df['Book-Author'].values[0]
        image_url = temp_df['Image-URL-M'].values[0]

        with cols[i]:
            st.markdown(f"""
                <div class='card'>
                    <img src="{image_url}" alt="{title}" />
                    <div class="book-title">{title}</div>
                    <div class="author">Author: {author}</div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
