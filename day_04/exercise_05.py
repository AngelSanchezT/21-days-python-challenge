def find_famous_cat(cats):
    max_followers = 0
    famous_cats = []
    
    for cat in cats:
        total_followers = sum(cat["followers"])
        if total_followers > max_followers:
            max_followers = total_followers
            famous_cats = [cat["name"]]
        elif total_followers == max_followers:
            famous_cats.append(cat["name"])
    
    return famous_cats