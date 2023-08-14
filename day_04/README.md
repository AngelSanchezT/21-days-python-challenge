# ✅ Ejercicio 05 - Encuentra a los gatitos más famosos

En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:

"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, manteniendo el orden en el que aparecen en la lista de entrada.

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:

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
Ejemplo 2:

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

## ✅ Ejercicio 06 - Obtén el promedio de los estudiantes

En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.

Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá las siguientes propiedades:

- `"name"`: El nombre del estudiante
- `"grades"`: Las notas de cada materia del estudiante

A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad `"class_average"` con el promedio de la clase y una lista de `"students"` con los estudiantes y sus promedios individuales.

Es importante mencionar que los promedios deben ser calculados con precisión y se deben redondear a dos decimales para que los test pasen sin problema alguno. Puedes usar el método `round()` el cual se usa de la siguiente manera 👇

```py
number = 100.32433
number = round(number, 2)

# 100.32
```

Ejemplo:

```txt

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

## Ejercicio 07 - Obten la información de los paquetes

En este desafío, te encuentras trabajando para una empresa de transporte de carga que necesita llevar un registro de los paquetes que se envían en cada viaje. Para ello, se te proporcionará una lista de tuplas, cada una de las cuales representará un paquete y tendrá las siguientes propiedades:

- (id, weight, destination)

A partir de esta información, debes crear una función que calcule el peso total de los paquetes, así como la cantidad de paquetes que se enviarán a cada destino. Para ello, debes retornar un nuevo diccionario que tenga las siguientes propiedades:

- `"total_weight"`: El peso total de los paquetes.
- `"destinations"`: Un diccionario con los destinos como claves y la cantidad de paquetes como valores.

Es importante mencionar que la función debe redondear el peso total a dos decimales y que cada destino debe aparecer sólo una vez en el diccionario.

Ejemplo:

```txt

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
