import pandas as pd

def drop_duplicate(dataframe):
    if dataframe.duplicated().sum() >=1:
        print(dataframe[dataframe.duplicated])
        ask = input("Do you want to drop duplicates? (Y/N) ")
        if ask.lower() == "y":
            dataframe.drop_duplicates(inplace=True)
            return "Duplicates dropped"
        else:
            return "Duplicates not dropped"
    else:
        return "NO Duplicates found"
    
def whitespace_remover(dataframe):
    for i in dataframe.columns:
        if dataframe[i].dtype == 'object':
            dataframe[i] = dataframe[i].apply(lambda x: x.strip())
    return dataframe