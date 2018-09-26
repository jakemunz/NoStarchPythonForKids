# EncoderDecoder.py Takes in a message, uppercases then shift letter value 13 places
message = input("Enter a message to encode or decode: ") # Get a message
message = message.upper()       # Make it all UPPERCASE
output = ""                     # Empty string to hold the output
for letter in message:          # Loop through each letter in the message
    if letter.isupper():
        value = ord(letter) + 13  # Shifts letter 13 places
        letter = chr(value)       # turn the value back into a letter
        if not letter.isupper():  # check to see if we shifted too far
            value -= 26           # wrap back around Z -> A
            letter = chr(value)   # subtracting 26 from letter value
    output += letter              # Add the letter to our output string
print("Output message: ", output) # Output for our coded/decoded message
           
