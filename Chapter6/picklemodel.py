import pickle
from classdef import AthleteList

def get_data(source):
    try:
        with open(source, 'r') as file:
            data= file.readline()
        temp= data.strip().split(',')
        return(AthleteList(temp.pop(0),temp.pop(0),temp))
               
    except IOError as ioerr:
        print('file error'+ str(ioerr))
        return None

def put_to_store(file_list):
    all_athletes={}
    for each_file in file_list:
        data= get_data(each_file)
        all_athletes[data.name]= data
    try:
        with open('pickle_athlete.txt', 'wb') as pickle_data:
            pickle.dump(all_athletes, pickle_data)
    except IOError as ioerr:
        print('error' +str(ioerr))
    return all_athlete

def get_from_store():
    all_athletes={}
    try:
        with open('pickle_athlete.txt','rb') as unpickle:
            all_athletes= pickle.load(unpickle)
        return all_athletes
    except IOError as ioerr:
        print(str(ioerr))
        return all_athletes
        
