user_word = ("Gregory:")
user_word = user_word.upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter, end="") 

magicians = ("Alice", "David", "Maddox")
for magician in magicians:
  print(magician)