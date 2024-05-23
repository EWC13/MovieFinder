import requests
import tmdbsimple as tmdb
import json

secrets_filename = 'secretKeys'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

print(api_keys['APIKEY'])

listOfGenres = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family",
                    "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "TV Movie",
                    "Thriller", "War", "Western"]
genre_id = {"Action":"28","Adventure":"12","Animation":"16","Comedy":"35","Crime":"80","Documentary":"99","Drama":"18","Family":"10751","Fantasy":"14","History":"36","Horror":"27",
            "Music":"10402","Mystery":"9648","Romance":"10749","Science Fiction":"878","TV Movie":"10770","Thriller":"53","War":"10752","Western":"37"}
page = 1
results = []
movieDict = {}


def printGenres():
    num = 1
    
    for gen in listOfGenres:
        print(str(num)+".)"+gen)
        num += 1


def MovieViewer():
    print("Movies Have been ordered by the average score from voters(Greatest to Least)")
    #beginning = input(f"Enter what number in the list you would like to begin(0-{len(movieDict)})" )
    length = input(f"What number of movies would you like to see?(1-{len(movieDict)}): ")
    while True:
        if length != "q":
            print("**********************************************")
            for movie in range(int(length)):
                ordered = sorted(movieDict, reverse=reversed)[movie]
                print(movieDict[ordered])
            print("**********************************************")
            length = input(f"What number of movies would you like to see?(1-{len(movieDict)}): ")
        else:
            print("Enjoy your Movie!")
            break


printGenres()
genre = input("Select a Genre from the Menu: ")

while True:
    if genre not in listOfGenres:
        print("Please enter one of the genres in the menu!")
        printGenres()
        genre = input()
    else:
        break

# make api call for 5 pages of themoviedb API 
while page < 5:
    response1 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+api_keys['APIKEY']+'&with_genres='+ genre_id[genre]+'&page='+str(page))
    results.append(response1.json())
    page += 1


# find the titles and vote average of movies on each page
for page in range(len(results)):
    #print(page)
    movies = results[page]['results']
    for value in movies:
        if value['original_language'] == 'en' and value['vote_average'] < 10.0 and value['vote_average'] > 5.0:
            #print(value['original_title'], value['vote_average'])
            if value['original_title'] not in movieDict.values():
                movieDict[value['vote_average']] = value['original_title']

MovieViewer()