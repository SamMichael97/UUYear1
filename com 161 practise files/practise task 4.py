#Task 1
#Two words are anagrams if they contain all of the same letters, but in a different order. For example,
#Python and ‘Typhon, and ‘Study’ and ‘Dusty’ are anagrams. One way to determine if something is an
#anagram is to tally the individual letters that make up each word, and then to compare those tallies.
#Write and program that reads two words in from the keyboard, determines whether or not these are
#anagrams and produces a report detailing the character make-up of each word.


word1 = input('Enter your first word').lower()
word2 = input('Enter your second word').lower()

list1 = {}
list2 = {}

for letter in word1:
    if letter in list1:
        list1[letter] = int(list1[letter]) + 1
    else: 
        list1[letter] = 1

for letter in word2:
    if letter in list2:
        list2[letter] = int(list2[letter]) + 1
    else: 
        list2[letter] = 1

print(list1 == list2)
print(list1)
print(list2)
