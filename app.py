import os

def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def CharShifter(text_char, key, forward=True):
    char = ''
    char_order = 0
    if forward:
        char_order = ord(text_char) + key
    else:
        char_order = ord(text_char) - key
    if (char_order <= ord('Z')) and (char_order >= ord('A')):
        char = chr(char_order)
    elif char_order > ord('Z'):
        char = chr(ord('A') + (char_order % (ord('Z') + 1)))
    elif char_order < ord('A'):
        char = chr(ord('Z') - (ord('A') - char_order) + 1)
    return char

def Encryption():
    planeText = input('Plane text: ').upper().replace(' ', '')
    key = int(input('Key number: '))
    cipher = ''
    for i in range(len(planeText)):
        cipher += CharShifter(planeText[i], key, True)
    print(cipher)

def Decryption():
    cipher = input('Cipher text: ').upper().replace(' ', '')
    key = int(input('Key number: '))
    planeText = ''
    for i in range(len(cipher)):
        planeText += CharShifter(cipher[i], key, False)
    print(planeText)
    
    
def main():
    while True:
        print('Enter \'e\' for Encryption')
        print('Enter \'d\' for Decryption')
        char = input('Application mode: ').lower()
        ClearConsole()
        if char == 'd':
            print('Decryption')
            print('==========\n')
            Decryption()
            exit(0)
        elif char == 'e':
            print('Encryption')
            print('==========\n')
            Encryption()
            exit(0)

if __name__ == "__main__":
    main()