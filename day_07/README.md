# Ejercicio 11 - Encuentra palabras con dos vocales

En este desafío, debes crear la lógica de la función `find_words_with_two_vowels` que encuentre las palabras que contienen **exactamente dos vocales** en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas las palabras de la lista original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.

Ejemplo 1:

```txt
Input: find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

Output: ["hello", "platzi"]

```

Ejemplo 2:

```txt
Input: find_words_with_two_vowels(["text", "test", "python", "example"])
Output: []

```

## Ejercicio 12 - Calcula la longitud de las palabras

En este desafío, debes crear una función llamada `count_words_by_length` que recibe una lista de palabras y devuelve un diccionario que mapea la longitud de las palabras a la cantidad de palabras que tienen esa longitud.

Ejemplo 1:

```txt
Input:
count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

Output:
{5: 1, 6: 2, 10: 1, 4: 2}

```

Ejemplo 2:

```txt
Input:
count_words_by_length([
  "apple",
  "banana",
  "orange"
])

Output:
{5: 1, 6: 2}

```
