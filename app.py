import streamlit as st

st.set_page_config(page_title="Book Recommender", layout="wide")

# Title and welcome
st.title("📚 My Book Recommender")
st.markdown("Welcome! Use the sidebar to navigate between pages.")

# Spacer
st.markdown("---")

# 📌 Model Description
st.subheader("🔍 How This Recommender Works")

st.markdown("""
This intelligent book recommender system helps you discover great books tailored to your reading preferences.
Whether you're into mystery, romance, or non-fiction, it finds books that match your taste!

### 🧠 The Technology Behind It
- **Collaborative Filtering**: Our model uses user behavior (what books people rate and read) to find patterns and suggest similar books.
- **Cosine Similarity**: We calculate how close two books are in terms of user interest, using a mathematical similarity score.
- **Preprocessed Data**: The model runs on a pivot table of users and books, optimized for quick lookup and recommendations.

### 📈 Data Used
- Over **thousands of book titles**, authors, and cover images.
- Millions of real-world **user ratings** from an open dataset.
- A curated list of the **Top 50 Most Popular Books** to explore.

### 🚀 Features You’ll Love
- 🎯 One-click recommendations for any book you like
- 🖼️ Clean visuals with book covers and author names
- ⚡ Built with Streamlit for fast and easy interaction
""")
