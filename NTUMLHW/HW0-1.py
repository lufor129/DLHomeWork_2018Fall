textfile = open("./words.txt","rt");
strArr = textfile.readline().split(" ");
dict = {}
for item in strArr:
    if(dict.get(item)):
        dict[item] = dict[item] + 1;
    else:
        dict[item] = 1;

arr=[]
for (item) in dict:
    arr.append([item,dict[item]]);

for index,element in enumerate(arr):
    print(element[0]+"  "+str(index)+"  "+str(element[1]));