---
title: "Data Professor and Streamlit"
day: "1"
publishDate: "2021-06-21"
thumbnailImage: "../images/day-76.png"
shareText: " Description: Streamlit es un libreria open-source de python para hacer mas sencillo crear paginas web para machine learning y ciencia de datos. "
hashtags: ['learn', 'Python', 'Streamlit', 'Data Science']
draft: false

---

# Como construir  `Data Science Web App` con `Python` - `Streamlit` 

| Source:      | [streamlit docs](https://docs.streamlit.io/en/stable/#) |
| ------------ | ------------------------------------------------------- |
| **Course:**  | [Channel youtuber](https://youtu.be/ZZ4B0QUHuNc)        |
| **Teacher:** | Data professor Youtuber                                 |



## Notes

### Primeros pasos :coffee:

`Streamlit` es un librería `open-source` de `Python` creada con el objetivo de hacer mas sencilla la creación de paginas web para `machine learning` y ciencia de datos.

Es necesario tener `Python` versión 3.6 - 3.8

1. Crearemos una carpeta `streamlit-apps` y dentro de esta carpeta crearemos un `entorno virtual` para trabajar con `streamlit`.

```bash
# Crear entorno virtual
virtualenv -p python3 .   
```

2. Luego  de crear nuestro entorno virtual de trabajo debemos activarlo.
``` Bash
source bin/activate 
```

3. Con nuestro entorno activado procedemos a instalar la librería `streamlit` para nuestros proyectos. Ejecutamos la librería para comprobar su correcto funcionamiento. 
```bash
pip install streamlit
streamlit hello
```

4. Creamos un archivo `first_app.py` 

```python
# Agregamos las siguientes importaciones
import streamlit as st
# Numpy y Pandas son impresindibles para trabajar con datos.
import numpy as np
import pandas as pd


# Los comentarios de una linea son iguales.
# Con los comentarios de mas de una linea podemos usar markdown
# Ejemplo: 

'''
# Esto es un titulo h1 con markdown
:+1:
:100:
Probamos la sintaxis _markdown_.
'''

'Creamos un dataframe y lo dibujamos'
df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Dibujamos el dataframe como en los notebooks

'Hola a todo el mundo **En es string normales funciona el markdown**'
'Asiganmos valor a una variable `x = 10`'
x = 10

'x', x  # <-- Dibujamos el string 'x' y luego el valor de x

'La coma de la linea anterior es parte de la sintaxis!'
```

5. Ejecutamos nuestra nueva aplicación: :100:

```bash
# Puedes pasar una URL, muy util con github gists
streamlit run first_app.py  
```

```
CTRL + C # Nos permite cancelar la app toda la vida
```

[Documentación sobre la `API` de `Streamlit`](https://docs.streamlit.io/en/stable/api.html)

- `Emoji shortcodes`, como son :+1: y  :sunglasses:. Para una lista de todos los códigos soportados, ver https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json.
- `LaTeX`  “$” or “$$” (the “$$” usado en una sola linea). Todas las funciones `LaTeX` soportadas , ver  https://katex.org/docs/supported.html.

