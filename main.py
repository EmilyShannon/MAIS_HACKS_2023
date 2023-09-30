import pandas as pd
import recommend
import helpers 

def get_input():
    current_album = input("Hi! Welcome to your AI metal recommendation tool. I'm here to recommend you some new albums. What album do you want this one to remind you of? ")
    recommend_albums(current_album)

# def recommend_bands(current_band):
#     recommender = recommend.Recommender()
#     bands = recommender.get_bands()
#     if(not (bands.loc[bands['title'] == current_band].empty)):
#         bands = recommender.get_band_recommendations()
#     else:
#         print("the band you chose is not in the database!")
#         return 
#     show_recommended_bands(bands)

def recommend_albums(current_album):
    recommender = recommend.Recommender()
    albums = recommender.get_albums()
    if(not (albums.loc[albums['title'] == current_album].empty)):
        albums = recommender.get_album_recommendations(current_album)
    else:
        print("the album you chose is not in the database!")
        return
    show_recommended_albums(albums)

# def show_recommended_bands(bands):
#     print("todo")

def show_recommended_albums(albums):
    print("todo")


get_input()