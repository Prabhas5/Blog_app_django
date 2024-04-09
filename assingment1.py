'''Assignment 1: Data Manipulation and Analysis

Problem Statement: You are given a CSV file data.csv containing data about customers, 
including their names, ages, and email addresses. Write a Python script to read the data from the CSV file,
calculate the average age of the customers, and find the most common domain name in the email addresses.'''

#Solutions
import pandas as pd

def calculate_avg(df):

    avg=df["age"].mean()
    #rounding the value of float

    return round(avg,3)
def most_common_domain(df):
    #adding new column by extacting email

    df["domain"]=df["email"].str.split("@").str[-1]
    #counting the domains

    domain_counts = df['domain'].value_counts()
    #counting the most count

    most_common_domain = domain_counts.idxmax()
    return most_common_domain

    
#reading csv file  from input  
df=pd.read_csv("data.csv")
#calling avg funtion

avg=calculate_avg(df=df)
#calling most count funtion

most_count=most_common_domain(df=df)

print(f'Average Age : {avg}',f'Most Common Domain: {most_count}',sep="\n")




