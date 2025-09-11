#!/usr/bin/env python

import matplotlib.pyplot as plt
x1 = 2
x2 = 10
y1 = 2
y2 = 10

plt.plot([x1, x2], [y1, y2])
plt.show()
plt.title('A simple line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()