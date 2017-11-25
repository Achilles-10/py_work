import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x ** 3 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, s=50,
            edgecolors='none')
plt.title("Cubic Numbers", fontsize=28)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0,5000,0,125000000000])

plt.show()
