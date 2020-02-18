# -Python-FoC-Project-1
## The "Power" of Social Networks

### Introduction
Project 1 is all about "social networks", and the power of social connections, both in terms of how impressively large a portion of the social network can be accessed from a small number of seed users and their friends/friends-of-friends, and how accurately the attributes of an individual can be predicted from (partial) attributes of their friends/friends-of-friends. A large part of the context for the project is in illustrating how it is that companies such as Cambridge Analytica are able to influence the world so impressively, from a small set of users of their products.

Throughout the project, we will refer to individuals as "nodes" in the social network, and (mutual) friendship connections as "edges" connecting those nodes. See the lecture slides for more details.

### Part I: _Friends_
Write a function `get_friendly_dict()` that calculates the degree-one friends of each individual in a social network. The function takes one argument:

- `friend_list`, a list of reciproal friendship links between individuals.
The function should return a dictionary of sets, containing the set of all "degree-one" (= immediate) friends for each individual in the social network. Note that the specific order of the individuals in the dictionary, and also the ordering of the friends in each set does not matter.

The structure of `friend_list` is as follows: each element is a 2-tuple of strings, representing a pairing of names of individuals in the social network who are friends. Note that as friendship links are reciprocal, the 2-tuple `('kim', 'sandy')`, e.g., indicates that `'kim'` is a friend of `'sandy'`, and also that `'sandy'` is a friend of `'kim'`.

Example function calls are:

```
>>> get_friendly_dict([('kim', 'sandy'), ('alex', 'sandy'), ('kim', 'alex'), ('kim', 'glenn')])
{'kim': {'glenn', 'sandy', 'alex'}, 'sandy': {'kim', 'alex'}, 'alex': {'sandy', 'kim'}, 'glenn': {'kim'}}
>>> get_friendly_dict([('kim', 'sandy'), ('sandy', 'alex'), ('alex', 'glenn'), ('glenn', 'kim')])
{'kim': {'glenn', 'sandy'}, 'sandy': {'kim', 'alex'}, 'alex': {'glenn', 'sandy'}, 'glenn': {'kim', 'alex'}}
```

### Part II: _Social Network Besties_
Write a function `friend_besties()` that calculates the "besties" (i.e. degree-one friends) of a given individual in a social network. The function takes two arguments:

- `individual`, an individual in the social network, in the form of a string ID.
- `bestie_dict`, a dictionary of sets of friends of each individual in the social network (as per the first question of the Project)
The function should return a sorted list, made up of all "degree-one" friends for the individual. In the instance that the individual does not have any friends in the social network, the function should return an empty list.

Example function calls are:

```
>>> get_friendly_dict([('kim', 'sandy'), ('alex', 'sandy'), ('kim', 'alex'), ('kim', 'glenn')])
{'kim': {'glenn', 'sandy', 'alex'}, 'sandy': {'kim', 'alex'}, 'alex': {'sandy', 'kim'}, 'glenn': {'kim'}}
>>> get_friendly_dict([('kim', 'sandy'), ('sandy', 'alex'), ('alex', 'glenn'), ('glenn', 'kim')])
{'kim': {'glenn', 'sandy'}, 'sandy': {'kim', 'alex'}, 'alex': {'glenn', 'sandy'}, 'glenn': {'kim', 'alex'}}

```

### Part III: _Social Network Second Besties_
Write a function `friend_second_besties()` that calculates the "second-besties" (i.e. degree-two friends) of a given individual in a social network. The function takes two arguments:

- `individual`, an individual in the social network, in the form of a string ID.
- `bestie_dict`, a dictionary of sets of friends of each individual in the social network (as per the first question of the Project)

The function should return a sorted list, made up of all "degree-two" friends for the individual. In the instance that the individual does not have any degree-two friends in the social network, the function should return an empty list.

Example function calls are:

```
>>> friend_second_besties('glenn', {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}})
['alex', 'sandy']
>>> friend_second_besties('kim', {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}})
[]

```
### Part IV: _Network Coverage_
**a hidden program is written to store the code from Part II and Part III for use in Part IV and Part V**
Write a function `besties_coverage()` that computes the "coverage" of nodes within a social network that are connected via predefined relationships to a given list of individuals, i.e. the proportion of connected individuals, to the total size of the network (= the number of people in the social network). The function takes three arguments:

