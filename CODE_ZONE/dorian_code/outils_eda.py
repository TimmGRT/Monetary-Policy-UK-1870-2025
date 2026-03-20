import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def histogram(df, column: str):
    try:
        df.hist(bins = 20, column = column)
        plt.ticklabel_format(style='plain', axis='x')
        plt.show()
    except : 
        print("Attention de travailler uniquement sur le fichier main_cleaned.parquet")

def time_evo (df,column: str):
    try:
        plt.plot(df['year'], df[column])
        plt.ticklabel_format(style='plain', axis='y')
        plt.show()
    except :
        print("Attention de travailler uniquement sur le fichier main_cleaned.parquet")
    
if __name__ == "__main__":
    print("Vous êtes bien dans le fichier outils_eda")