import a
import b
import matplotlib.pyplot as plt
plt.plot(a.l1,b.l2,'s-',color = 'r',label="Visualization")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc = "best")
plt.savefig('c_output.png')
plt.show()
