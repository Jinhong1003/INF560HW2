# from a import create_number
import a
l2 = []
l1=a.l1
for items in l1:
    a = 3 * items + 6
    l2.append(a)
filename = open('b_output.doc', 'w')
for value in l2:
    filename.write(str(value)+",")
filename.close()
if __name__ == '__main__':
    print(l2)
