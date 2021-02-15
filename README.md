# module 5
#1.
multiplication = 'print("module #5 assignment")'
code = """
def multiply(x,y):
	  return x*y

print ('the sum of the multiplication of 5 and 20 is: ',multiply(5,20))
"""
exec(multiplication)
exec(code)

#2.
def insert_string(str, word):
 return str[:2] + word + str[2:]

print(insert_string('{{}}', 'SQL'))
print(insert_string('<<>>', 'Github'))
print(insert_string('[[]]', 'Python'))