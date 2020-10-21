import random
def create_number():
    random.seed(10)
    l1=[]
    while len(l1)<1000:
        l1.append(random.randint(0,100))
    return(l1)
l1=create_number()
filename = open('a_output.doc', 'w')
for value in l1:
    filename.write(str(value)+",")
filename.close()
if __name__ == '__main__':
    print(l1)