- `individuals`, a list of individuals, each in the form of a string ID;
- `bestie_dict`, a dictionary of sets of friends of each individual in the social network (as per the first question of the Project); and
- `relationship_list`, a list of functions defining relationships in the social network, selected from `friend_besties` and `friend_second_besties`.

The function should return a float, corresponding to the proportion of the total number of individuals who are either a member of `individuals` or connected via one of the relationships in `relationship_list`.

Example calls to the function are:

```
>>> besties_coverage(['glenn'], {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, [])
0.25
>>> besties_coverage(['glenn'], {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, [friend_besties])
0.5
>>> besties_coverage(['glenn'], {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, [friend_second_besties])
0.75
>>> besties_coverage(['glenn'], {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, [friend_besties, friend_second_besties])
1.0

```

### Part V: _Social Network Attribute Prediction_
**a hidden program is written to store the code from Part II and Part III for use in Part IV and Part V** 

The final question is for bonus marks, and is deliberately quite a bit harder than the four basic questions (and the number of marks on offer is deliberately not commensurate with the amount of effort required — bonus marks aren't meant to be easy to get!). Only attempt this is you have completed the earlier questions, and are up for a challenge!

The context for the bonus question is the prediction of attributes of a user based on the attributes of their social network, and the observation that a user's friends often have very similar interests and background to that user (what is formally called homophily).

Write a function `friendly_prediction()` which takes four arguments:

- `unknown_user`, a string indicating the identity of the user you are to predict attributes for;

- `features`, a set of features you are to predict attributes for;

- `bestie_dict`, a dictionary of sets of the besties for each user in the dataset, following the same format as the earlier questions in the project;

- `feat_dict`, a dictionary containing the known attributes for each user in the training data, across a range of features; note that there is no guarantee that the attribute for a given feature will be known for every training user.

Your function should return a dictionary of features (based on `features`), with a predicted list of values for each.

Your function should make its predictions as follows:

- first, identify the set of besties for the given user, and for each feature of interest, determine the most-commonly attested attribute for that feature among the besties; in the case of a tie, the prediction should be a sorted list of attributes;

- second, for any features where no bestie has an attribute for that feature (meaning no prediction was possible in the first step), repeat the process using the second-besties, once again in the form of a sorted list of attributes;

- in the case that no bestie or second-bestie has that attribute, return an empty list.

Note that all attributes will take the form of strings, with the empty string representing the fact that the user explicitly has no value for that feature (e.g. if the user did not go to university, the value for university would be ''), and the lack of an attribute for a given feature indicating that the attribute is unknown. Note further that even if the attribute for `unknown_user` is available in `feat_dict`, you should predict based on the attributes of besties and second besties.

Example calls to the function are:

```
>>> friendly_prediction('glenn', {'favourite author', 'university'}, {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, {'glenn': {'university': ''}, 'kim': {'favourite author': 'AA Milne'}, 'sandy': {'favourite author': 'JRR Tolkien', "university": "University of Melbourne"}, 'alex': {'favourite author': 'AA Milne', 'university': 'Monash University'}})
{'university': ['Monash University', 'University of Melbourne'], 'favourite author': ['AA Milne']}
>>> friendly_prediction('kim', {'university'}, {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, {'glenn': {'university': ''}, 'kim': {'favourite author': 'AA Milne'}, 'sandy': {'favourite author': 'JRR Tolkien', "university": "University of Melbourne"}, 'alex': {'favourite author': 'AA Milne', 'university': 'Monash University'}})
{'university': ['', 'Monash University', 'University of Melbourne']}
>>> friendly_prediction('kim', {'birthplace'}, {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, {'glenn': {'university': ''}, 'kim': {'favourite author': 'AA Milne'}, 'sandy': {'favourite author': 'JRR Tolkien', "university": "University of Melbourne"}, 'alex': {'favourite author': 'AA Milne', 'university': 'Monash University'}})
{'birthplace': []}

```
Project Credit: [Tim Baldwin](https://people.eng.unimelb.edu.au/tbaldwin/#top) - 2019 Semester 1 for Foundation of Computing

**all code in this repo, unless specified as example, are by Betty Lin** 
