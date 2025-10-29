try:
    filename=input("Enter filename: ")
    file=open(filename,"r")

    text=file.read()

    charcount=len(text)
    wordcount=len(text.split())
    sentencecount=0

    for i in text:
        if i in "?.!":
            sentencecount+=1

    print("Characters: ",charcount)
    print("Words:", wordcount)
    print("Sentences: ",sentencecount)

except FileNotFoundError:
    print("File doesn't exist.")