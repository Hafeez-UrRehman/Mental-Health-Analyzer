

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/SHAN/Hafeez/trained_model.sav', 'rb'))

def Ment_Pred(input_data):
    
    inputdataToNPArray = np.asarray(input_data)
    inputdataToNPArrayReshape = inputdataToNPArray.reshape(1,-1)
    predic = loaded_model.predict(inputdataToNPArrayReshape)
    print(predic)
    

    if (predic[0] == 0):
        print("The person is suffering from Anxiety ")
    elif (predic[0] == 1):
      print("The person is suffering from Depression ")
    elif (predic[0] == 2):
      print("The person is  suffering from Loneliness ")
    elif (predic[0] == 3):
      print("The person is suffering from Stress ")
    else:
        print("The person is Normal" )
        
 
    
def main():
    st.title("Mental Health Prediction System")
    
    feeling_nervous = st.text_input('Feeling Nervous or Not')
    panic = st.text_input('Panicking or Not')
    breathing_rapidly = st.text_input ('breathing.rapidly or Not')
    sweating = st.text_input ('sweating or Not')
    trouble_in_concentration = st.text_input('trouble.in.concentration or Not')
    having_trouble_in_sleeping  = st.text_input('having.trouble.in.sleeping or Not')
    having_trouble_with_work = st.text_input('having.trouble.with.work or Not')
    hopelessness = st.text_input('Feeling hopelessness or Not')
    anger = st.text_input('anger or Not')
    over_react = st.text_input('over.reacting or Not')
    change_in_eating = st.text_input('change.in.eating or Not')
    suicidal_thought = st.text_input('suicidal.thought or Not')
    feeling_tired = st.text_input('feeling.tired or Not')
    close_friend = st.text_input('Have close.friend or Not')
    social_media_addiction = st.text_input('social.media.addiction or Not')
    weight_gain = st.text_input('weight.gaining or Not')
    material_possessions = st.text_input('material.possessions or Not')
    introvert = st.text_input('Are you introvert or Not')
    popping_up_stressful_memory = st.text_input('popping.up.stressful.memory or Not')
    having_nightmares = st.text_input('having.nightmares or Not')
    avoids_people_or_activities = st.text_input('avoids.people.or.activities or Not')
    feeling_negative = st.text_input('feeling.negative or Not')
    trouble_concentrating = st.text_input('trouble.concentrating or Not')
    blamming_yourself = st.text_input('blamming.yourself for everything or Not')

    
    diagnosis = ''
    
    
    if st.button ('Mental Health Test Result'): 
        
        diagnosis = Ment_Pred ([feeling_nervous, panic, breathing_rapidly, sweating, trouble_in_concentration, having_trouble_in_sleeping, having_trouble_with_work, hopelessness, anger, over_react, change_in_eating, suicidal_thought, feeling_tired, close_friend, social_media_addiction, weight_gain, material_possessions, introvert, popping_up_stressful_memory, having_nightmares, avoids_people_or_activities, feeling_negative, trouble_concentrating, blamming_yourself])
        
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
        


