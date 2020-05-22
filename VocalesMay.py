vowels = ['a','A','e','E','i','I','o','O','u','U']
text=input('Ingresar la palabra: ')
for i in text:
  for j in vowels:
    if i in j:
      print(i.upper())