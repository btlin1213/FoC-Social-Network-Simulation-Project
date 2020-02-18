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

Project Credit: [Tim Baldwin](https://people.eng.unimelb.edu.au/tbaldwin/#top) - 2019 Semester 1 for Foundation of Computing

**all code in this repo, unless specified as example, are by Betty Lin** 
