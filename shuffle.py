import random
fid = open("task_data.csv", "r")
li = fid.readlines()
fid.close()
print(li)

random.shuffle(li)
print(li)

fid = open("data.csv", "w")
fid.writelines(li)
fid.close()
