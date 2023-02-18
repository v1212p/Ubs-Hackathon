import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#punctuation removal
import string
#importing nlp library
import nltk
from nltk.stem import WordNetLemmatizer

#Stop words present in the library
stopwords = nltk.corpus.stopwords.words('english')

from nltk.stem import WordNetLemmatizer
#defining the object for Lemmatization
wordnet_lemmatizer = WordNetLemmatizer()

job1_df=pd.read_excel('JD_dataset (1).xlsx')
profiles_df=pd.read_excel('linkedin_dataset (1).xlsx')
job1_df[['Job Title','Job Description']] = job1_df[[ 'Job Title','Job Description']].fillna('')
profiles_df[['profile', 'work experience']] = profiles_df[['profile','work experience']].fillna('')

def remove_punctuation(text):
  punctuationfree = "".join([i for i in text if i not in string.punctuation])
  return punctuationfree

def tokenization(text):
    tokens = re.split('W+',text)
    return tokens

#defining the function to remove stopwords from tokenized text
def remove_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output

#defining the function for lemmatization
def lemmatizer(text):
  lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
  return lemm_text

def removelowernpunc():
    #storing the puntuation free text
    job1_df['Job Title'] = job1_df['Job Title'].apply(lambda x:remove_punctuation(x))
    job1_df['Job Description'] = job1_df['Job Description'].apply(lambda x:remove_punctuation(x))
    profiles_df['profile'] = profiles_df['profile'].apply(lambda x:remove_punctuation(x))
    profiles_df['work experience'] = profiles_df['work experience'].apply(lambda x:remove_punctuation(x))

    #lower case 
    job1_df['Job Title']= job1_df['Job Title'].apply(lambda x: x.lower())
    job1_df['Job Description']= job1_df['Job Description'].apply(lambda x: x.lower())
    profiles_df['profile']= profiles_df['profile'].apply(lambda x: x.lower())
    profiles_df['work experience']= profiles_df['work experience'].apply(lambda x: x.lower())

    #applying function to the column
    job1_df['Job Title']= job1_df['Job Title'].apply(lambda x: tokenization(x))
    job1_df['Job Description']= job1_df['Job Description'].apply(lambda x: tokenization(x))
    profiles_df['profile']= profiles_df['profile'].apply(lambda x: tokenization(x))
    profiles_df['work experience']= profiles_df['work experience'].apply(lambda x: tokenization(x))

    #applying the function
    job1_df['Job Title']= job1_df['Job Title'].apply(lambda x:remove_stopwords(x))
    job1_df['Job Description']= job1_df['Job Description'].apply(lambda x:remove_stopwords(x))
    profiles_df['profile']= profiles_df['profile'].apply(lambda x:remove_stopwords(x))
    profiles_df['work experience']= profiles_df['work experience'].apply(lambda x:remove_stopwords(x))

    job1_df['Job Title']=job1_df['Job Title'].apply(lambda x:lemmatizer(x))
    job1_df['Job Description']=job1_df['Job Description'].apply(lambda x:lemmatizer(x))
    profiles_df['profile']=profiles_df['profile'].apply(lambda x:lemmatizer(x))
    profiles_df['work experience']=profiles_df['work experience'].apply(lambda x:lemmatizer(x))

def searchpeople(key):   
    df = pd.DataFrame(columns=['Name','Link','Percentage'])
    if(key=='java developer'): n=0
    elif(key=='backend developer'): n=1
    elif(key=='web developer'): n=2
    elif(key=='python developer'): n=3
    elif(key=='data scientist'): n=4
    elif(key=='full stack developer'): n=5
    elif(key=='ui developer'): n=6
    elif(key=='senior devops engineer'): n=7
    elif(key=='cyber security'): n=8

    for i in range (0,len(profiles_df)):
        string1=job1_df.iloc[n]["Job Description"]
        string2=profiles_df.iloc[i]["profile"]
        value=fuzz.ratio(string1,string2)
        if(value>40):
            df.loc[len(df.index)] = [profiles_df.iloc[i]["name"],profiles_df.iloc[i]["url"],value]
    
    return df.sort_values(by='Percentage',ascending=False)

st.set_page_config(page_title='BitByBit',
                   page_icon=None, 
                   layout="centered", 
                   initial_sidebar_state="auto"
    )

with st.sidebar:
    st.header('     Jobs Recruitment')
    my_page = option_menu("", ['Java Developer','Backend Developer', 'Web Developer','Python Developer','Data Scientist','Full Stack Developer','UI Developer','Senior DevOps Engineer','Cyber Security'], 
        menu_icon="cast", default_index=1,
        styles={
        "container": {"padding": "5!important"},
        "icon": {"font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
    })

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/flat-lay-workstation-with-copy-space-laptop_23-2148430879.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
if my_page == 'Java Developer':
    st.title('Java Developer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.dataframe(searchpeople('java developer'))

elif my_page == 'Backend Developer':
    st.title('Backend Developer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.write(searchpeople('backend developer'))

elif my_page == 'Full Stack Developer':
    st.title('Full Stack Developer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.write(searchpeople('full stack developer'))

elif my_page == 'Web Developer':
    st.title('Web Developer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.write(searchpeople('web developer')) 
        
elif my_page == 'Python Developer':
    st.title('Python Developer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search Here')
    if button:
        st.write(searchpeople('python developer'))   

elif my_page == 'Data Scientist':
    st.title('Data Scientist')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.write(searchpeople('data scientist')) 

elif my_page == 'UI Developer':
    st.title('UI Developer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.write(searchpeople('ui developer'))   

elif my_page == 'Senior DevOps Engineer':
    st.title('Senior DevOps Engineer')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    
    if button:
        st.write(searchpeople('senior devops engineer'))

elif my_page == 'Cyber Security':
    st.title('Cyber Security')
    st.write(
    """ Let's hire the best people for this job...."""
)
    #st.markdown(page_bg_img,unsafe_allow_html=True)
    button = st.button('Search here')
    if button:
        st.write(searchpeople('cyber security'))

else:
    st.title('this is a different page')
    slide = st.slider('this is a slider')
    slide