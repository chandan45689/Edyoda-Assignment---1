#Write a Python program that accepts a word from the user and reverse it.

word=input("Enter a word:")
b=""
for i in range(len(word)):
    b=word[i]+b


print("The reversed word is:",b)
