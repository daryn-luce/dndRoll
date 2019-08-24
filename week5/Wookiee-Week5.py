#Week 5's Project:
#Input a string and return the string reversed. for instance if the string is "Hello, World!" return "!dlroW ,olleH"

#Bonus points: just reverse the words, not the sentence. For instance return ",olleH !dlroW"

#Hints:
#There are two ways to do this. you can loop though the string and add to a
#new string = character + newstring
#or do string manipulation string[-1]

print("Please enter a sentence")
Text = input()

Reverse = (Text[::-1])
def ReverseWordText(Sentence):
    return ' '.join(word[::-1] for word in Text.split(" "))

print("Original String: " + Text)
print("Reverse String: " + Reverse)
print("Reverse Words String: " + ReverseWordText(Text))
