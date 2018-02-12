# news_recommendation

A simple news recommendation algorithm created using Singular Value Decomposition with the help of lightFM

## Prerequisites

```
Python (3.6)
sklearn
lightfm (pip install lightfm)
```

## Using the code

#### Case 1: when user searches for a news article eg - Mooncakes

```
Usage: python update.py <mode> <input category> <user id>
eg: python update.py 1 Mooncakes 3
Modes: 
1 - update ratings for a user id
2 - delete ratings for a user id 
```
 
#### Case 2: getting recommedations for a user

```
Usage: python recommedation.py <user id>
eg: python recommedation.py 2 
```
  
#### Case 3: Deleting a rating (not a useful use case)
```
Usage: python update.py <mode> <input category> <user id>
eg: python update.py 2 Mooncakes 3
Modes: 
1 - update ratings for a user id
```

## Acknowledgments

* Resources on https://github.com/lyst/lightfm
* https://www.youtube.com/watch?v=9gBC9R-msAk
