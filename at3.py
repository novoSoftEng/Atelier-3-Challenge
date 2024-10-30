import random

def custom_hash(input_string, mapping_string, fixed_size):
    # Step 1: Reverse the string
    reversed_string = input_string[::-1]

    # Step 2: Shuffle the string deterministically based on its length
    length = len(reversed_string)
    random.seed(length)  # Set the seed for reproducibility
    shuffled_string = ''.join(random.sample(reversed_string, length))

    # Step 3: Map each character to another character in mapping_string
    mapped_string = ''.join(mapping_string[ord(char) % len(mapping_string)] for char in shuffled_string)

    # Step 4: Ensure fixed output size
    if len(mapped_string) > fixed_size:
        return mapped_string[:fixed_size]  # Trim if too long
    elif len(mapped_string) < fixed_size:
        return mapped_string.ljust(fixed_size)  # Pad if too short
    else:
        return mapped_string

# Example usage
input_string = "Hello World fjezfjzenfzef;,nn  ee,kjefzekfejn ;?JFAZNJRAZMKDNl,;rbmj*:1"
mapping_string = "ABCDEFGHIJKLMNO125478963PQRSTUVWXYZ/*+$£=+}ç_"
fixed_size = 16

hashed_output = custom_hash(input_string, mapping_string, fixed_size)
print(hashed_output)


hashed_output = custom_hash("Hello World jezfjzenfzef;,nn  ee,kjefzekfejn ;?JFAZNJRAZMKDNl,;rbmj*:1", mapping_string, fixed_size)
print(hashed_output)
