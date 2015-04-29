#include <vector>
#include <deque>
#include <stack>
#include <map>
#include <iostream>

using namespace std;

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

}