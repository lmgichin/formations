#include <cstdlib>
#include <iostream>

using namespace std;


template <class T>
class stack_gene
{
	int nmax;   // nombre maximum de la valeur de la pile
	int nelem;	// nombre courant de valeurs de la pile
	T * adv;    // pointeur sur les valeurs


public:
	stack_gene(int = 20);		// constructeur
	~stack_gene();				// destructeur
	stack_gene & operator << (T);    // opérateur d'empilage
	stack_gene & operator >> (T	&);  // opérateur de dépilage
									 // (attention T &)
	int operator ++ ();			// opérateur de test pile pleine
	int operator -- ();			// opérateur de test pile vide
	friend ostream & operator <<(ostream &, stack_gene<T> &);
};

template <class T> 
stack_gene<T>::stack_gene(int n)
{
	nmax = n;
	adv = new T[nmax];
	nelem = 0;
}

template <class T> 
stack_gene<T>::~stack_gene()
{
	delete []adv;
}


template <class T> 
stack_gene<T> & stack_gene<T>::operator << (T n)
{
	if (nelem < nmax) 
		adv[nelem++] = n;
	
	return (*this);
}

template <class T> 
stack_gene<T> & stack_gene<T>::operator >> (T & n)
{
	if (nelem >	0) 
		n = adv[--nelem];

	return (*this);
}

template <class T> 
int stack_gene<T>::operator ++ ()
{
	return  (nelem == nmax);
}


template <class T> 
int stack_gene<T>::operator -- ()
{
	return (nelem == 0);
}

template <class T> 
ostream& operator << (ostream & sortie, stack_gene<T> & p)
{
	sortie << "// ";
	int i;
	for (i = 0; i < p.nelem; i++
		) sortie << p.adv[i] << " ";
		sortie << "//";
	return sortie;
}