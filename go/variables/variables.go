package main

import "fmt"

// ***
// Programme de test de déclarations de variables
// ***

func main() {

	var ch string
	var ch2 string = " et l'autre..."

	i := 1
	i += 1
	i ++
	ch = "Ceci est ma chaine"
	fmt.Printf("Variable chaine = %s\nEntier = %d\n", ch+ch2, i)

	readData()

	{var (
		i = 7
		c string
		k = 0

	)
		fmt.Println(i, c, k)

	}

	a,b,c,d := 1,2,3,4
	fmt.Printf("%d %d %d %d\n", a,b,c,d)
}

func readData() {
	fmt.Print("Enter a number: ")
	var input float64
	fmt.Scanf("%f", &input)
	output := input * 2
	fmt.Printf("Le double est : %.2f\n",output)

	const imm = 3.14
	fmt.Printf("%2f",imm)

}
