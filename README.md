# Morse_Code

Morse Code is one of two methods that uses a combination of dots, dashes, and spaces to represent alphabetic characters, numbers, and punctuation.
The algorithm is quite basic. Every letter of the English alphabet is replaced by a succession of dots and dashes, or occasionally just a single dot or dash, and vice 
versa.


#Encryption 

1.When encrypting a message, each character from a word is extracted one at a time, and its matching morse code is compared with a data structure.
2.We first add a space to our string that will hold the result before storing the morse code in a variable that will hold our encoded string.


#Decryption

1.For decryption, we begin by adding a space to the end of the string that has to be unlocked.
2.As of right now, we continue removing characters from the string until we run out of spaces.
3.As soon as we encounter a space, we seek for the English character that corresponds to the characters that were extracted and add it to a variable that will hold the outcome.
