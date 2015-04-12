package main

import "fmt"


type Shaper interface {

	area() int
}


type Rectangle struct {
	length, width int
}

type Carre struct {
	cote int
}

func (r Rectangle) area() int {

	return r.length * r.width
}

func (c Carre) area() int {

	return c.cote * c.cote
}

func main () {

	r := Rectangle {length : 5, width : 3}

	fmt.Println("Details de r : ", r)
	fmt.Println("Aire de r : ", r.area())

	s := Shaper(r)
	fmt.Println("Aire de S : ", s.area())
	c := Carre {5}
	s = c
	fmt.Println("Aire de S : ", s.area())

	objArr := []Shaper{r,c}

	for i,_ := range(objArr) {
		fmt.Println("Aire de l'objet", objArr[i].area())
	}
}
