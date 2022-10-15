import requests
from bs4 import BeautifulSoup
import pandas as pd

topics_url = 'https://www.imdb.com/search/title/?title_type=top-rated&year=1980,2022&sort=moviemeter,asc'
response = requests.get(topics_url)

doc = BeautifulSoup(response.text, 'html.parser')
doc.find('title')

def get_movie_titles(doc):
    
    selection_class="lister-item-header"
    movie_title_tags=doc.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
        
        
    return movie_titles

titles = get_movie_titles(doc)

def get_movie_year(doc):
    year_selector = "lister-item-year text-muted unbold"           
    movie_year_tags=doc.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    return movie_year_tagss


years = get_movie_year(doc)

def get_movie_runtime(doc):
    url_selector="lister list detail sub-list"           
    movie_runtime_tags=doc.find_all('h3',{'class':url_selector})
    movie_url_tagss=[]
    base_url = 'https://www.imdb.com/search/title/?year=1980-01-01,2022-12-31&sort=runtime,asc'
    for tag in movie_runtime_tags:
        movie_url_tagss.append('https://www.imdb.com/search/title/?year=1980-01-01,2022-12-31&sort=runtime,asc' + tag.find('a')['href'])
    return movie_url_tagss

urls = get_movie_runtime(doc)

def get_movie_rating(doc):
    rating_selector="inline-block ratings-imdb-rating"            
    movie_rating_tags=doc.find_all('div',{'class':rating_selector})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    return movie_rating_tagss

ratings = get_movie_rating(doc)

def get_movie_duration(doc):
    
    selection_class="runtime"
    movie_duration_tags=doc.find_all('span',{'class':selection_class})
    movie_duration=[]

    for tag in movie_duration_tags:
        duration = tag.text[:-4]
        movie_duration.append(duration)
        
        
    return movie_duration

durations = get_movie_duration(doc)

def get_movie_votes(doc):
    
    selection_class="text-muted"
    movie_votes_tags=doc.find_all('span',{'class':selection_class})
    movie_votes=[]

    for tag in movie_votes_tags:
        votes = tag.find('span')
        movie_votes.append(votes)
        
        
    return movie_votes

titles = get_movie_votes(doc)

def get_movie_metascore(doc):
    
    selection_class="metascore"
    movie_votes_metascore=doc.find_all('span',{'class':selection_class})
    movie_metacore=[]

    for tag in movie_votes_metascore:
        votes = tag.find('span')
        movie_metacore.append(votes)
        
        
    return movie_metacore

titles = get_movie_metascore(doc)


def get_movie_description(doc):
    
    selection_class="text-muted"
    movie_description_tag=doc.find_all('p',{'class':selection_class})
    movie_description=[]

    for tag in movie_description_tag:
        votes = tag.find('p')
        movie_description.append(votes)
        
        
    return movie_description

titles = get_movie_description(doc)


def all_pages():
    movies_dict={
        'title':[],
        'votes':[],
        'duration':[],
        'rating':[],
        'year':[],
        'metascore':[],
        'runtime':[],
        'description':[]
    }

    for i in range(1,2000,100):
       
        try:
            url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start='+str(i)+'&ref_=adv_next'
            response = requests.get(url)
        except:
            break
        
        if response.status_code != 200:
            break
           
    # Parse using BeautifulSoup
        doc = BeautifulSoup(response.text, 'html.parser')
        titles = get_movie_titles(doc)
        runtime = get_movie_runtime(doc)
        votes=get_movie_votes(doc)
        ratings = get_movie_rating(doc)
        durations = get_movie_duration(doc)
        years = get_movie_year(doc)
        metascore = get_movie_metascore(doc)
        description = get_movie_description(doc)
    
        
    # We are adding every movie data to dictionary
        for i in range(len(titles)):
            movies_dict['title'].append(titles[i])
            movies_dict['votes'].append(votes[i])
            movies_dict['duration'].append(durations[i])
            movies_dict['rating'].append(ratings[i])
            movies_dict['year'].append(years[i])
            movies_dict['metascore'].append(metascore[i])
            movies_dict['runtime'].append(runtime[i])
            movies_dict['description'].append(description[i])
        
    return pd.DataFrame(movies_dict)



movies = all_pages()
movies.to_csv('movies.csv',index=None)