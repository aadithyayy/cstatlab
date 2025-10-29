fruits=("Apple","Banana","Kiwi","Dragonfruit","Orange")
text=input("Enter item:")

if text.title() in fruits:
    print("Yes!, would you like one?")
else:
    print("Not in here.")