import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("pressure.csv")
kp = df["KP (m)"]
p = df["Pressure (Pa)"]
x = []
y = []
x = list(p/1000000)
y = list(kp)
plt.plot(x, y)
plt.xlabel('Pressure (MPa)->')
plt.ylabel('KP (m)->')
plt.show()
