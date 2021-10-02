def iswordpresent(sentence, word):
    s = sentence.split(" ")
    for i in s:
        if (i == word):
            return True
    return False
s = input("write your sentence:")
word = input("which question phrase you are searching:")
if (iswordpresent(s,word)):
    print("yes")
else:
    print("no")