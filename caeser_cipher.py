logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ||     `   88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `     "Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    )8  ||        88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdPPY8 88   
 
                                                     
           88             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP-----88 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(text1,shift1,direction1):
  end_text = ''
  for letter in text1:
    letter_value = ord(letter)
    if 97<=letter_value<=122:
      if direction1=='encode':
        new_letter_val = (letter_value - ord('a') + shift1) % 26
        code='encrypted'
      elif direction1=='decode':
        new_letter_val = (letter_value - ord('a') - shift1) % 26
        code='decrypted'
      end_text += chr(new_letter_val+ord('a'))
    else:
      end_text+=letter
  print(f"The {code} message is: {end_text}")
  
caeser(text,shift,direction)

while True:
  choice=input("\nType 'yes' if you want to go again otherwise type 'no' \n").lower()
  if choice=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)
  else:
    break
