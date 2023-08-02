from mcq import getMCQ
import re
import random
import streamlit as st 

mcq_file = st.file_uploader("Upload text to generate MCQ questions from", type=["txt"], accept_multiple_files=False, key="mcq")

if mcq_file:
    with st.spinner("Please wait till the MCQ questions are generated, this will take some time."):
        notes = mcq_file.read().decode("utf-8")
        key_distractor_list, keyword_sentence_mapping = getMCQ(notes)
        index = 1
        text_data=""
        for each in key_distractor_list:
            sentence = keyword_sentence_mapping[each][0]
            pattern = re.compile(each, re.IGNORECASE)
            output = pattern.sub( " _______ ", sentence)
            text_data+="%s)"%(index)+" "+output+"\n"
            choices = [each.capitalize()] + key_distractor_list[each]
            top4choices = choices[:4]
            random.shuffle(top4choices)
            optionchoices = ['a','b','c','d']
            for idx,choice in enumerate(top4choices):
                text_data+="\t"+optionchoices[idx]+")"+" "+choice
            text_data+="\nMore options: \n"
            for i in range(4,min(21,len(choices))):
                text_data+=choices[i]+"\n"
            text_data+="\n\n"
            index = index + 1
        st.download_button("Download the MCQ questions", data=text_data, file_name="MCQ_questions.txt", key="mcq_ques")     
else:
    st.error("No file were uploaded")