package main

import (
	"fmt"
)

type Person struct {

	nom string
	prenom string
	age uint16
}


func modPers ( p *Person) {

	p.age += 7
}

func agePers ( p Person) uint16 {

	return p.age
}

func ( p Person) agePersMeth()  uint16 {

	return p.age
}

type Physical interface {
	agePersMeth() uint16
}

func getAge ( p ...Physical) uint16{
	return p.agePersMeth()
}

func main() {

	ar := Person {nom : "Rimbaud", prenom : "Arthur", age : 23}
	var p Person

	p.nom = "Hugo"
	p.prenom = "Victor"
	p.age = 46

	fmt.Printf("Personnes : %v %v\n", p, ar)

	modPers(&ar)
	fmt.Printf("Personnes : %v %v\n", p, ar)

	pp := new(Person)
	pp.nom = "inconnu"
	modPers(pp)
	fmt.Printf("Personnes : %v\n", *pp)

	fmt.Printf("Les ages sont : %d %d %d\n", agePers(p),agePers(ar), agePers(*pp) )
	fmt.Printf("Les ages sont : %d %d %d\n", p.agePersMeth(),ar.agePersMeth(), (*pp).agePersMeth() )
	fmt.Printf("Les ages sont : %d\n", getAge(&p) )
}
