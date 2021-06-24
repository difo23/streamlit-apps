import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# Draw a title and some text to the app:
'''
# This is the document title
:+1:
:100:
This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

":+1"
'Hola a todo el mundo **En `string` normales funciona el markdown**'

"100"
x = 10

'x', x  # <-- Draw the string 'x' and then the value of x

'La coma de la linea anterior es parte de la sintaxis!'
