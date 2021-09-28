from resources import logo, morse_dict

playOn = True
print(logo)

while playOn:
    message = (input("Type out your message: ")).lower()
    result = ""

    for char in message:
        if char in morse_dict:
            result = result + morse_dict[char] + '  '
        else:
            result = result + char + '  '

    print(result)
    if (input("Got another? Y/N ")).lower() == 'n':
        print("See ya.")
        playOn = False
