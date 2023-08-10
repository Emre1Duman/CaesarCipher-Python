from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(start_text, shift_amount, cipher_direction):
  end_text = ""
  for char in start_text:
    if char in alphabet: #Checks to see if every charcter of the word is in the list
      position = alphabet.index(char)
      if cipher_direction == "encode":
        new_position = position + shift_amount
      elif cipher_direction == "decode":
        new_position = position - shift_amount
      end_text += alphabet[new_position]
    elif char not in alphabet: #If the user enters a number/symbol/space it is kept within the final encrypted word
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
  

print(logo)
endgame = False
while endgame == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 #Shifting large numbers down to fit in the alphabet
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    go_again = input("Type 'yes if you want to go again. Otherwise type 'no'.\n").lower()
    if go_again == "no":
       endgame = True #Breaks the loop
       print("Goodbye...")

#Slightly different method:
  # end_text = ""
  # if cipher_direction == "decode":
  #   shift_amount *= -1
  # for char in start_text:
  #   if char in alphabet:
  #       position = alphabet.index(char)
  #       new_position = position + shift_amount
  #       end_text += alphabet[new_position]
  #   elif char not in alphabet: #If the user enters a number/symbol/space it is kept within the final encrypted word
  #      end_text += char