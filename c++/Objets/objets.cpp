#include "objets.h"
#include <iostream>

using namespace std;


// ***************************************************************************************************
// surcharge de l'opérateur << pour un Point
// ***************************************************************************************************

ostream &operator<< (ostream &flux, PointV1 pt) {

	flux << "Valeurs du point : X = " << pt.mX << " Y = " << pt.mY;
	return flux;

}
// *

void main(void) {

	// Test classe Point


	PointV1 pt;

	pt.mX = 5;
	pt.mY = 6;

	cout << "Val x = ";

	cout << "Point (" << pt.mX << "," << pt.mY << ")" << endl;
	cout << pt << endl;

	// Test classe Rectangle

	Rectangle r(4,5);
	r.SetLargeur(7);
	r.SetLongueur(10);

	cout << "Aire r = " << r.Aire() << endl;

	// copy constructeur

	Rectangle rc(r);

	cout << "Aire rc = " << rc.Aire() << endl;

	// fonction friend

	GetValue(r);

	// test de "this"

	Rectangle r2(10, 10);
	cout << "Comparaison = " << r.Compare(r2) << endl;

	// pointeurs sur classes

	Rectangle *pr = &r;

	GetValue(*pr);

	pr = new Rectangle(5, 2);
	GetValue(*pr);
	delete pr;

	// variables de classes

	cout << "Nombre de rectangles : " << Rectangle::count << endl;


	// héritage

	Carre c(5), c2(7), c3;

	GetValue(c);
	cout << "Aire de carre : " << c.Aire() << endl;

	c3 = c + c2;
	cout << "Aire de carre : " << c3.Aire() << endl;

	// Test fonctions virtuelles
	A a;
	B b;

	a.F1();
	a.F2();
	b.F1();
	b.F2();

	A *pa = &b;
	pa->F1();
	pa->F2();
}

