import cache_api
import json
#API="put youy api"
def get_movie_data(name):
    baseurl = "http://www.omdbapi.com"
    params={ 't':name, 'r':'json','apikey':API}
    movies_inf = cache_api.get(baseurl,params=params,temp_cache_file="Movies_cache.txt")
    movies_inf = json.loads(movies_inf)
    return movies_inf
def get_movie_rating(movies_lst):
    movies_dic = {}
    for movie in movies_lst:
        movie_inf = get_movie_data(movie)
        ratings_lst = movie_inf['Ratings']
        for rating in ratings_lst:
            if rating['Source']=='Rotten Tomatoes':
                movies_dic[movie] = int(rating['Value'][:-1])
    return movies_dic
