import streamlit as st

st.set_page_config(page_title="Contact", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:white;'>📬 Contact</h1>", unsafe_allow_html=True)

st.write("If you'd like to get in touch:")
st.markdown("""
- 📧 Email: `you@example.com`
- 💼 LinkedIn: [YourProfile](https://www.linkedin.com)
- 🌐 Portfolio: [yourportfolio.com](https://yourportfolio.com)
""")
