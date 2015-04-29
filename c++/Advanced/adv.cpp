#include <iostream>
#include <string>
#include <vector>

using namespace std;

void test_STL(void);

// ***********************************************************************************************
// Définition d'une fonction template
// ***********************************************************************************************

template <typename T>
const T & Max(const T &A, const T &B)
{
	return (A > B) ? A : B;
}

// ***********************************************************************************************
// Définition d'une classe template
// ***********************************************************************************************

template <class T>
class Stack {
private:
	vector<T> elems;     // elements 

public:
	void push(T const&);  // push element 
	void pop();               // pop element 
	T top() const;            // return top element 
	bool empty() const{       // return true if empty.
		return elems.empty();
	}
};

template <class T>
void Stack<T>::push(T const& elem)
{
	// append copy of passed element 
	elems.push_back(elem);
}

template <class T>
void Stack<T>::pop()
{
	if (elems.empty()) {
		throw out_of_range("Stack<>::pop(): empty stack");
	}
	// remove last element 
	elems.pop_back();
}

template <class T>
T Stack<T>::top() const
{
	if (elems.empty()) {
		throw out_of_range("Stack<>::top(): empty stack");
	}
	// return copy of last element 
	return elems.back();
}

// ***********************************************************************************************
// Génération d'exceptions
// ***********************************************************************************************

struct MyException : public exception
{
	const char * what() const throw ()				// throw() => la fonction ne lèvera jamais d'exception
	{
		return "C'est ma C++ Exception...";
	}
};

double divide(int a, int b) {

	if (b == 0) {
		//throw string("Divide by zero !!!");
		throw MyException();
	}

	return a / b;
}

void Test()
{
	try
	{
		throw std::logic_error("Exception de test");
	}
	catch (const std::logic_error & e)
	{
		std::cerr << "L'exception '" << e.what()
			<< "' a été levée et va être relancée.\n";
		throw; // relancer l'exception courante 
	}
}

void(*oldHandler)();

void MyTerminate(void) {

	cout << "New code of handled exceptions" << endl;
	(oldHandler)();
}
// ***********************************************************************************************


void main(void)

{

	// * Test exception 1

	try {
		cout << divide(2, 0) << endl;
	}
	catch (const string &msg) {
		cout << "Oups, exception : " << msg << endl;
	}
	catch (MyException &e) {
		cout << "Oups, exception : " << e.what() << endl;
	}

	// 

	try
	{
		Test();
	}
	catch (const std::logic_error & e)
	{
		std::cerr << "Erreur : " << e.what() << ".\n";
	}

	//

	oldHandler = set_terminate(MyTerminate);
	//throw ("test");

	// * Test template Max

	cout << "Max (1,2) = " << Max<int>(1, 2) << endl;
	cout << "Max ('abc','def') = " << Max<string>("abc", "def") << endl;

	// * Test class template

	try {
		Stack<int>    intStack;  // stack of ints 
		Stack<string> stringStack;    // stack of strings 

		// manipulate int stack 
		intStack.push(7);
		cout << intStack.top() << endl;

		// manipulate string stack 
		stringStack.push("hello");
		cout << stringStack.top() << std::endl;
		stringStack.pop();
		stringStack.pop();
	}
	catch (exception const& ex) {
		cerr << "Exception: " << ex.what() << endl;
	
	}

	// *** test de la STL
	test_STL();
}