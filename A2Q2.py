#Write a Python program to count the number of even and odd integers from a series of numbers.


list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=0
odd=0
for i in list:
    if i % 2==0:
        even=even+1
    else:
        odd=odd+1
print("Number od even numbers:",even)
print("Number of odd numbers:",odd)
        

