import hashlib, random, os, time
from binascii import hexlify
from socket import *
import ch9_crypto_chat as ct


def get_dh_sharedsecret():
    return


def get_dh_sharedKey():
    return


def decrypt(ciphertext, usePKI, useDH, serverSecret):
    try:
        msg = ct.decrypt(ciphertext, usePKI, useDH, serverSecret)
    except:
        msg = ciphertext
    return msg


def main():
    useClientPKI = False
    useDHKey = False
    serverSecret = 0

    key = ""
    host = ""
    port = 8080
    buf = 1024 * 2
    addr = (host, port)

    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)

    print("Waiting to receive message...")

    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        plaintext = decrypt(data, useClientPKI, useDHKey, serverSecret)

        result = ct.check_server_command(plaintext)
        if result == 10:
            plaintext = b"PKI Encryption disabled"
        elif result == 11:
            plaintext = b"PKI Encryption enabled"
        elif result == 20:
            ClientKey = plaintext
        elif result == 21:
            plaintext = b"Diffie Hellman Enabled"

        msg = str(plaintext, "utf-8")

        if result == 0:
            break
        if useClientPKI == True or useDHKey == True:
            print("Received secured message : ", msg)
        else:
            print("received message: ", msg)

    UDPSock.close()
    os._exit(0)


if __name__ == "__main__":
    main()
