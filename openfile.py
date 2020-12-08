import pandas as pd
import numpy as np 

class my_dictionary:
    def __init__(self, file_path):
        self.df = self.open_file(file_path)
        self.file_headers = self.df.columns.to_list()
        self.list_of_lists = self.create_nested_list()

    # Function to add key:value
    def open_file(self, file_path):
        file_data = None
        try:
            file_data = pd.read_csv(file_path, delimiter=',')
        except Exception as e:
            print(e)
        else: 
            file_data.fillna(value = 0, inplace = True)
        return file_data

    def create_nested_list(self):
        """Created list of lists with all rows 
            of csv including headers
        """
        rows_lists = list()
        for row in self.df.values:
            rows_lists.append(list(row))
        return rows_lists

    def create_list_of_dict (self):
        myList = list()
        for values in self.list_of_lists:
            myList.append(dict(zip(self.file_headers[1:], values[1:])))
        return myList

    def modify_dict_value(self, dict_list): 
        for dictionary in dict_list:
            if (dictionary['overall']== None):
                return dictionary


def main():
    file_path = input("Enter direct path of your file: ")
    myobj = my_dictionary(file_path)
    myList = myobj.create_list_of_dict()
    return myList