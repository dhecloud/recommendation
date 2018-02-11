from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import numpy as np
import scipy.sparse as sp
from datasets import fetch_news_data

data = fetch_news_data()

#create model
model = LightFM(loss='warp')
#train model
model.fit(data['train'], epochs=30, num_threads=2, verbose=True)
print('done!')

def get_recommendation(model, data, user_ids):

    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:


        #categories our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank in order
        top_items = data['categories_labels'][np.argsort(-scores)]
        #print top 3 results
        print("User %s" % user_id)
        print("\n     Recommended:")
        for x in top_items[:3]:
            print("     %s" % x)

if __name__ == "__main__":
    get_recommendation(model, data, [2])
