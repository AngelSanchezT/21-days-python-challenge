# ✅ Ejercicio 03 - Averigua si un año es bisiesto

En este desafío de Python, debes crear la lógica de la función `is_leap_year`, que determina si un año es bisiesto o no. Un año es bisiesto si cumple con las siguientes condiciones:

- Es divisible por 4, pero no por 100.
- Si es divisible por 100 debe serlo por 400 también.

La función `is_leap_year` recibe un único parámetro: el año a evaluar. Debe devolver `True` si el año es bisiesto o `False` en caso contrario.

Toma en cuenta que la función debe ser capaz de manejar valores no enteros o negativos.

Ejemplo 1:

```
Input: 2000;
Output: true;
```

Ejemplo 2:

```
Input: -2024;
Output: false;
```

Ejemplo 3:

```
Input: 1984.25;
Output: false;
```

# ✅ Ejercicio 04 - Dibuja un triangulo usando bucles


En este desafío, debes dibujar un triángulo equilatero usando bucles.

Recibirás dos parámetros: `size` y `character`, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, respectivamente. Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

> Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable.
> 

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:

```
Input: printTriangle(3, "*")
Output:
  *
 ***
*****
```

Ejemplo 2:

```
Input: printTriangle(6, "$")
Output:
     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$
$$$$$$$$$$$
```