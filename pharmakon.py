from drug import Drug, Interact, Receptors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import phargui as pg
from phargui import Start





modafinil = Drug("Modafinil", "Stimulant", 200, 1, 12)
alcohol = Drug("Alcohol", "Depressant", 10, 0, 5)
seroxat = Drug("Seroxat", "Stimulant", 20, 1, 5)

df = pd.read_csv("Drug_Database.csv")
df = df.dropna()





"""

df = pd.read_csv("Drug_Database.csv", delimiter = ',')
df = df.dropna()

"""








        
