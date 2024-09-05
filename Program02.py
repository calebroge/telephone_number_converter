# Program02.py
# Caleb Roge


# Step 1. Prompt user to enter in a telephone number
phone_word = input("Enter a phone number: ")
phone_number = "1-800-"

# Step 2. Process the phone number if it has letters or numbers

def digit(letter):
    """convert letters to numbers"""
    
    if letter == 'a' or letter == 'A' or letter == 'b' or letter == 'B' or letter == 'c' or letter == 'C':
        return '2'
    elif letter == 'd' or letter == 'D' or letter == 'e' or letter == 'E' or letter == 'f' or letter == 'F':
        return '3'
    elif letter == 'g' or letter == 'G' or letter == 'h' or letter == 'H' or letter == 'i' or letter == 'I':
        return '4'
    elif letter == 'j' or letter == 'J' or letter == 'k' or letter == 'K' or letter == 'l' or letter == 'L':
        return '5'
    elif letter == 'm' or letter == 'M' or letter == 'n' or letter == 'N' or letter == 'o' or letter == 'O':
        return '6'
    elif letter == 'p' or letter == 'P' or letter == 'q' or letter == 'Q' or letter == 'r' or letter == 'R' or letter == 's' or letter == 'S':
        return '7'
    elif letter == 't' or letter == 'T' or letter == 'u' or letter == 'U' or letter == 'v' or letter == 'V':
        return '8'
    elif letter == 'w' or letter == 'W' or letter == 'x' or letter == 'X' or letter == 'y' or letter == 'Y' or letter == 'z' or letter == 'Z':
        return '9'
    else:
        return (letter)

phone_number = phone_number + digit(phone_word[6])
phone_number = phone_number + digit(phone_word[7])
phone_number = phone_number + digit(phone_word[8])
phone_number = phone_number + '-'
phone_number = phone_number + digit(phone_word[9])
phone_number = phone_number + digit(phone_word[10])
phone_number = phone_number + digit(phone_word[11])
phone_number = phone_number + digit(phone_word[12])
        
# Step 3. Output the phone number digit

print(f"The digits are: {phone_number}")
