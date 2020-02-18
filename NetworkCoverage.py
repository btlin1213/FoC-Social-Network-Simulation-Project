# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# THE FUNCTIONS FROM PART II AND PART III
from hidden import friend_besties, friend_second_besties

def besties_coverage(individuals, bestie_dict, relationship_list):
    '''Calculates the ratio of connected nodes within a social network 
    to the total number of nodes in the social network'''
    
    # initialise the count of friend(s) to 1 
    count = 1
    
    # the nested 'for' statements iterates through the elements in
    # each input. For each friend that satisfies the relationship iterated in 
    # relationship_list (third input), update value of count to (count + 1)
    for relationship in relationship_list:
        for individual in individuals:
            for friend in relationship(individual, bestie_dict): 
                count += 1
                
    # express the final value of count as a percentage of the total number
    # of people in the network of bestie_dict
    return count / len(bestie_dict)
 