def string_reverse(str1):

    reverse = ''
    i = len(str1)
    while i> 0:
        reverse += str1[ i - 1 ]
        i = i - 1
    return reverse
str1=input("enter string to be reversed\n")
print("reverse of a string is\n",string_reverse(str1))







#a=str(input("Enter a string: "))
#print("Reverse of the string is: ")
#print(a[::-1])