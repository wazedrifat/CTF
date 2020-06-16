from eulerToientPhi import *
import time

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

def numToWord(n):
	hexvalue = hex(n)[2:]
	return "".join([chr(int(s, 16)) for s in [hexvalue[i:i+2] for i in range(0,len(hexvalue),2)]])

publicKey = int(input("public key : "))
mod = int(input("mod : "))
cypherText = int(input("cypherText : "))

startTime = time.time()
phi = eulerPhi(mod)
privateKey = modInv(publicKey, phi)
recoveredText = bigMod(cypherText, privateKey, mod)

print()
print("privateKey = ", privateKey)
print("recoveredText = ", recoveredText)
print(numToWord(recoveredText))

print()
second = int(time.time() - startTime)

if (second >= 3600):
	hour = second // 3600
	second %= 3600
	print(hour, "hour", end = " ")
if (second >= 60):
	minute = second // 60
	second %= 60
	print(minute, "minute", end = " ")
print(second, "second", end = " ")
