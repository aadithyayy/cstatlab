vowcount=0
constcount=0
wordcount=0
qcount=0

text=input("Enter string:")
wordcount=len(text.split())

for i in text:
    if i.isalpha():
        if i in "AEIOUaeiou":
            vowcount+=1
        else:
            constcount+=1
    elif i=="?":
        qcount+=1

print("Words:",wordcount)
print("Consonants:",constcount)
print("Vowels:", vowcount)
print("? marks:",qcount)