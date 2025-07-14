import numpy as np 
import pandas as pd

def main():
    dataset = pd.read_csv("studentsData.csv")
    
    print("Columns:", ", ".join(dataset.columns))
    print("\nFull data:\n", dataset)
    
    print("\nData summary:")
    print(dataset.describe())
    
    print("\nNumber of students per class:")
    print(dataset['class'].value_counts())
    
    print("\nAverage marks per class:")
    print(dataset.groupby('class')['mark'].mean())

if __name__ == "__main__":
    main()
