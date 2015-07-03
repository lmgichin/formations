#include <iostream>
#include <thread>
#include <mutex>
#include <string>
#include <vector>

using namespace std;

class Philosophe 
{

public:
	Philosophe(string);
	int GetNbRepas(void) { return m_repas; }
	void eat(void);
	
private:
	string m_name;
	static mutex mtx;
	int m_repas;
};

mutex Philosophe::mtx;

Philosophe::Philosophe(string name)
{
	m_name = name;
	m_repas = 0;
	cout << "Philosophe " << name << " created\n";
}

void Philosophe::eat(void)
{
	while (mtx.try_lock() == false)
	{
		cout << "Philosophe " << m_name << " is thinking... \n";
		this_thread::sleep_for(chrono::seconds(1));
	}
	cout << "Philosophe " << m_name << " is eating  #" << ++m_repas << "\n";
	this_thread::sleep_for(chrono::seconds(3));
	mtx.unlock();
	
}

void StartPhilo(string name)
{
	Philosophe philo(name);

	while (philo.GetNbRepas() != 5)
	{
		philo.eat();
		this_thread::sleep_for(chrono::seconds(1));
	}
}
void main(void)
{
	vector<thread> v;

	v.push_back(thread(StartPhilo, "Socrate"));
	v.push_back(thread(StartPhilo, "Platon"));
	v.push_back(thread(StartPhilo, "Aristote"));

	for (unsigned int i = 0; i < v.size(); i++)
		v[i].join();
}