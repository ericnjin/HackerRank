string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

#Create a store list to store count of each character
store = [0]*26

for alpha in string:
    store[ord(alpha)-97] += 1
#count odd alphas
odd = 0

for item in store:
    if item%2 !=0:
        odd +=1
if odd <= 1:
    found = True
    
if not found:
    print("NO")
else:
    print("YES")
