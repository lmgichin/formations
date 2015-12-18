#include <iostream>
#include <string>

using namespace std;


// *********************************************************************************************
// RAPPEL : pour faire du polymorphisme en C++, il FAUT 2 choses : 
//		- des fonctions virtuelles
//		- des pointeures ou des r�f�rences
// *********************************************************************************************
class Forme{

public:
	virtual ~Forme(void);
	virtual void affiche(void) const;			// le polymorhisme ne marchera que si on d�clare la m�thode virtual

};

class Carre__ : public Forme {

public:
	virtual ~Carre__(void);						// S'il y a au moins UNE fonction virtuelle, il FAUT que le destructeur soit
												// d�clar� VIRTUAL, sinon c'est le mauvais destructeur qui sera appel� 
	virtual void affiche(void) const;			// le polymorhisme ne marchera que si on d�clare la m�thode virtual
};


void Forme::affiche(void) const {

	cout << "Je suis une forme" << endl;

}
void Carre__::affiche(void) const {
	
	cout << "Je suis un carr� " << endl;
}

Forme::~Forme(void) {

	cout << "Destructeur de la Forme" << endl;
}

Carre__::~Carre__(void) {

	cout << "Destructeur du carr�" << endl;
}

void affiche(Forme &f) {		// le polymorphisme ne marchera que si on passe la r�f�rence de l'objet

	f.affiche();
}

void testPoly(void) {

	Forme f;
	Carre__ c;

	cout << "***" << endl << endl;
	affiche(f);
	affiche(c);

	Forme *pf = new Carre__;
	pf->affiche();
	delete pf;
	cout << "***" << endl << endl;

}