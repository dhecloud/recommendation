from datasets import _parse_news_category, read_raw_data
import sys
import numpy as np
import time


CATPATH = "data/categories.txt"
MATRIXPATH = "data/newsmatrix.txt"

def get_cur_news_cat(path):
    #open categories.txt
    categories_raw = read_raw_data(path)
    #parse categories list
    cat_labels = _parse_news_category(categories_raw)
    categories_raw.close()
    return cat_labels


#primitive algo, will not scale well for huge txt files
def update_cur_news_matrix(path, userid, itemid, rating):
    assert type(userid) is int 
    assert type(itemid) is int 
    assert type(rating) is int 
    found = 0
    i = 0
    with open(path, "r") as matfile:
        for line in matfile:
            if not line:
                continue
            uid, iid, currating, timestamp = line.split('\t')
            if int(uid) == int(userid) and int(iid) == int(itemid):
                print("found!")
                found = 1
                break
            i+=1
        if found is 0:
            print("user id and item id not currently in matrix!")
            return 0
        
    matfile.close()
    matfile = open(path, "r+")
    lines = matfile.readlines()
    lines[i] = str(userid) + "\t" + str(itemid) + "\t" + str(rating) + "\t" + str(int(time.time())) 
    if i != len(lines) - 1:
        lines[i] += "\n"
    matfile.seek(0)
    matfile.writelines(lines)
    matfile.close
    print("updated ratings!")
    
    
def update_new_newsmatrix(path, userid, itemid, rating):
    assert type(userid) is int 
    assert type(itemid) is int 
    assert type(rating) is int 
    
    with open(path, "a") as matfile:
        newline = "\n" + str(userid) + "\t" + str(itemid) + "\t" + str(rating) + "\t" + str(int(time.time()))
        matfile.write(newline)
    matfile.close()
    print("matfile updated!")

def update_new_cat(cat, path, num):
    with open(path, "a") as catfile:
        newline = "\n"+str(cat)+"|"+str(num)
        catfile.write(newline)
    catfile.close()
    print("categories file updated!")

def delete_cur_cat(cat, path):
    cat_labels = list(get_cur_news_cat(CATPATH))
    i = cat_labels.index(cat)
    print(i)
    catfile = open(path, "r+")
    lines = catfile.readlines()
    lines.pop(i)
    catfile.seek(0)
    catfile.writelines(lines)
    catfile.close
    print("deleted categories!")

if __name__ == "__main__":
    delete_cur_cat("World", CATPATH)
    '''
    inputcat = sys.argv[1]
    #get current categories
    cat_labels = get_cur_news_cat(CATPATH)
    #if cat in list: do nothing
    if inputcat in cat_labels:
        pass
    else:
        #update category.txt
        update_new_cat(inputcat, CATPATH, len(cat_labels))
        cat_labels += [inputcat]
    #update newsmatrix
    update_new_newsmatrix(MATRIXPATH, 4, 2, 3)
    '''