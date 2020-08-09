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
    print("enter the encripted ver")
    text = input(">> ")
    for i in range(26):
        print("Shift pattern : " + str(i))
        print("Cipher: " + encrypt(text,i))

if __name__ == "__main__":
    main()