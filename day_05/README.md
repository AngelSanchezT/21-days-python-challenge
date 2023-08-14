# Ejercicio 08 - Calcula la cantidad de letras en una oración

En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.

Ejemplo 1:

```txt

Input: "Hola mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
}

```

## Ejercicio 09 - Encuentra el mayor palíndromo

En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.

Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista, la función debe devolver `None`. Si hay más de un palíndromo con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.

> Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante como hacia atrás.

Ejemplo 1:

```txt

Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

Output: "racecar"
```

Ejemplo 2:

```txt

Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])

Output: None
```
