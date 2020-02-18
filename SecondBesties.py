def friend_second_besties(individual, bestie_dict):

    '''Calculate the degree-2 friends, that is, friends of friends
    of a given individual in a social network'''
    
    # initialise empty list for appending the names of degree-two friends
    # of individual (first input) and return as answer at the end of execution
    answer = []
    # the nested if-for-for-if statements ensure the individual (first input)
    # is a key in the besties dictionary and that only the degree-two friends  
    # have their names appended to the answer list (omit degree-one friends).

    if individual in bestie_dict.keys():
        for degree_1 in list(bestie_dict[individual]):
            for name in list(bestie_dict[degree_1]):
                if name != individual and name not in bestie_dict[individual]:
                    answer.append(name)
        return sorted(answer)
    
    # if any of the conditions mentioned in previous comment is
    # not satisfied, return an empty list to symbolise 0 degree-two friends

    else:
        return []