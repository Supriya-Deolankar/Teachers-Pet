from true_false import get_true_false
import streamlit as st

true_false_file = st.file_uploader("Upload text to generate True or False questions from", type=["txt"], accept_multiple_files=False, key="tf")

if true_false_file:
    with st.spinner("Please wait till the True or False questions are generated, this will take some time."):
        notes = true_false_file.read().decode("utf-8")
        questions_dict = get_true_false(notes)
        index = 1
        choice_list = ["a)","b)","c)","d)","e)","f)"]
        text_data=""
        for true_sentence in questions_dict:
            false_sentences = questions_dict[true_sentence]
            print_string = "**\n%s) True Sentence :**"%(str(index))
            text_data+=print_string
            text_data+="  "+true_sentence
            text_data+="  **\nFalse Sentences (GPT-2 Generated)**"
            for ind,false_sent in enumerate(false_sentences):
                print_string_choices = "**%s** %s"%(choice_list[ind],false_sent)
                text_data+=print_string_choices
            index = index+1
            text_data+="\n\n"
        st.download_button("Download the True or False questions", data=text_data, file_name="TrueOrFalse_questions.txt", key="tf_ques") 
        
else:
    st.error("No file were uploaded")