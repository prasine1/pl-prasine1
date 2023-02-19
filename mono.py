import sys
import random
import string
def encrypt(inputfile, outputfile, seed):
    # Initialize the plaintext-ciphertext mapping
    mapping = {}
    alphanum = string.ascii_lowercase+"0123456789"
    char_list = list(alphanum)
    random.seed(seed)
    random.shuffle(char_list)
    for i, j in enumerate(alphanum):
        mapping[j] = char_list[i]
        print(j+"-"+char_list[i],end=", ")

    # Read the input file and write the encrypted output
    f_in = open(inputfile, "r")
    f_out= open(outputfile, "w")
    readline = f_in.read()
    encrypted = "".join([mapping[c] for c in readline])
    f_out.write(encrypted)
def decrypt(inputfile, outputfile, seed):
    # Initialize the ciphertext-plaintext mapping
    mapping = {}
    alphanum = string.ascii_lowercase+"0123456789"
    char_list = list(alphanum)
    random.seed(seed)
    random.shuffle(char_list)
    for i, j in enumerate(alphanum):
        mapping[char_list[i]] = j
    with open(inputfile, "r") as f_in, open(outputfile, "w") as f_out:
        readline = f_in.read()
        decrypted = "".join([mapping[c] for c in readline])
        f_out.write(decrypted)
def main(inputfile, outputfile, seed, mode):
    if mode == "1":
        print("ENCRYPTION")
        encrypt(inputfile, outputfile, seed)
    elif mode == "0":
        decrypt(inputfile, outputfile, seed)
if __name__ == "__main__":

    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
