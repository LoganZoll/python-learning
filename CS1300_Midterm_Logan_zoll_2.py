#Asks the user for a multi-word sentence
user_string=input("Please enter a multi-word sentence: ")


#Prints the number of characters
number_of_characters=len(user_string.strip())
print(f"Total number of characters: {number_of_characters}")


#Prints the number of words
number_of_words=len(user_string.split(" "))
print(f"Total number of words: {number_of_words}")


#Prints the number of vowels
number_of_vowels=0
vowels =  ['a','e','i','o','u']
for i in range(0,4):
    number_of_vowels+=user_string.count(vowels[i])
print(f"Total number of vowels: {number_of_vowels}")


#Prints the number of consonants
number_of_consonants=number_of_characters-number_of_vowels
print(f"Total number of consonants: {number_of_consonants}")


#Prints the average word length
average_word_length=0
words=user_string.split()
for i in words:
    average_word_length+=len(i)
average_word_length/=len(words)
print(f"Average length of words: {average_word_length}")


#Prints the longest word
longest_word=""
for i in words:
    if(len(i)>len(longest_word)):
        longest_word=i
print(f"Longest word: {longest_word}")