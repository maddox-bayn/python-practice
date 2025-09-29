first_name = "Maddox"
last_name = "Emmanuel"

print(f"hello, {first_name} {last_name}. nice to meet you") 


#program loop with the if $ for(continue) 
user_word = ("gregory:")
user_word = user_word.upper()
word_without_vowels = ""   
for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels  += letter
print("word without vowels:", word_without_vowels)  