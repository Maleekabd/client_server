import hashlib, random, os, time
from binascii import hexlify
from socket import *
import ch9_crypto_chat as ct


def get_dh_sharedsecret():
    return


def get_dh_sharedKey():
    return


def encrypt(plaintext, usePKI, useDH, ClientSecret):
    msg = ct.decrypt(plaintext, usePKI, useDH, ClientSecret)
    return msg


def main():
    host = "127.0.0.1"
    port = 8080
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)

    sendUsingPrivate = False
    sendUsingDH = False
    skipEncryption = False

    ClientSecret = get_dh_sharedKey()
    print("welcome to crypto chat! \n")
    print()

    while True:
        if sendUsingPrivate == True or sendUsingDH == True:
            data = str(input("enter secure message to send or type exit : ")).encode()
        else:
            data = str(input("enter message to send or type exit : ")).encode()

        result = ct.check_client_command(data)
        if data == b"exit":
            break
        if result == 0:
            break

        ciphertext = encrypt(data, sendUsingPrivate, sendUsingDH, ClientSecret)

        if skipEncryption:
            ciphertext = data
            skipEncryption = False

        UDPSock.sendto(ciphertext, addr)

    UDPSock.close()
    os._exit(0)


if __name__ == "__main__":
    main()
