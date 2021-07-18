import os
from pandas import read_csv

train_path = os.path.join("Data", "train.csv")
test_path = os.path.join("Data", "test.csv")
sub_path = os.path.join("Data", "sample_submission.csv")

def get_train():
    train = read_csv(train_path)
    return(train)

def get_test():
    test = read_csv(test_path)
    return(test)

def get_cat(dataframe):
    
    '''
    returns categorical features
    '''
    
    categorical = dataframe.loc[:, dataframe.columns.str.\
        startswith("cat")]
    
    return(categorical)

def get_cont(dataframe):
    
    '''
    returns continuous features
    '''
    
    continuous = dataframe.loc[:, dataframe.columns.str.\
        startswith("cont")]
    
    return(continuous)

def get_sub():
    sub = read_csv(sub_path)
    return(sub)