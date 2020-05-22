def isPrime(num):
 list=[];
 for i in range(1,num-1):
  list.append(i+1)
 #print(list)
 if (num==2):
     print('Es primo')
 for j in range(len(list)):
  if (num%list[j]==0):
     print('No es primo')
     break
  else:
      print('Es primo')
      break