package main

import "fmt"

// ***
// Programme de test des chaines de caractères
// ***

func main(){

	fmt.Println("Test de chaine")
	fmt.Printf("Longueur de chaine = %d\n",len("Test de chaine"))
	fmt.Println("Premier caractère : " + string("Test de chaine"[0]))
	fmt.Println("5 premiers caractères : " + string("Test de chaine"[0:4]))
	fmt.Println("Les autres : " + string("Test de chaine"[5:]))
}

