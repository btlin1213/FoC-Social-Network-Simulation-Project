from hidden import friend_besties, friend_second_besties
from collections import defaultdict
def friendly_prediction(unknown_user, features, bestie_dict, feat_dict):
    d = defaultdict(list)
    for feature in list(features):
        if feature not in feat_dict:
            d[feature] = []
        for bestie in friend_besties(unknown_user, bestie_dict):
            if bestie in feat_dict.keys() and feature in feat_dict[bestie]:
                d[feature].append(feat_dict[bestie][feature])
            else:
                for second_bestie in friend_second_besties(unknown_user, 
                                                           bestie_dict):
                    if second_bestie in feat_dict.keys() and feature in \
                     feat_dict[second_bestie]:                        
                        d[feature].append(feat_dict[second_bestie][feature])
        d[feature] = sorted(d[feature])
    return dict(d.items())