# Ejercicio 13 - Filtra mensajes de un user específico

En este desafío implementarás una función que filtre los mensajes de un usuario específico. La función `filter_user_messages` recibirá dos parámetros:

- `messages`: una lista de mensajes
- `user`: un nombre de usuario.

Debe devolver una nueva lista que contenga solo los mensajes del usuario especificado.

La lista messages contiene diccionarios con información sobre cada mensaje, incluyendo el remitente ('sender') y el contenido del mensaje ('content').

> En caso de no encontrar mensajes del usuario deberá retornar una lista vacía `[]`

Ejemplo 1:

```txt
Input:

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
filter_user_messages(messages, user)

Output:

[
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

```

## Ejercicio 14 - Crea tu propio método map

En este desafío, deberás implementar una función personalizada que emule el comportamiento del método map utilizando funciones de orden superior.

La función recibirá dos parámetros: una lista y una función (func). La lista contendrá un conjunto de elementos (números, objetos, cadenas, etc.), y la función se utilizará para realizar una acción específica en cada elemento de la lista. El objetivo es retornar una nueva lista con los resultados obtenidos de aplicar la función a cada elemento, de manera similar a como lo haría el método map.

Ejemplo 1:

```txt

Input: my_map([1, 2, 3, 4], lambda num: num * 2)

Output: [2, 4, 6, 8]
```

Ejemplo 2:

```txt

Input: my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"])

Output: ["michi", "firulais"]
```
