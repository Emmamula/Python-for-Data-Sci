multiplication = 'print("module #5 assignment")'
code = """
def multiply(x,y):
	  return x*y

print ('the sum of the multiplication of 5 and 20 is: ',multiply(5,20))
"""
exec(multiplication)
exec(code)


cars = ['mustang', 'GTR', 'R8']
cars.insert(1, "gsxr 1000")
print(cars)