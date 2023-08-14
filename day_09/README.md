# Ejercicio 15 - Maneja correctamente los errores

En este desafío, debes crear una función llamada `calculate_average` que calcule el promedio de una lista de números. Sin embargo, la función debe manejar correctamente dos casos especiales:

- Si la lista está vacía, la función debe generar una excepción ValueError con el mensaje "La lista está vacía".

- Si la lista contiene elementos que no son números, la función debe generar una excepción TypeError con el mensaje "La lista contiene elementos no numéricos".

Tu objetivo es implementar la función calculate_average de manera que maneje adecuadamente estos casos y devuelva el promedio de los números en la lista.

Aquí tienes algunos ejemplos de entrada y salida esperada:

Ejemplo 1:

```txt

Input: calculate_average([1, 2, 3, 4, 5])
Output: 3.0
```

Ejemplo 2:

```txt

Input: calculate_average([10, 20, 30, 40, 50])
Output: 30.0
```

Ejemplo 3:

```txt

Input: calculate_average([])
Output: ValueError: La lista está vacía
```

Ejemplo 4:

```txt

Input: calculate_average([1, 2, '3', 4, 5])
Output: TypeError: La lista contiene elementos no numéricos
```

## Ejercicio 16 - Manejo de excepciones

En este desafío, debes crear una función llamada `calculate_discounted_price` que calcule el precio con descuento de un producto. La función recibirá dos parámetros: `price` (precio) y `discount` (descuento). Tu objetivo es implementar la lógica necesaria para calcular el precio con el descuento aplicado.

Sin embargo, hay algunas condiciones y manejo de excepciones que debes tener en cuenta:

- Si el precio o el descuento son valores negativos, deberás lanzar una excepción del tipo `ValueError` con el mensaje "El precio y el descuento deben ser valores positivos".

- Si el precio o el descuento no son números, deberás lanzar una excepción del tipo `TypeError` con el mensaje "El precio y el descuento deben ser números".

- En caso de que ocurra cualquier otro tipo de excepción no prevista, deberás capturarla y lanzar una excepción genérica del tipo `Exception` con el mensaje "Ha ocurrido un error inesperado" seguido del mensaje de la excepción original para obtener más detalles.

Tu función debe retornar el precio con el descuento aplicado. Si el cálculo se realiza correctamente, deberás retornar el resultado. En caso de producirse alguna excepción, deberás propagarla para que pueda ser manejada en el contexto adecuado.

Ejemplo 1:

```txt

Input: calculate_discounted_price(100, 0.2)
Output: 80.0
```

Ejemplo 2:

```txt

Input: calculate_discounted_price(-50, 0.2)
Output: ValueError: El precio y el descuento deben ser valores positivos
```
