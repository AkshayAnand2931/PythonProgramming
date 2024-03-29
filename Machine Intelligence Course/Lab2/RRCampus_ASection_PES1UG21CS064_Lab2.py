import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score,confusion_matrix


# Split the data into training and testing sets
# input: 1) x: list/ndarray (features)
#        2) y: list/ndarray (target)
# output: split: tuple of X_train, X_test, y_train, y_test
def split_and_standardize(X,y):
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return (X_train,X_test,y_train,y_test)




# Create and train 2 MLP classifier(of 3 hidden layers each) with different parameters
# input:  1) X_train: list/ndarray
#         2) y_train: list/ndarray

# output: 1) models: model1,model2 - tuple
def create_model(X_train,y_train):
    
    model1 = MLPClassifier(hidden_layer_sizes=(10,10,10),activation='relu',solver="adam",learning_rate_init=0.001)
    model2 = MLPClassifier(hidden_layer_sizes=(5,10,5),activation='tanh',solver='sgd',learning_rate_init=0.1,max_iter=5)

    model1.fit(X_train,y_train)
    model2.fit(X_train,y_train)

    return (model1 ,model2)




# create model with parameters
# input  : 1) model: MLPClassifier after training
#          2) X_train: list/ndarray
#          3) y_train: list/ndarray
# output : 1) metrics: tuple - accuracy,precision,recall,fscore,confusion matrix
def predict_and_evaluate(model,X_test,y_test):
    
    predicted_values = model.predict(X_test)

    accuracy = accuracy_score(y_test,predicted_values)
    precision = precision_score(y_test,predicted_values,average="micro")
    recall = recall_score(y_test,predicted_values,average="micro")
    f1score = f1_score(y_test,predicted_values,average='micro')
    confusion = confusion_matrix(y_test,predicted_values)
    #print(accuracy,precision,recall,f1score,confusion)
    return(accuracy,precision,recall,f1score,confusion)