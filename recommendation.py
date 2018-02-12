'''
Usage: python recommedation.py <user id>
eg: python recommedation.py 2 
'''

from lightfm import LightFM
import numpy as np
import scipy.sparse as sp
from datasets import fetch_news_data
import sys
import time

def train_model(data):
    stime = time.time()
    #create model
    model = LightFM(loss='warp')
    #train model
    model.fit(data['train'], epochs=30, num_threads=2, verbose=False)
    etime = time.time()
    ttime = etime - stime
    print('model fitted in ' + str(ttime) + " seconds")

    return model

def get_recommendation(model, data, user_ids):

    #generate recommendations for each user we input
    for user_id in user_ids:

        n_users, n_items = data['train'].shape

        #categories our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank in order
        top_items = data['categories_labels'][np.argsort(-scores)]
        #print top 3 results
        print("User %s" % user_id)
        print("\n     Recommended:")
        for x in top_items[:3]:
            print("     %s" % x)
    
    return top_items[:3]
    
if __name__ == "__main__":
    userid = int(sys.argv[1])
    data = fetch_news_data()
    model = train_model(data)
    recommedations = get_recommendation(model, data, [userid])