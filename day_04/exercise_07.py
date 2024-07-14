def get_package_info(packages):
    total_weight = 0
    destination_counts = {}
    
    for package in packages:
        id, weight, destination = package
        total_weight += weight
        if destination in destination_counts:
            destination_counts[destination] += 1
        else:
            destination_counts[destination] = 1
    
    return {
        "total_weight": round(total_weight, 2),
        "destinations": destination_counts
    }

# Ejemplo de uso
print(get_package_info([
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
]))
