# ✅ Ejercicio 02 - Calcula la propina

En este desafío tendrás que calcular la propina que deben dejar los clientes de un restaurante en función de su consumo.

La función `calculate_tip` recibirá dos parámetros, `bill_amount` que representa el costo total de lo que se haya consumido y `tip_percentage` que representa el porcentaje de propina a dejar. Ambos valores serán de tipo float y siempre serán positivos, incluyendo el 0. La función deberá devolver el valor de la propina como un número.

> Recuerda que para redondear a dos decimales tendrás que hacer uso de round(numero, cantidad de decimales)

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:

```python
Input: calculate_tip(100, 10);
Output: 10;
```

Ejemplo 2:

```python
Input: calculate_tip(1524.33, 25);
Output: 381.08;
```