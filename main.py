import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("X Q&A 🌱")
st.title("Ask me any questions related F1 and abroad studies")
btn = st.button("Create Knowledgebase")
if btn:
    print("adding data")
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])


# create_vector_db()



