# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  numpy as np
import pickle 

loaded_model = pickle.load(open('C:/Users\SHAN/hafeez project/trained_model.sav', 'rb'))

input_data = (1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1)

inputdataToNPArray = np.asarray(input_data)
inputdataToNPArrayReshape = inputdataToNPArray.reshape(1,-1)
predic = loaded_model.predict(inputdataToNPArrayReshape)
print(predic)

if (predic[0] == 0):
    print("The person is suffering from Anxiety ")
elif (predic[0] == 1):
  print("The person is suffering from Depression ")
elif (predic[0] == 1):
  print("The person is  suffering from Loneliness ")
elif (predic[0] == 1):
  print("The person is suffering from Stress ")
else:
    print("The person is Normal" )



