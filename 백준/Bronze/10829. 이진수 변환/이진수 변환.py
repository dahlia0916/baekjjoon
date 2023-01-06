import sys
dec = int(sys.stdin.readline())
def dec2bin(dec):
    bin = ''
    while not (dec == 0 or dec == 1):
        r = dec % 2
        bin = str(r) + bin
        dec = dec // 2
    bin = str(dec) + bin
    return bin
print(dec2bin(dec))