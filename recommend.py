import helpers 
import pandas as pd 

class Recommender:

    def __init__(self):
        data = helpers.read_data()
        self.albums = data[0]
        self.bands = data[1]
        self.reviews = data[2]

    def get_album_recommendations_from_review(self, review, indices):
        index = indices[review]
        #Get the cosine similarity score for the row of the cosine matrix correpsonding to this review
        sim_scores = list(enumerate(self.get_review_similarities()[index]))
        #Get 5 most similar reviews 
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        rec_indices = [k[0] for k in sim_scores]
        album_ids = self.reviews['album'].iloc[rec_indices]
        print(album_ids)
        albums = []
        for id in album_ids:
            albums.append(self.albums.loc[self.albums['id'] == id])

        return albums

    def get_album_recommendations(self, album_name):
        album_id = self.albums.loc[self.albums['title'] == album_name]['id']
        if(self.reviews.loc[self.reviews['album'] == album_id].empty):
            print("there are no reviews of this album to base a recommendation off of")
        else:
            reviews = self.reviews.loc[self.reviews['album'] == album_id]
            max_score = 0 
            for review in reviews:
                if(float(review['score']) > max_score):
                    review_to_use = review
        self.get_album_recommendations_from_review(review_to_use['content'], indices = pd.Series(self.reviews.index, index=self.reviews['content']).drop_duplicates())
            
    #There are multiple reviews for some album, so we'll use the average rating 
    def get_score(self, album_id):
        avg_score = 0
        for review in self.reviews.loc[self.reviews['album'] == album_id]:
            avg_score += float(review['score'])

    def get_reviews(self):
        return self.reviews
    
    def get_bands(self):
        return self.bands
    
    def get_albums(self):
        return self.albums
    
    def get_review_similarities(self):
        return helpers.get_cosine_similarities(self.reviews)