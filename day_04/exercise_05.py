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

# Ejemplo de uso
print(find_famous_cat([
    {
        "name": "Luna",
        "followers": [500, 200, 300]
    },
    {
        "name": "Michi",
        "followers": [100, 300]
    },
]))

print(find_famous_cat([
    {
        "name": "Mimi",
        "followers": [320, 120, 70]
    },
    {
        "name": "Milo",
        "followers": [400, 300, 100, 200]
    },
    {
        "name": "Gizmo",
        "followers": [250, 750]
    }
]))
