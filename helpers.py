import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def read_data():
    albums = pd.read_csv('metal_data/albums.csv')
    bands = pd.read_csv('metal_data/bands.csv')
    reviews = pd.read_csv('metal_data/reviews.csv')
    return albums, bands, reviews

def get_cosine_similarities(reviews):
    #Define a TF-IDF vectorizer and remove all english stop words.
    tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    reviews['content'] = reviews['content'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tf_idf_mat= tfidf.fit_transform(reviews['content'])
    return linear_kernel(tf_idf_mat, tf_idf_mat)