import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Niemcy", "Francja", "Włochy", "Hiszpania", "Polska", "Rumunia", "Holandia", "Belgia", "Grecja", "Czechy", "Portugalia", "Szwecja", "Węgry", "Austria", "Bułgaria", "Dania", "Finlandia", "Słowacja", "Irlandia", "Chorwacja", "Litwa", "Słowenia", "Łotwa", "Estonia", "Cypr", "Luksemburg", "Malta"])
y = np.array([3134,2228,1672,1113,424,169,421,175,174,184,462,112,349,47,276,214,80])

plt.bar(x, y, color = "#4CAF50")
plt.show()
