#Added inventory logic using Enumerate and Short-hand If-Else
print("-------welcom to my startup store-------\n this is the products :")

products = {"lapto" : 20000 , "mouse": 500 , "keyboard": 700,  "monitor":3000, "cable":100}
for index, product in enumerate(products,start=1):
      print(f"{index}. {product} -rs {products [product]}")
num = int(input("Enter the product index that you want to buy : "))
print(f"------- Order Placed: {product} for Rs.{products[product]} -------") if 1 <= num <= len(products) else print("Invalid Selection")
