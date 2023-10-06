import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Dataset Preparation
def prepareData(classes_list,class_dict):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    # Classes to include
    
    class_indices_to_keep = [0,1,2]

    # Training Dataset
    train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, transform=transform, download=True)
    for i in range(len(train_dataset)):
        if(train_dataset.targets[i] in classes_list):
            train_dataset.targets[i] = class_dict[train_dataset.targets[i]]
        else:
            train_dataset.targets[i] = -1
    train_dataset = torch.utils.data.Subset(train_dataset, [i for i in range(len(train_dataset)) if train_dataset.targets[i] in class_indices_to_keep])
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)

    # Testing Dataset
    test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=transform, download=True)
    for i in range(len(test_dataset)):
        if(test_dataset.targets[i] in classes_list):
            test_dataset.targets[i] = class_dict[test_dataset.targets[i]]
        else:
            test_dataset.targets[i] = -1
    test_dataset = torch.utils.data.Subset(test_dataset, [i for i in range(len(test_dataset)) if test_dataset.targets[i] in class_indices_to_keep])
    test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)
    return train_loader,test_loader

# The CNN Model Class
class CNN(nn.Module):

    # Define Initialization function
    def __init__(self):
        super().__init__()
        self.optimizer = None 
        self.criterion = None 

        # ----------------------------------------------
        self.conv1 = nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3)
        self.conv2 = nn.Conv2d(in_channels=64,out_channels=64,kernel_size=3)
        self.conv3 = nn.Conv2d(in_channels=64,out_channels=32,kernel_size=3)

        self.max_pool1 = nn.MaxPool2d(kernel_size=2,stride=1)
        self.max_pool2 = nn.MaxPool2d(kernel_size=2,stride=2)
        self.avg_pool = nn.AvgPool2d(kernel_size=2,stride=1)

        self.relu = nn.ReLU()
        self.linear = nn.Linear(3200,64)
        # ----------------------------------------------
        self.setCriterionAndOptimizer() # Do not Delete

    # Define Forward Pass
    def forward(self, x):

        output = self.conv1(x)
        output = self.max_pool1(output)

        output = self.conv2(output)
        output = self.max_pool2(output)

        output = self.conv3(output)
        output = self.avg_pool(output)

        output = output.reshape(output.size(0),-1)

        output = self.linear(output)
        output = self.relu(output)

        return output
        

    # Set Values of self.optimizer and self.criterion
    def setCriterionAndOptimizer(self):
        self.optimizer = optim.Adam(self.parameters(), lr=0.002)
        self.criterion = nn.CrossEntropyLoss()

# Implement training loop here
# Input: 1) model: CNN object
# Output: 1) train_accuracy: float
# You are supposed to use the train_loader DataLoader object for training
def train(model,train_loader):

    accuracy = 0
    while accuracy < 80:

        correct_predictions = 0
        for inputs,labels in train_loader:

            outputs = model(inputs)
            loss = model.criterion(outputs,labels)

            _, predicted = torch.max(outputs,1)
            correct_predictions += (predicted == labels).sum().item()

            model.optimizer.zero_grad()
            loss.backward()
            model.optimizer.step()

        accuracy = 100.0 * correct_predictions / labels.size(0)

    return accuracy


# Implement evaluation here
# Input: 1) model: CNN object
# Output: 1) test_accuracy: float
def evaluate(model,test_loader):

    running_loss = 0.0
    correct_predictions = 0
    total_samples = 0
    criterion = model.criterion

    with torch.no_grad():
        for inputs, labels in test_loader:
            
            # Forward pass
            outputs = model(inputs)
            
            # Calculate loss
            loss = criterion(outputs, labels)
            
            # Update statistics
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct_predictions += (predicted == labels).sum().item()
            total_samples += labels.size(0)
    
    # Calculate validation/test loss and accuracy
    test_loss = running_loss / len(test_loader)
    test_accuracy = 100.0 * correct_predictions / total_samples
    
    print(f'Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.2f}%')
    
    return test_accuracy 