def get_friendly_dict(friend_list):

    '''Takes a list of friendship links and calculate the degree-one 
    friends of each individual in the list'''

    # create empty dictionary for addition of key(individual)
    # and values(individual's degree-one friends) 
    friend_dict = {}
    
    # account for all possible scenarios for each pair in input list
    for pair in friend_list:
        if pair[0] not in friend_dict.keys():
            friend_dict[pair[0]] = {pair[1]}
        if pair[1] not in friend_dict.keys():
            friend_dict[pair[1]] = {pair[0]}
        if pair[0] in friend_dict.keys():
            friend_dict[pair[0]].add(pair[1])
        if pair[1] in friend_dict.keys():
            friend_dict[pair[1]].add(pair[0])
            
    return friend_dict
