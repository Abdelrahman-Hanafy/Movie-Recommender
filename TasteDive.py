import cache_api
import json

API = 'put your api'
def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    params={'q':name, "limit":5,'type':'movies','K':API}
    movies_dic = cache_api.get(baseurl, params=params,temp_cache_file="Movies_cache.txt")
    movies_dic = json.loads(movies_dic)
    return movies_dic

def extract_movie_titles(movies_dic):
    titles = [d["Name"] for d in movies_dic['Similar']['Results']]
    return titles

def get_related_titles(movies_lst):
    related=[]
    for movie in movies_lst:
        titles=extract_movie_titles(get_movies_from_tastedive(movie))
        #related = [title for title in titles if title not in related]
        for title in titles:
            if title in related : continue
            else: related.append(title)
    return related
