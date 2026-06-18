menu={
  'dosa':30,
  'idly':30,
  'puri':25,
  'pongal':20,
  'vada':20,
  'breadomllet':30, 
}
total=0
while True:
  #hello
  order=input('enter the tiffens').lower()
   
  if order=='exit':
     break
  if order in menu:
   quantity=int(input('enter the quantity'))
   b=menu[order]*quantity
   print(quantity)
   print(b)
   total+=b
  else:
    print('sorry, the item is not avaliables')
print(total)