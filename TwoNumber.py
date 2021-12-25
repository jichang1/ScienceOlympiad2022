
def sum(a, b):
    return a+b

def product(a, b):
    return a * b

def inputnumber():
  a = int(input("enter first number: "))
  b = int(input("enter second number: "))
  return a, b

a, b = inputnumber()
print("sum:{}\n".format(sum(a, b)))
print("product:{}\n".format(product(a, b)))