list_of_movies=[ {"name":"alien","genre":"science fiction","rating":8.4,"release_year":2000},
                  {"name":"the martian","genre":"science fiction","rating":8.0,"release_year":2015},
                  {"name":"superbard","genre":"comedy","rating":7.6,"release_year":2007},
                  {"name":"airplane","genre":"comedy","rating":7.7,"release_year":1980},
                  { "name":"die hard","genre":"action","rating":8.2,"release_year":1988},
                  { "name":"gladiator","genre":"action","rating":8.5,"release_year":2000},
                  {"name": "Se7en", "genre": "thriller", "rating": 8.6, "year": 2007},
                  {"name": "Gone Girl", "genre": "thriller", "rating": 8.1, "year": 2014}]


user_genre=input("give me movie genra which you want to see:")
user_rating=float(input("what is menimum requirement of rating:"))
user_release_year=int(input("  preferred release year: "))
#preffered_movie=[]
#print(list_of_movies)
#We define a list of dictionaries, each representing a movie with its attributes.
#We iterate through each dictionary in the list using a for loop.
#Inside the loop, we use another for loop to iterate through the key-value pairs of each dictionary using the items() method.
#We print each key and its corresponding value.
#We use a conditional statement to check if the rating of each movie is greater than according to use preffernce.
#We add a newline for clarity between each movie.

movie_name=[]
for movie in list_of_movies:
    for keys ,values in movie.items():
        print(keys , values)
        
    if user_genre==movie['genre']:
        print(movie)
    if user_rating>=movie['rating']:
        movie_name.append(movie)
        print(movie)
    
        print(movie_name)
    else:
        print("your prefferd movie is not present")
