package main

import "fmt"

func somme(x, y int32, res *int32) {

	*res = x  + y
}

func modArray( ch *[5]int) {

	(*ch)[1] = 7
}

func main () {

	// pointeurs d'entiers
	var a,b,x int32

	a,b = 2,3
	somme (a,b, &x)

	fmt.Printf("Somme = %d\n", x)

	// via un new

	sm := new(int32)
	somme (a,b,sm)
	fmt.Printf("Somme = %d\n", *sm)


	// pointeurs d'array

	var tab [5]int
	modArray ( &tab )
	fmt.Printf( "Array = %v\n", tab)
}
