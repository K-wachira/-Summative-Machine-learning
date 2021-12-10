import numpy as np
from keras.models import load_model
import h5py
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from PIL import Image
import cleanData as cleaner
import auto_twitter as twter
#app=Flask(__name__)
#Swagger(app)

pickle_in = open("Model.h5","rb")
prd_model = load_model("Model.h5")

#@app.route('/')
def welcome():
    return "Sentiment Analysis"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(tweet_array):
    prediction=prd_model.predict([tweet_array])
    print(prediction)
    return prediction




def autotweets():
    genre = st.radio(
        "What's your favorite movie genre",
        ('Ruto', 'Uhuru', 'Raila'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn't select comedy.")
    s=twter.getTweets(search_words, date_since) 


def main():
    st.title("Twitter Sentiment Analysis")
    html_temp = """
    <div style="background-color:#033923;padding:10px">
    <h2 style="color:white;text-align:center;">Machine learning class project app </h2>
    <p>  </p>
    </div>
    """


    st.markdown(html_temp,unsafe_allow_html=True)
    tweet = st.text_area('Copy and Paste a Kenyan political tweet to Analyze', 
    '''eg Ruto thinks that, the votes that Uhuru Kenyatta got in Murang'a County in 2013 and 2017 is because of him. Laughable though.
    ''', 
    max_chars = 280)


    search_words = "Ruto"
    date_since = "2019-12-1"


    if tweet.strip() == "" or len(tweet.strip()) < 20:
        st.warning("Invalid input, please put in a valid tweet")
        return

    if st.button('Auto predict'):
        st.write('hello there')
        genre = st.selectbox(
        "What polititian do u want to veiw the tweet",
        ['Ruto', 'Uhuru', 'Raila'], index=1, 
         )

        if genre == 'Ruto':
            search_words = "Ruto"
            st.write('You selected Ruto.')
        elif genre == 'Uhuru':
            search_words = "Uhuru"
            st.write('You selected Uhuru.')
        elif genre == 'Raila':
            search_words = "Raila"
            st.write('You selected Raila.')
        else:
            st.write("You didn't select comedy.")
        
    if st.button('Continue ? '):
        tweet=twter.getTweets(search_words, date_since)
        st.write("The Fetched tweet is:", tweet)

       
        
    tweet_array = cleaner.loadTweet(tweet)
    print(tweet_array)
    
    st.success("Tweet in question: {}".format( tweet))

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(tweet_array)
        if (result).astype("int32"):
            result = "positive sentiment"
        else:
            result = "negative sentiment"
    st.success('The this tweet has a {}'.format(result))
    if st.button("By: "):
        st.text("Kelvin ")
        st.text("Machine learning project")






if __name__=='__main__':
    main()

# small change