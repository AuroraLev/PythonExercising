def remove_chars(word,n):
    if len(word) < n:
        return print("Either word is too small or n is too large. Try again!")
    else:
        return word[n:len(word)]
        
strInput = str(input())
intInput = int(input())

print(remove_chars(strInput,intInput))