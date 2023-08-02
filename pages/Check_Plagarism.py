import streamlit as st
from document_similarity import get_results

student_files = st.file_uploader("Upload Student Files", type=["txt"], accept_multiple_files=True, key="students")

if len(student_files) <2:
    st.error("Upload atleast 2 files.")
else:
    with st.spinner("Please wait till all files are compared for plagarism, this will take some time."):
        notes = [_file.read().decode("utf-8") for _file in student_files]
        s_names = [_file.name for _file in student_files]
        scores = get_results(notes,s_names)
        text_data=""
        for data in scores:
            text_data+="Similarity between {0} and {1} is {2} percent.\n".format(data[0],data[1],data[2])
        st.download_button("Download the plagarism details", data=text_data, file_name="plagarism_scores.txt", key="similarity_scores")