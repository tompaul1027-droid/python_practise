followers={"a","b","c","d"}
following={"a","b","c","d","e"}
following.difference_update(followers)
if("followers"!="following"):
    print("you are not eligable")
print(following)