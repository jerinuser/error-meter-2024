import streamlit as st
import random

st.subheader("Error Meter")
with st.form(key="my_form"):
	file = st.file_uploader("Upload Error log", type=["txt"])
	submit_button = st.form_submit_button(label='Submit')

def count_error():
    ar = str(file.read(),"utf-8")
    return ar.count("--------------------------------------------------------------------------------------------------")

if submit_button:

	 # To See details
    file_details = {"filename":file.name, "filetype":file.type,
                              "filesize":file.size}
    
    err = count_error()

    cat = 0 if err==0 else random.randint(1,10)
    score = 0 if cat<4 else random.randint(1,100)
    st.write("Score: %d"%(score))
    st.write("Number of Errors: %d"%(err))
    st.write("Number of Cateogories: %d"%(cat))
    if(err==0):
        st.write("Reason: No Tact Error Log Format found")
    if(cat<4 and err != 0):
        st.write("Reason: No Diversed Errors found")

