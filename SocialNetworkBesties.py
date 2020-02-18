def friend_besties(individual, bestie_dict):

    '''Calculate the degree of a given individual in
    a social network'''
    
    # function returns a sorted list of the values  
    # under the key called individual (first input) 
    if individual in bestie_dict.keys():
        return sorted(list(bestie_dict[individual]))
    
    # return empty list if individual (first input) 
    # is not a key in the dictionary
    else:
        return []
    

