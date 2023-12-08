fr = open('text.txt', 'r')
text = fr.read()
fr.close()

word1 = ""
word2 = ""
while True: 
    word1 = input("Enter the first word: ")
    if word1.strip() == "":
        print("Wrong word! Try again")
    else:
        break
while True: 
    word2 = input("Enter the second word: ")
    if word2.strip() == "":
        print("Wrong word! Try again")
    else:
        break



newtext = text.replace(word1.strip(), word2.strip())

fw = open("text.txt", "w")
fw.write(newtext)
fw.close()

print("Everything is done!")