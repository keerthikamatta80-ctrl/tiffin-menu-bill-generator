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
  order=input('enter the tiffen').lower()
   
  if order=='exit':
     break
  if order in menu:
   quantity=int(input('enter the quantity'))
   b=menu[order]*quantity
   print(quantity)
   print(b)
   total+=b
  else:
    print('sorry, the item is not avaliable')
print(total)