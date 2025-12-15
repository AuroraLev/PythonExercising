print("Write down a sentence, any sentence: ")

usersentence = str(input())

print("Now write down which word you want to find the number of occurrences of: ")

userword = str(f" {input()} ")

n = usersentence.count(f"{userword}")
    
print(f"Number of occurrences of the word {userword} in your sentence is: {n}")