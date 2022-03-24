#was to enter 5 string in a list and check and print string whose length has even number od character.(without any string function) Do this script using UDF.

def createList():
    l=[]
    for i in range(5):
          s=input("Enter string");
          l.append(s)

def countEven(l):
    count=0
    for i in l:
        for j in i:
          if(i%2==0):
            count+=1
    return(count)

createList()
ans=countEven(l)
print(ans)
