# ✅ Exercise 05 - Find the Most Famous Kittens

In this challenge, you need to find the most famous kitten based on the number of followers.

You will receive a list of dictionaries that will include the following properties:

- `"name"`: the name of the kitten.
- `"followers"`: a list of numbers, where each number represents the followers on each social network.

Your task is to return a list with the names of the cats that have **only the highest number of followers.** If there are two or more cats with the same maximum number of followers, you should include them in the resulting list, keeping the order in which they appear in the input list.

You will have inputs and outputs like the following 👇

Example 1:

```python
Input: find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

Output: ["Luna"]
```

Example 2:

```python
Input: find_famous_cat([
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
])

Output: ["Milo", "Gizmo"]

```

# ✅ Exercise 06 - Get the Average of the Students

In this challenge, you must calculate the overall average of a class, as well as the individual average of each student.

To do this, you will be provided with a list of dictionaries, each of which will represent a student and have the following properties:

- `"name"`: The name of the student
- `"grades"`: The grades of each subject of the student

From this information, you should return a new dictionary that has the property `"class_average"` with the class average and a list of `"students"` with the students and their individual averages.

It is important to mention that the averages must be calculated accurately and rounded to two decimal places so that the tests pass without any problem. You can use the `round()` method which is used as follows 👇

```py

number = 100.32433
number = round(number, 2)

# 100.32

```

Example:

```py

Input: get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])

Output: {
  "class_average": 88.17,
  "students": [
    {
      "name": "Pedro",
      "average": 88.75
    },
    {
      "name": "Jose",
      "average": 88.5
    },
    {
      "name": "Maria",
      "average": 87.25
    }
  ]
}

```

# Exercise 07 - Get the Package Information

In this challenge, you are working for a freight transportation company that needs to keep track of the packages sent on each trip. To do this, you will be provided with a list of tuples, each of which will represent a package and have the following properties:

- (id, weight, destination)

From this information, you should create a function that calculates the total weight of the packages, as well as the number of packages that will be sent to each destination. To do this, you should return a new dictionary that has the following properties:

- `"total_weight"`: The total weight of the packages.
- `"destinations"`: A dictionary with the destinations as keys and the number of packages as values.

It is important to mention that the function must round the total weight to two decimal places and that each destination must appear only once in the dictionary.

Example:

```py

Input:

[
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
]

Output:

{
  "total_weight": 171.50,
  "destinations": {
    "Mexico": 3,
    "Colombia": 4,
    "Argentina": 3
  }
}

```
