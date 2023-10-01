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
        sim_scores = sim_scores[1:26]
        rec_indices = [k[0] for k in sim_scores]
        all_albums = self.reviews['album'].iloc[rec_indices]
        unique_ids = []
        for a in all_albums.items():
            if(a[1] not in unique_ids):
                unique_ids.append(a[1])
        album_ids = unique_ids[0:5]
        albums = []
        for album_id in album_ids:
            albums.append(self.albums.loc[self.albums['id'] == album_id])
        return albums

    def get_album_recommendations(self, album_name):
        album_id = int(self.albums.loc[self.albums['title'] == album_name]['id'].to_numpy()[0])
        if(self.reviews.loc[self.reviews['album'] == album_id].empty):
            print("there are no reviews of this album to base a recommendation off of")
            return
        else:
            reviews = self.reviews.loc[self.reviews['album'] == album_id]
            max_score = 0 
            for index, review in reviews.iterrows():
                if(float(review['score']) > max_score):
                    review_to_use = review
            return self.get_album_recommendations_from_review(review_to_use['content'], indices = pd.Series(self.reviews.index, index=self.reviews['content']).drop_duplicates())
            
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