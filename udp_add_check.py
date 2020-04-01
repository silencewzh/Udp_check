import matplotlib.pyplot as plt
import numpy as np 

def add_binary(num1,num2):
    carry=0
    num1=num1[::-1]
    num2=num2[::-1]
    new_binary=""
    for index in range(len(num1)):
      sum=int(num1[index])+int(num2[index])+carry
      if (sum>1):
        carry=1
        sum-=2
        new_binary=new_binary+str(sum)
      else:
        carry=0
        new_binary=new_binary+str(sum)
    #溢出写反码 
    if (carry):
      temp=new_binary
      new_binary=""
      for index in range(len(temp)):
        if (int(temp[index])):
          new_binary=new_binary+str(0)
        else:
          new_binary=new_binary+str(1)
    
    new_binary=new_binary[::-1]
    return new_binary
#最后加起来验证是否全为1
def add_all(num1,num2):
    carry=0
    num1=num1[::-1]
    num2=num2[::-1]
    new_binary=""
    for index in range(len(num1)):
      sum=int(num1[index])+int(num2[index])+carry
      if (sum>1):
        carry=1
        sum-=2
        new_binary=new_binary+str(sum)
      else:
        carry=0
        new_binary=new_binary+str(sum)
  
    new_binary=new_binary[::-1]
    return new_binary

num1="0110011001100000"
num2="0101010101010101"
num3="1000111100001100"
sum1=add_binary(num1,num2)
final=add_binary(sum1,num3)
sum_all=add_all(final,add_all(num3,add_all(num1,num2)))
status="correct" if sum_all=="1111111111111111" else "false"
print("upd_check:",final)
print("sum_all:",sum_all)
print("finally",status)

num_show=[]

#将最后加和取出作为数组
for num in sum_all:
  num_show.append(int(num))

  
x = np.arange(0,16) 
y = num_show
plt.title("Udp_check") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,"ob") 
plt.show()