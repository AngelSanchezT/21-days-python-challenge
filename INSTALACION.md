# Guía de Instalación de Python y pip en Windows

## Paso 1: Descargar e instalar Python

1. Visita la página oficial de [descargas de Python](https://www.python.org/downloads/).
2. Descarga el instalador adecuado para tu sistema (generalmente, "Windows x86-64 executable installer" para sistemas de 64 bits).
3. Ejecuta el instalador y asegúrate de seleccionar la opción **"Add Python to PATH"** antes de hacer clic en **"Install Now"**.

## Paso 2: Verificar la instalación de Python y pip

1. Abre una terminal o símbolo del sistema (puedes buscar "cmd" en el menú de inicio).
2. Escribe `python --version` para verificar que Python está instalado correctamente. Deberías ver la versión de Python que instalaste.
3. Escribe `pip --version` para verificar que pip también está instalado. Deberías ver la versión de pip instalada.

## Paso 3: Instalar pip manualmente (si no se instaló automáticamente)

1. Si por alguna razón pip no se instaló automáticamente, puedes instalarlo manualmente:
   1. Descarga el script `get-pip.py` desde el siguiente enlace: [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
   2. Guarda el archivo en una ubicación fácil de recordar, por ejemplo, en tu escritorio.
   3. Abre una terminal o símbolo del sistema y navega hasta el directorio donde guardaste `get-pip.py`. Puedes usar el comando `cd` para cambiar de directorio, por ejemplo:
      ```sh
      cd Desktop
      ```
   4. Ejecuta el siguiente comando para instalar pip:
      ```sh
      python get-pip.py
      ```

## Paso 4: Actualizar pip (opcional)

Es recomendable actualizar pip a la última versión. Puedes hacerlo con el siguiente comando:

```sh
python -m pip install --upgrade pip
```

## Solución de Problemas: "pip" no se reconoce como un comando interno o externo

Si recibes el error `"pip" no se reconoce como un comando interno o externo`, sigue estos pasos:

1. **Asegurarse de que Python está en el PATH**:
   - Abre una terminal o símbolo del sistema y escribe `python --version` para verificar si Python está en el PATH. Si este comando no funciona, Python tampoco está en el PATH.
   - Durante la instalación de Python, asegúrate de seleccionar la opción "Add Python to PATH". Si olvidaste hacerlo, deberás agregar Python al PATH manualmente.

2. **Agregar Python y Scripts al PATH manualmente**:
   - Encuentra la ubicación donde instalaste Python. Por defecto, suele estar en una de estas rutas:
     ```
     C:\Python39
     C:\Users\[tu_usuario]\AppData\Local\Programs\Python\Python39
     ```
   - Abre las **Propiedades del Sistema**:
     - Pulsa `Win + R`, escribe `sysdm.cpl` y presiona Enter.
   - Ve a la pestaña **Opciones avanzadas** y haz clic en **Variables de entorno**.
   - En la sección **Variables del sistema**, busca y selecciona la variable **Path**, y haz clic en **Editar**.
   - Haz clic en **Nuevo** y añade las rutas a Python y Scripts. Por ejemplo:
     ```
     C:\Users\[tu_usuario]\AppData\Local\Programs\Python\Python39\
     C:\Users\[tu_usuario]\AppData\Local\Programs\Python\Python39\Scripts\
     ```
   - Guarda y cierra todas las ventanas.

3. **Verificar la instalación de pip**:
   - Después de agregar las rutas al PATH, abre una nueva terminal o símbolo del sistema y escribe `pip --version` para verificar si ahora pip se reconoce.

4. **Reinstalar Python con la opción de añadir al PATH**:
   - Si los pasos anteriores no funcionan, considera reinstalar Python y asegúrate de seleccionar la opción "Add Python to PATH" durante la instalación.

5. **Usar el comando completo para pip**:
   - Como alternativa, puedes usar el comando completo para ejecutar pip:
     ```sh
     python -m pip install [paquete]
     ```

## ¡Listo!

Después de seguir estos pasos, deberías tener Python y pip instalados correctamente en tu sistema Windows. Si tienes alguna pregunta adicional o encuentras algún problema, no dudes en buscar ayuda en la [documentación oficial de Python](https://docs.python.org/3/).
