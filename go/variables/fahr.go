package main

import "fmt"

func main(){

	var temp uint32

	fmt.Printf("Entrez la valeur en farenheit : ")
	fmt.Scanf("%d", &temp)
	fmt.Printf("La valeur en degrés est : %d\n", (temp-32)*5/9)

	fmt.Printf("Entrez la valeur en degrés : ")
	fmt.Scanf("%d", &temp)
	fmt.Printf("La valeur en farenheit est : %d\n", ((temp*9/5) +32))
}
