import matplotlib.pyplot as plt
from pathlib import Path

results = Path('results')

x_values = range(1,5001)
y_values = [value**3 for value in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.inferno, s=15)
#Inferno sounds wicked cool

ax.set_title("Cubed Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

plt.savefig(results / "cubes.png")
#I use savefig instead of show since I am working in WSL