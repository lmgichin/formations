#include <vector>
#include <deque>
#include <stack>
#include <map>
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

// Foncteur de somme
class Sommer
{
public:
	Sommer():m_somme(0)
	{}

	void operator()(int n)
	{
		m_somme += n;
	}

	int resultat() const
	{
		return m_somme;
	}

private:
	int m_somme;

};

// Foncteur affichage

class Afficher
{
public:
	void operator()(int a) const
	{
		cout << a << endl;
	}
};

// Foncteur de test pair

struct EstPair {

public:
	const bool operator()(int val){
		return (val % 2 == 0 );
	}
};

// Foncteur de génération incrémentale

class Remplir{
public:
	Remplir(int i):m_valeur(i)
	{}

	int operator()()
	{
		++m_valeur;
		return m_valeur;
	}

private:
	int m_valeur;
};

// Foncteur de génération aléatoire

class Generer
{
public:
	int operator()() const
	{
		return rand() % 10;  //On renvoie un nombre entre 0 et 9
	}
};

// Foncteur pour modifier l'ordre de tri d'une map 

class MapCompareLength {

public:
	bool operator()(const string& a, const string& b)
	{
		return a.length() < b.length();
	}
};


// *** Fonction de test de la STL

void test_STL(void) {

	// les vecteurs : <=> équivalent à une queue

	vector<int> t1(8,2),	// tableau de 8 éléments contenant 2
		t2(3, 5);			// tableau de 3 éléments contenant 5

	t1.push_back(7);	// ajout d'un élément en fin

	for (unsigned int i = 0; i < t1.size(); i++)
		cout << "Valeur " << i << " de t1 = " << t1[i] << endl;

	t2.pop_back();		// suppression du dernier élément

	for (unsigned int i = 0; i < t2.size(); i++)
		cout << "Valeur " << i << " de t2 = " << t2[i] << endl;

	t1.swap(t2);		// échange des deux tableaux

	cout << "Taille de t1/t2 : " << t1.size() << " " << t2.size() << endl;

	// les doubles queues

	deque<int> dq(2, 3);	// une queue à double sens de 2 éléments contenant 3

	dq.push_front(7);	// insertion du nombre 7 en tête

	for (unsigned int i = 0; i < dq.size(); i++)
		cout << "Valeur " << i << " de dq = " << dq[i] << endl;

	// les piles FILO (FIFO = queue)
	stack<int> pile;

	pile.push(1);	
	pile.push(2);

	cout << "En haut de la pile : " << pile.top() << endl;

	pile.pop();		// suppression de l'élément en haut de la pile
	cout << "En haut de la pile : " << pile.top() << endl;

	// les maps
	map<char, int> stats;
	map<char, int>::iterator it;
	string s = "Donnez du whisky à ce vieux juge qui fume";

	for (unsigned int i = 0; i < s.size(); i++)
		stats[s[i]]++;

	for (it = stats.begin(); it != stats.end(); it++)
		cout << "Valeur courante de map : " << it->first << " = " << it->second << endl;

	// tri des maps
	map<string, int> fruits;
	map<string, int, MapCompareLength> fruits2;
	map<string, int>::iterator iter;

	fruits["pomme"] = 3;
	fruits["raisin"] = 7;
	fruits["kiwi"] = 2;
	fruits["noix de coco"] = 1;
	fruits2["pomme"] = 3;
	fruits2["raisin"] = 7;
	fruits2["kiwi"] = 2;
	fruits2["noix de coco"] = 1;

	for (iter = fruits.begin(); iter != fruits.end(); iter++)
		cout << "Nombre de " << iter->first << " : " << iter->second << endl;

	for (map<string, int>::iterator it = fruits2.begin(); it != fruits2.end(); it++)
		cout << "Nombre de " << it->first << " : " << it->second << endl;

	// test algorithm

	vector<int> tab(100, 0);
	Remplir f(0);

	generate(tab.begin(), tab.end(), f);

	srand((unsigned int)time((time_t *)0));

	generate(tab.begin(), tab.end(), Generer());
	cout << "Nombre de 0 dans le tableau : " << count(tab.begin(), tab.end(), 0) << endl;
	cout << "Nombre de pairs dans le tableau : " << count_if(tab.begin(), tab.end(), EstPair()) << endl;
	sort(tab.begin(), tab.end());
	//for_each(tab.begin(), tab.end(), Afficher());
	Sommer somme = for_each(tab.begin(), tab.end(), Sommer());
	cout << "La somme des éléments générés est : " << somme.resultat()<< endl;

}
