import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import numpy as np

def loadmodel():
    clf=pickle.load(open("spam.pkl","rb"))
    return clf

def Vectorizer():
    cvnew=pickle.load(open("vectorizer.pkl","rb"))
    return cvnew

model=loadmodel()
cv=Vectorizer()

def WebAppPage():
    st.title("**SPAM**  💬  Detection Page: ")
    st.write("""Lets Get Started""")

    st.write("""Please select a **Mode** from the sidebar: """)

    # st.markdown("# Main page 🎈")
    # st.sidebar.markdown("# Main page 🎈")

    # st.markdown("# Page 2 ❄️")
    # st.sidebar.markdown("# Page 2 ❄️")
    # k=st.sidebar.selectbox("Use Examples or Own Message: ", ("Examples","Custom"))
    # if k=="Examples":
    #     page1()
    # else:
    #     page2()
    
    with st.sidebar:
        choose = option_menu("Use Examples or Own Custom Message: ", ["Examples","Custom"])

    if choose=="Examples":

        ExHam=(
        "Its a part of checking IQ",
        "Sorry my roommates took forever, it ok if I come by now?",
        "As a valued customer, I am pleased to advise you that following recent review of your Mob No. you are awarded with a å£1500 Bonus Prize, call 09066364589",
        "Ok lar i double check wif da hair dresser already he said wun cut v short.",
        "Thanks for your subscription to Ringtone UK your mobile will be charged å£5/month Please confirm by replying YES or NO.",
        "I plane to give on this month end",
        "U can call me now...",
        "Finished class where are you.",
        "I call you later, don't have network. If urgnt, sms me.",        
        "07732584351 - Rodger Burns - MSG = We tried to call you re your reply to our sms for a free nokia mobile + free camcorder",
        "SMS. ac Sptv: The New Jersey Devils and the Detroit Red Wings play Ice Hockey.",
        "Congrats! 1 year special cinema pass for 2 is yours.",        
        "Urgent UR awarded a complimentary trip to EuroDisinc Trav",
        "You are a winner U have been specially selected 2 receive å£1000 or a 4* holiday"
        "Sorry, I'll call later")

        Ham=st.selectbox("Select one example: ",ExHam)  
    
        # msg=input("ENTER THE MESSAGE: ")
        vect=cv.transform([Ham]).toarray()
        predict=model.predict(vect)
        if predict==[0]:
            st.write("IT'S A HAM!")
        else:
            st.write("IT'S A SPAM!")
    
    elif choose== "Custom":
        name = st.text_input('Enter your Message: ')
        vect=cv.transform([name]).toarray()
        predict=model.predict(vect)
        if predict==[0]:
            st.write("IT'S A HAM!")
        elif predict==[1]:
            st.write("IT'S A SPAM!")
        else:
            st.write("Enter the message, Then press ENTER! ")

WebAppPage()
