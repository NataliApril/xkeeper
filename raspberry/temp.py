import re 
  
# initializing string 
test_str = "GeeksforGeeks is best for Geeks"
  
# initializing substring 
test_sub = "noy"
  
# printing original string 
print("The original string is : " + test_str) 
  
# printing substring 
print("The substring to find : " + test_sub) 
  
# All occurrences of substring in string 
res = [i.start() for i in re.finditer(test_sub, test_str)] 
  
# printing result 
print("The start indices of the substrings are : " + str(res)) 