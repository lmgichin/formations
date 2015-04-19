#include <iostream>
#include <string>

using namespace std;


int ext_val = 7;

// affichage des nombres premiers entre 2 et max


void printPrime(int max) {

	bool br;

	for (int i = 2; i <= max ; i++ ) {

		br = false;

		for (int j = 2; j < i; j++ ) {

			if (i % j == 0 ){
				br = true;
				break;
			}

		}

		if ( br == false )
			cout << i << " est un nombre premier" << endl;
		
	}
}

// test chaine de caractères

void testString_c(void) {

	char str1[11] = "Hello";
	char str2[] = "World";
	char str3[10];
	int  len;

	// copy str1 into str3
	strcpy_s(str3, str1);
	cout << "strcpy( str3, str1) : " << str3 << endl;

	// concatenates str1 and str2
	strcat_s(str1, str2);
	cout << "strcat( str1, str2): " << str1 << endl;

	// total lenghth of str1 after concatenation
	len = strlen(str1);
	cout << "strlen(str1) : " << len << endl;

}

void testString_cpp(void) {

	string str1 = "Hello";
	string str2 = "World";
	string str3;
	int  len;

	// copy str1 into str3
	str3 = str1;
	cout << "str3 : " << str3 << endl;

	// concatenates str1 and str2
	str3 = str1 + str2;
	cout << "str1 + str2 : " << str3 << endl;

	// total lenghth of str3 after concatenation
	len = str3.size();
	cout << "str3.size() :  " << len << endl;
}

// inversion de paramètres avec passage par pointeur

void swap(int *x, int *y) {

	int t = *x;
	*x = *y;
	*y = t;

}

// inversion de paramètres avec passage par référence

void swap(int &x, int &y) {

	int t = x;
	x = y;
	y = t;

}

// retour d'une référence

int &ref(int idx, int tab[]) {

	return tab[idx];
}