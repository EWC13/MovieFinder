# MovieFinder

# Description
In this project I used the TMDb API to get a list of movies in JSON format, I then parsed through that getting the names and voter scores. I created a dictionary with the ordered values based on the voter scores. In order to run this code you will need to access and create an account, along with generating an API key on the [TMDb website](https://www.themoviedb.org/). I used the tmdbsimple library as the documentation also provided in that link was easy to follow. I also used the requests library to make the API call, it is called 5 times in the code I have hear on github, each call is a new page.

# What I learned
I was familiar with APIs, but I have never actually created a project calling an API. So I got to learn how to interact with the API and the value with an API key. I also used a dictionary twice within this project in order to make sure the proper genre is selected and then to sort those top movies in descending order based on their voter rating. 

# How to Run
It is pretty simple to run.

```python movieSorter.py```

After that you will be presented with a menu of the genres from where you will select the genre, then you will have the choice to select the number of movies you want displayed.

# Helpful links
- [https://adinasteinman.medium.com/navigating-my-first-api-the-tmdb-database-d8d2975b0df4]
- [https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee]
- [https://developer.themoviedb.org/reference/discover-movie]
- [https://developer.themoviedb.org/docs/getting-started]
