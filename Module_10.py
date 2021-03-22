from matplotlib import pyplot as plt
x = [1, 3, 1, 3]
y = [7, 7, 3, 3]
plt.subplot(1, 2, 1)
plt.plot(x, y)

x1 = [1, 2, 3, 1]
y1 = [3, 5, 3, 3]
plt.subplot(1, 2, 2)
plt.plot(x1, y1)

plt.show()

#2


from plotnine.data.diamonds import price
from plotnine import ggplot

ggplot(price)
