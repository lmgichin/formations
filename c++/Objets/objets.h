#include <iostream>

// Classe Point V1

class PointV1 {

public:
	int mX, mY;
};

// classe Rectangle

class Rectangle{

public:
	static int count;

	Rectangle(){}

	Rectangle(int lg, int la) : mLongueur(lg), mLargeur(la) {
		std::cout << "Constructeur Rectangle " << mLongueur << " " << mLargeur << std::endl;
		count++;
	}
	
	~Rectangle();
	int Aire() {
		return mLongueur * mLargeur;
	}

	void SetLargeur(int largeur);
	void SetLongueur(int longueur);
	friend void GetValue(Rectangle);
	int Compare(Rectangle);
	
protected:
	int mLongueur,
		mLargeur;

};

int Rectangle::count = 0;

void Rectangle::SetLargeur(int largeur) {
	mLargeur = largeur;
}

void Rectangle::SetLongueur(int longueur) {
	mLongueur = longueur;
}

Rectangle::~Rectangle(void) {

	std::cout << "Destruction du Rectangle" << std::endl;
}

int Rectangle::Compare(Rectangle r2) {

	return this->Aire() - r2.Aire();
}

void GetValue(Rectangle r) {

	std::cout << "Valeurs des attributs : " << r.mLargeur << " " << r.mLongueur << std::endl;
}


// *************************************************************************

class Carre : public Rectangle {

public:

	Carre(int cote);
	Carre() {}
	Carre operator+ (const Carre&);


};

Carre::Carre(int cote) {

	this->SetLargeur(cote);
	this->SetLongueur(cote);
}

Carre Carre::operator+(const Carre &c2) {

	Carre c(this->mLongueur + c2.mLongueur);

	return c;
}

// *************************************************************************************
// Classes de tests des fonctions virtuelles
// *************************************************************************************

class A {

public:

	void F1(void)  { std::cout << "A::F1" << std::endl; }
	virtual void F2(void) { std::cout << "A::F2" << std::endl; }
};

class B : public A {

public:

	void F1(void)  { std::cout << "B::F1" << std::endl; }
	void F2(void) { std::cout << "B::F2" << std::endl; }
};
