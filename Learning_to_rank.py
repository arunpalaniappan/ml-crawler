import numpy as np
from keras.layers import Activation, Dense, Input, Subtract
from keras.models import Model

def RankNet(input_shape):

    hidden_layer1 = Dense(4, activation="relu")
    hidden_layer2 = Dense(2, activation='relu')
    hidden_layer3 = Dense(1, activation='linear')
  
    input_1 = Input(shape=(input_shape,))
    x_1 = hidden_layer1(input_1)
    x_1 = hidden_layer2(x_1)
    x_1 = hidden_layer3(x_1)
  
    input_2 = Input(shape=(input_shape,))
    x_2 = hidden_layer1(input_2)
    x_2 = hidden_layer2(x_2)
    x_2 = hidden_layer3(x_2)
  
    subtracted_results = Subtract(name='Subtract_layer')([x_1, x_2])
    
    output = Activation('sigmoid', name='Activation_layer')(subtracted_results)
    
    model = Model(inputs=[input_1, input_2], outputs=output)

    return model

def Model_creation(padded_docs,paired_docs,target):

    INPUT_DIM = len(padded_docs[1])
    Y = target
    
    model = RankNet(INPUT_DIM)
    model.compile(optimizer="adam", loss="binary_crossentropy")
    
    model.fit(([padded_docs, paired_docs]), np.array(Y), batch_size=10, epochs=25, verbose=1)
    
    results = model.predict([padded_docs,paired_docs])
    
    return results