"""Assignment 4: Web Scraping and Data Analysis

Problem Statement: Write a Python script to scrape data from a website (e.g., IMDb) to retrieve information about 
20 top-rated movies. Extract the movie title, year of release and IMDb rating for each movie, 
and store this information in a CSV file. Perform data analysis to find the average rating of the top-rated movies.


Input: https://www.imdb.com/chart/top/

Output: A CSV file top_movies.csv containing information about the top-rated movies."""

#Solution
import pandas as pd
import requests
from bs4 import BeautifulSoup

def response(url,header):
    #Making get request
    resp=requests.get(url=url,headers=header)
    #Returning response object
    return resp

def write_to_file(soup_objet,file_name):
    #Converting to str
    str_soup=soup_objet.prettify()

    with open(file_name,"w",encoding="utf-8") as file_handle:
        file_handle.write(str_soup)
        return True
    
def scract_movie_data(soup):
    movies = []
    for movie in soup.find_all('div', class_='ipc-metadata-list-summary-item__tc')[:20]:
        title = movie.h3.get_text(strip=True)
        year = movie.find("span",class_="sc-b0691f29-8 ilsLEX cli-title-metadata-item").text
        rating = movie.find("span",class_="ipc-rating-star--imdb").get_text(strip=True)[:3]
        movies.append({'Movies_Title': title, 'Released_Year': int(year), 'Rating': float(rating)})
    return movies

header={"User-Agent": "Mozilla/5.0"}
url='https://www.imdb.com/chart/top'
file_name="Imdb_top_move.html"
resp=response(url,header)
def main():
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,"html.parser")
        #Writing the file locally
        temp=write_to_file(soup,file_name)
        if temp:
            with open(file_name,"r",encoding='utf-8') as file:
                data=file.read()
                #Making soup object
                _soup=BeautifulSoup(data,"html.parser")
                #Invoking funtion to fecth data from locally created file
                movies_data=scract_movie_data(soup)
                #Making data frame from dict object
                df=pd.DataFrame.from_dict(movies_data)
                #writing the data frame to csv file 
                df.to_csv("top_movies.csv",index=False,mode="w",sep="\t")
                return True          
        else:
            print("Some Error occured while creating the file")
            return False
if __name__=="__main__":
    if main():
        print("Success !!")
    else:
        print("Error!!")

