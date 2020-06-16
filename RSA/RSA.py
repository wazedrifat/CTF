import time
from factorise import *

def eulerPhi(n):
	res = 1
	fac = factorise(n)
	prev = -1

	for i in fac:
		if (i != prev):
			prev = i
			n /= i
		res *= i - 1

	res *= int(n)
	return int(res)

def bigMod(n : int, p : int, mod : int):
    res = 1 % mod
    x = n % mod
    
    while (p > 0):
        if (p&1):
            res = (res * x) % mod
            
        x = (x * x) % mod;
        p >>= 1
    
    return res

def ext_GCD(a, b):
	if (b <= 0):
		return (a, 1, 0)
	
	d = ext_GCD(b, a%b)
	x, y = d[2], d[1] - (d[2] * (a // b))

	return (d[0], x, y)
    
def modInv(a, mod):
	x = ext_GCD(a, mod)
	ret = x[1] % mod

	if (ret < 0):
		ret += mod	
	return ret

publicKey = int(input("public key : "))
mod = int(input("mod : "))

# factorise(mod)
# eulerPhi(mod)

cypherText = int(input("cypherText : "))

startTime = time.time()
phi = eulerPhi(mod)
print("phi = ", phi)
print("time : ", time.time() - startTime)

privateKey = modInv(publicKey, phi)
print()
print("privateKey = ", privateKey)

check = (privateKey * publicKey) % phi
print("check = ", check)

recoveredText = bigMod(cypherText, privateKey, mod)
print("recoveredText = ", recoveredText)


hexRecoveredText = hex(recoveredText)
print("hex : ", hexRecoveredText)
print("string : ", bytearray.fromhex(str(hex)).decode())
