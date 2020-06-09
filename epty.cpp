#include <bits/stdc++.h>
using namespace std;

#define IN freopen("in.txt", "r", stdin);
#define OUT freopen("out.txt", "w", stdout);
#define LL long long int
#define MX 500001
#define max3(a, b, c) max(a, max(b, c))
#define min3(a, b, c) min(a, min(b, c))
#define max4(a, b, c, d) max(a, max3(b, c, d))
#define min4(a, b, c, d) min(a, min3(b, c, d))
#define EPS 1e-9
#define MOD 1000000007
#define PI 2.0 * acos(0.0)
#define PII pair <int, int>
#define VI vector <int>
#define VVI vector <VI>

bool flag[MX];
vector<int> prime;
void SieveOfEratosthenes(int limit = MX)
{
	prime.clear();
	flag[0] = flag[1] = 1;

	prime.push_back(2);

	for (int i = 4; i <= limit; i += 2)
		flag[i] = 1;

	for (int i = 3; i * i < limit; i += 2)
		if (flag[i] == 0)
			for (int j = i * i; j <= limit; j += 2 * i)
				flag[j] = 1;

	for (int i = 3; i <= limit; i += 2)
		if (flag[i] == 0)
			prime.push_back(i);
}

//	Euler Phi Function : count of numbers <= N 
//	that are coPrime with N
//	Number of elements e, such that gcd(e,n)=d is equal to ϕ(nd).
//	∑of (d/n)  [ ] = n.
int eulerPhi(int n) {
	int res = n, sqrtn = sqrt(n);

	for (int i = 0; i < prime.size() && prime[i] <= sqrtn; i++) {
		if (n % prime[i] == 0) {
			while (n % prime[i] == 0)
				n /= prime[i];

			sqrtn = sqrt(n);
			res /= prime[i];
			res *= prime[i] - 1;
		}
	}

	if (n != 1) {
		res /= n;
		res *= n - 1;
	}
	return res;
}

//	returns (n^p) % mod
int bigMod(int n, int p, int mod ) {
	int res = 1%mod, x = n%mod;

	while (p) {
		if (p&1)
			res = (res * x) % mod;
		
		x = (x * x) % mod;
		p >>= 1;
	}
	return res;
}

//	x = (1/a) % mod
int modInv(int a, int mod) {	//	mod is prime
	return bigMod(a, mod - 2, mod);
}

int main() {
	IN OUT		//ThisIsForDebuggingPurposes
	
	SieveOfEratosthenes();

	LL publicKey, text, mod;

	cout << "enter public text : ";
	cin >> text;

	cout << "enter public key : ";
	cin >> publicKey;

	cout << "enter mod : ";
	cin >> mod;

	LL code = bigMod(text, publicKey, mod);
	LL privateKey = modInv(publicKey, eulerPhi(mod));
	// privateKey = 37;
	cout << "code = " << code << endl;		//ThisIsForDebuggingPurposes
	cout << "privateKey = " << privateKey << endl;		//ThisIsForDebuggingPurposes

	LL recoveredText = bigMod(code, privateKey, mod);
	cout << "recoveredText = " << recoveredText << endl;		//ThisIsForDebuggingPurposes
}