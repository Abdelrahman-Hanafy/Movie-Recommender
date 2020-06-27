import cache_api, json,TasteDive, OMDB
import sqlite3

conn = sqlite3.connect('Moviesdb.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Movies (Movie TEXT, rating INTEGER)''')
cur.execute('''
CREATE TABLE IF NOT EXISTS recommendations (Movie TEXT, recommendations TEXT)''')

'''------------------------------------------------------------------------------------------------------------------------'''

def get_sorted_recommendations(movies_lst):
    related_lst = TasteDive.get_related_titles(movies_lst)
    ratings_dis = OMDB.get_movie_rating(related_lst)
    sorted_rec  = sorted(ratings_dis.keys(), key=lambda rate:ratings_dis[rate]  ,  reverse = True)
    for Movie in sorted_rec:
        cur.execute('SELECT Movie FROM Movies WHERE Movie=?', (Movie,) )
        if cur.fetchone() is None:
            cur.execute('''INSERT INTO Movies (Movie, rating)
                VALUES (?, ?)''', (Movie,ratings_dis[Movie]))
        cur.execute('SELECT Movie FROM recommendations WHERE Movie=?', (str(movies_lst),) )
        if cur.fetchone() is None:
            cur.execute('''INSERT INTO recommendations (Movie, recommendations)
                VALUES (?, ?)''', (str(movies_lst),str(sorted_rec)))

    return sorted_rec

''' --------------------------------------------------------------------------------------------------------------------------------'''

x = True
while x :
    lst=[]
    Movie = input("\nEnter a movie name : ")
    if len(Movie) < 1:
        print("\n Erorr Inpit")
        continue
    lst.append(Movie)
    recommendations = get_sorted_recommendations(lst)
    if len(recommendations) == 0:
        print("\nWrong movie name Entered")
    else : print("\n",recommendations)
    x = input("\nDo you want to ask again (y/n) : ")
    if x == 'y': x=True
    elif x == 'n': x=False
    else:
        print("\nErorr Inpit")
        break

''' ---------------------------------------------------------------------------------------------------------------------------------------'''

conn.commit()
cur.close()
