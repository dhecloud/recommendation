import itertools
import scipy.sparse as sp
from sklearn import preprocessing
import numpy as np

def _parse_data(data):

    for line in data:
        if not line:
            continue

        uid, iid, rating, timestamp = [int(x) for x in line.split('\t')]
        yield uid, iid , rating, timestamp

def _parse_news_category(news_category_raw):

    categories = []

    for line in news_category_raw:
        if line:
            category, catid = line.split('|')
            categories.append('{}'.format(category))

    category_feature_labels = np.array(categories)

    return category_feature_labels

def _get_dimensions(train_data):

    uids = set()
    iids = set()

    for uid,iid, r, _ in itertools.chain(train_data):

        uids.add(uid)
        iids.add(iid)

    rows = max(uids) + 1
    cols = max(iids) + 1
    return rows, cols

def _build_matrix(rows, cols, data):


    matrix = sp.lil_matrix((rows,cols), dtype = np.float32)
    for uid, iid, rating, _ in itertools.chain(data):
        #increase each rating by 1 (to account for rating of 0 == 1)
        matrix[uid, iid] = rating +1

    matrix = matrix.tocsr()
    #set missing ratings to 1 (minimum rating is 1)
    matrix[matrix==0] = 1.0
    matrix = preprocessing.normalize(matrix)
    print("normalized!")
    return matrix.tocoo()

def read_raw_data(path):
    newsfile = open(path)
    return newsfile

def fetch_news_data():

    train_raw = read_raw_data("data/newsmatrix.txt")
    categories_raw = read_raw_data("data/categories.txt")

    num_users , num_items = _get_dimensions(_parse_data(train_raw))

    train_raw = read_raw_data("data/newsmatrix.txt")

    train = _build_matrix(num_users, num_items, _parse_data(train_raw))
    print(train)
    categories_feature_labels = _parse_news_category(categories_raw)

    data = {'train': train,
            'categories_labels': categories_feature_labels}

    return data
