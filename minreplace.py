# Python3 program to find minimum 
# replacements in a string to 
# make adjacent characters unequal 

# Function which counts the minimum 
# number of required operations 
def count_minimum(s):
	
	# n stores the length of the string s 
	n = len(s)

	# ans will store the required ans 
	ans = 0
	
	# i is the current index in the string 
	i = 0
	
	while i < n:
		j = i
		
		# Move j until characters s[i] & s[j] 
		# are equal or the end of the 
		# string is reached 
		while j < n and (s[j] == s[i]):
			j += 1
		
		# diff stores the length of the 
		# substring such that all the 
		# characters are equal in it 
		diff = j - i
		
		# We need atleast diff/2 operations 
		# for this substring 
		ans += diff // 2
		i = j
		
	print(ans)
	
# Driver code
if __name__=="__main__":
	
	str = "xxxxxx"
	count_minimum(str)
	
# This code is contributed by rutvik_56
