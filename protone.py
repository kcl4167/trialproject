#!/usr/bin/env python3
quote = input("Enter the size of product: ")
rate = int(input("Enter the price rate: "))
size = quote.split('*')
price = int(size[0]) * int(size[1]) * int(size[2]) * rate /1000000
print("The price is: ", price)

