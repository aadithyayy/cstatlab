text=input("Enter string:")
stack=[]
for i in text:
    if i in "{([":
        stack.append(i)
    elif i=="}" and stack[-1]=="{":
        stack.pop()
    elif i==")" and stack[-1]=="(":
        stack.pop()
    elif i=="]" and stack[-1]=="[":
        stack.pop()

if len(stack)==0:
    print("okey!")
else:
    print("nahh!")