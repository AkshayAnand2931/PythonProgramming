"""
    Assume input tensor is of the form:
    tensor = [outlook,temp,humidity,windy,play]
    here play is the target variable (class)
    remaining four are explanatory variables

"""
import torch

"""Calculate the entropy of the entire dataset"""
# input:tensor
# output:int/float
def get_entropy_of_dataset(tensor:torch.Tensor):

    if(tensor.dim() == 1):
        play = tensor[:]
    else:
        play = tensor[:,-1]

    play = [o.item() for o in play]
    unique = list(set(play))
    no_of_classes = len(unique)
    probability = [0] * no_of_classes

    for i in play:
        probability[unique.index(i)] += 1

    total = sum(probability)
    probability = [ (prob/total) for prob in probability]

    entropy = 0
    for prob in probability:
        if prob != 0:
            entropy = entropy - (prob * torch.log2(torch.tensor(prob)))
    return entropy


"""Return avg_info of the attribute provided as parameter"""
# input:tensor,attribute number 
# output:int/float
def get_avg_info_of_attribute(tensor:torch.Tensor, attribute:int):
    
    attr = tensor[:,attribute]
    attr = [o.item() for o in attr]

    outcomes = list(set(attr))
    
    no_of_classes = len(outcomes)
    probability = [0] * no_of_classes


    for i in attr:
        probability[outcomes.index(i)] += 1

    total = sum(probability)
    probability = [(prob/total) for prob in probability]    

    tensor_Array = [[] for i in range (0,no_of_classes)]

    for i in range(0,len(attr)):

        element = tensor[:,-1][i].item()
        list1 = tensor_Array[outcomes.index(attr[i])]
        list1.append(element)
    
    tensor_Array = [torch.tensor(list) for list in tensor_Array]
    avg_info = 0

    for i in range(0,no_of_classes):
        avg_info += probability[i] * get_entropy_of_dataset(tensor_Array[i])

    return avg_info


"""Return Information Gain of the attribute provided as parameter"""
# input:tensor,attribute number
# output:int/float
def get_information_gain(tensor:torch.Tensor, attribute:int):

    return get_entropy_of_dataset(tensor) - get_avg_info_of_attribute(tensor,attribute)


# input: tensor
# output: ({dict},int)
def get_selected_attribute(tensor:torch.Tensor):
    """
    Return a tuple with the first element as a dictionary which has IG of all columns
    and the second element as an integer representing attribute number of selected attribute

    example : ({0: 0.123, 1: 0.768, 2: 1.23} , 2)
    """
    no_of_attr = len(tensor[0]) - 1
    attr_dict = {}

    for i in range(0,no_of_attr):
        attr_dict[i] = get_information_gain(tensor,i)
    
    maximum = max(attr_dict.values())
    max_index = [key for key,value in attr_dict.items() if value == maximum]

    return (attr_dict,max_index[0])