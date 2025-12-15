#prints out every second letter of a word

word = str(input("Enter a word where every second letter of the word should be printed out: "))

numb = len(word)

for i in range(numb):
    if i+1 % 2 == 0:
        print(word[i])

#OR: range(0, numb-1,2)
# --> no modulo needed