def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def main():
    print("enter the text to encript")
    text = input(">>> ")
    s = 4
    
    print("Plain Text : " + text)
    print("Shift pattern : " + str(s))
    print("Cipher: " + encrypt(text,s))

if __name__ == "__main__":
    main()