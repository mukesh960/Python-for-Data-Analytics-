# Write code here
#take a  cost and selling price  from user
cp=int(input("Enter a cost price of  Product: "))
sp=int(input("EnEnter a selling price of  Product: "))

#to find  profit and loss
if cp>sp:
  print("loss ",sp-cp)
elif sp>cp:
 print("profit ",sp-cp)

 # cost price and selling price are same
else: 
  print("No profit and No loss")