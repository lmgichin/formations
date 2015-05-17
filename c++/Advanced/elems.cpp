#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Element
{
	int     Number;
	string  Symbol;
	string  Name;

	Element()
		: Number(0)
		, Symbol()
		, Name()
	{
	}

	bool operator()(const Element & lhs, const Element &rhs)
	{
		return lhs.Symbol < rhs.Symbol;
	}

	void print ( void )
	{
		Element elem = *this;

		cout << elem.Number << "  " << elem.Symbol << "  " << elem.Name << endl;
	}
};

template <class T>
class Liste
{
public:
	void add(const T &data)
	{
		vect.push_back(data);
	}

	void affiche(void)
	{
		for_each(vect.begin(), vect.end(), [](T &elem)
		{
			elem.print();
		} );
	}

	void sort(void)
	{
		T elt;

		std::sort(vect.begin(), vect.end(), elt );
	}

private:
	vector<T> vect;
};

void testElems(void)
{
	Liste<Element> maliste;

	Element el;
	el.Name = "Or";
	el.Number = 23;
	el.Symbol = "Au";

	maliste.add(el);

	el.Name = "Argent";
	el.Symbol = "Ag";
	el.Number = 192;
	maliste.add(el);
	maliste.sort();
	maliste.affiche();
}