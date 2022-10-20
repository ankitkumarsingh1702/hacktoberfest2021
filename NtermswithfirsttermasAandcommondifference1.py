# Python3 program to implement
# the above approach

# Function to count all possible
# AP series with common difference
# 1 and sum of elements equal to N
def countAPs(N) :
	
	# Stores the count of AP series
	count = 0

	# Traverse through all factors of 2 * N
	i = 1
	while(i * i <= 2 * N) :

		res = 2 * N
		if (res % i == 0) :

			# Check for the given conditions
			op = res / i - i + 1

			if (op % 2 == 0) :

				# Increment count
				count += 1
			if (i * i != res
				and (i - res / i + 1) % 2 == 0) :
				count += 1	
		i += 1

	# Print count - 1
	print(count - 1)


# Driver Code

# Given value of N
N = 963761198400

# Function call to count
# required number of AP series
countAPs(N)

