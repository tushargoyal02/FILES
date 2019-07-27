# Deep Learning for Data Science

*   The more nodes we have in hidden layer the more good the model will be.
*   Hidden Layer mean the layer not visible to outside world, but consist of all dependcies of input layer.


### Forward Propagation

*   There is a  multiply add process
*   Dot Product

Example

    import numpy as np

    input_data = np.array([2,3])

    weights= {'node0': np.array([1, 1]),
                'node1': np.array([-1,1]),
                'output1': np.array([2, -1])}

    # here node 0 work as hidden layer  
    node_0_value = (input_data * weights['node0']).sum()

    node1_value =   (input_data * weights['node1].sum())



    #hidden layer 
    hidden_layer = np.array([node_0_value, node_1_value])

    output = (hidden_layer * weights['output']).sum()


*   Activation Functions: These are required to capture linearity and non linearity 

    *   This is applied to input node to produce output

    
*   RELU : Rectified Linear Activation
    *   This function takes a single number as an input, returning 0 if the input is negative, and the input if the input is positive.    

            node_0_output = np.tanh(node_0_input)

            # this calculate the relu     
            relu(node_0_output)





*   Create model with sequential

        model = Sequential()

        #add hidden layer
        model.add(Dense(100, activation'relu', input_shape=input_shape))


* Low value for loss function is good.


*   Keras alllow to give or set validation data

        model.fit(predictors, target, validation_split=0.3)



### EarlyStopping

    from keras.callbacks import EarlyStopping

    # patience is how many time it will see before stopping
    early_stopping_monitor = EarlyStopping(patience=2)

    model.fit(... , callbacks=[early_stopping_monitor])


*   Overfitting and underfitting:

    *   Overfitting does work well with Training data but not with Test data
    *   Underfitting doesnt work well with anyone.
    





        


