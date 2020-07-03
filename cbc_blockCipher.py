def blockCipher(plaintext,IV,key):
    initVector = IV
    P_ASCII = []
    CIPTEXT = []
    for i in range(len(plaintext)):
        P_ASCII.append(ord(plaintext[i]))
    # Applying the CBC mode block cipher 
    for i in range(len(P_ASCII)):
        if(i==0):
            CIPTEXT.append(((P_ASCII[i]^IV)*key)%256);
        else:
            CIPTEXT.append(((P_ASCII[i]^CIPTEXT[i-1])*key)%256);


    print("Plain Text: "+ plaintext)
    print("ASCII Form of Plain Text: ")
    for item in P_ASCII:
        print(item, end=" ")
    print("\n")

    print("Cipher text generated from Plain Text (Integer Representation): ")

    for item in CIPTEXT:
        print(item, end=" ")
    print("\n")
    print("Cipher text generated from Plain Text (Binary Representation): ")

    for item in CIPTEXT:
        print(bin(item)[2:].zfill(8), end=" ")
    print("\n")
    return CIPTEXT
    
########### main() ###############################
def main():
    cipherText = blockCipher("hello",201,197)


if __name__ == "__main__":
    main()

