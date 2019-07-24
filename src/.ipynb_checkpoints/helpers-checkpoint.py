import pandas as pd
import numpy as np

def legend(df,col):
    """
    Creates a new dataframe where the index is the passed column 'col' and 
    the first column is a sequential integer
    ------------------
    Input
    df = DataFrame
    col = String
    ------------------
    Output
    DataFrame
    
    """
    cols = list(df.columns)
    cols.remove(col)
    newdf = df.groupby(col).count().reset_index()
    newdf = newdf.drop(cols,axis=1)
    newdf = newdf.reset_index()
    newdf.index = newdf[col]
    newdf.drop(col,axis=1,inplace=True)
    newdf.columns = ['id']
    return newdf

def to_int(df,u):
    """
    Searches the df and returns the associated Id for the given index
    -------------------
    Input
    df = DataFrame
    u = String
    -------------------
    Output
    Integer
    
    """
    return df.at[u,'id']


def create_legend(df,col):
    """
    Creates a new dataframe where the index is the passed column 'col' and 
    the first column is a sequential integer
    ------------------
    Input
    df = DataFrame
    col = String
    ------------------
    Output
    DataFrame
    
    """
    cols = list(df.columns)
    cols.remove(col)
    newdf = df.groupby(col).count().reset_index()
    newdf = newdf.drop(cols,axis=1)
    newdf = newdf.reset_index()
    newdf.drop('index',axis=1,inplace=True)
    newdf.columns = ['id']
    return newdf
