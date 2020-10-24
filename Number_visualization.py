import Create_number
import New_number
import matplotlib.pyplot as plt
plt.plot(Create_number.l1,New_number.l2,'s-',color = 'r',label="Visualization")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc = "best")
plt.savefig('c_output.png')
plt.figure()
plt.show()
