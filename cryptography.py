def machine():
    keys = 'abcdefghijklomnoqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys, value))
    decryptDict = dict(zip(value, keys))

    message = input("Please Eenter Your Secret Message: ")
    mode = input("Please Enter The Mode- Encode(E) Or Decode(D): ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])

    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])

    else:
        print("Please Enter A Correct Choice")

    return newMessage.capitalize()

print(machine())
