import streamlit as st
from functions.summarize import call_summarize_endpoint


st.markdown("""
    <style>
    .stButton>button {
        color: lightgreen;
        border: 2px solid green;
    }
    .stTextArea>div>textarea {
        text-color: white;
        border: 2px solid #d3d3d3; /* Default border color */
    }
    .stTextArea>div>textarea.error {
        border: 2px solid red;
    }
    .stTextArea>div>textarea.success {
        border: 2px solid green;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Text Summarizer")
st.write("")

# Create two columns
col1, col2 = st.columns([4, 3])

# Input text box in the left column
with col1:
    st.subheader("Input Text")
    input_text = st.text_area("Enter text to summarize here", placeholder="blah blah blah", height=300)
    summarize_button = st.button("Summarize")

# Output summary box in the right column
with col2:
    st.subheader("Summary")
    if input_text and summarize_button:
        # Call your summarization function here
        summary = call_summarize_endpoint(input_text)
        if "Err" in summary:
            st.text_area("summary", value=summary["Err"], height=300, label_visibility="hidden", disabled=True, key="error")
        else:
            st.text_area("summary", value=summary, height=300, label_visibility="hidden", disabled=True, key="success")
    else:
        st.text_area("summary", placeholder="blah", height=300, label_visibility="hidden", disabled=True)