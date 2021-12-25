"""
https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/

"""
# Python 3.x code to demonstrate star pattern
# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ",end="")
	
		# ending line after each row
		print("\r")

# Python 3.x code to demonstrate star pattern
# Function to demonstrate printing pattern
def pypart2(n):
	myList = []
	for i in range(1,n+1):
		myList.append("*"*i)
	print("\n".join(myList))


# Python 3.x code to demonstrate star pattern
# Function to demonstrate printing pattern
def pypart3(n):
	
	# number of spaces
	k = 2*n - 2

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 2
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	# initialising starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		num = 1
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def contnum(n):
	
	# initializing starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# not re assigning num
		# num = 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
	# 5 in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# explicitly converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
	
		# incrementing number
		num = num + 1
	
		# ending line after each row
		print("\r")

# Python code 3.x to demonstrate star pattern
# Function to demonstrate printing pattern of alphabets
def contalpha(n):	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows   
	for i in range(0, n):
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# explicitly converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
		
			# incrementing at each column
			num = num +1

		# ending line after each row
		print("\r")


# Driver Code
n = 5
pypart(n)
pypart2(n)
pypart3(n)

triangle(n)
numpat(n)

# calling Function
contnum(n)

alphapat(n)

contalpha(n)
