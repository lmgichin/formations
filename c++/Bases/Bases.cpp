#include <iostream>

using namespace std;


int i;						// variable globale
const int INTCONST = 3;
extern int ext_val;
void printPrime(int);
void testString_c(void);
void testString_cpp(void);

namespace ns {
	
	void func(void) {

		cout << "Fonction dans ns " << endl;
	}

	namespace ns2 {

		void func(void) {

			cout << "Fonction dans ns2 " << endl;
		}
	}
}


void fct(void) {

	int i;

	i = 7;     // affectation de la variable locale
	::i = 3;   // affectation de la variable globale
}

using namespace ns;

void func(void) {

	cout << "Fonction du main " << endl;

}

void printCount(void)

{
	static int count = 3;

	cout << "Compteur = " << count++ << endl;
}

int sum(int a = 1, int b = 1) {

	return a + b;
}

void main(void) {

	fct();

	cout << i << endl;

	::func();			// appel de la fonction du main
	ns::func();			// appel de la fonction de ns
	ns::ns2::func();	// appel de la fonction de ns2

	// Test de variable locale static

	for (int i = 0; i < 5; i++)
		printCount();
	
	// Test de variable externe

	cout << "Var ext = " << ext_val << endl;

	// nombres premiers

	printPrime(100);

	// valeurs par défaut de fonctions

	cout << "Somme = " << sum() << endl;

	// test String
	testString_c();
	testString_cpp();

}