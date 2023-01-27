def palindrome(string):
    if string==string[::-1]:
        return("The string is a palindrome")
    else:
        return("The string is not a palidrome")
    
string = input("Enter the string : ")
print (palindrome(string))
