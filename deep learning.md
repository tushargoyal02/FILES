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

    node_0_value = (input_data * weights['node0']).sum()

    node1_value =   (input_data * weights['node1].sum())