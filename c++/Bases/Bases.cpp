#include <iostream>

using namespace std;


int i;

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

void main(void) {

	fct();

	cout << i << endl;

	::func();			// appel de la fonction du main
	ns::func();			// appel de la fonction de ns
	ns::ns2::func();	// appel de la fonction de ns2
	
	
}