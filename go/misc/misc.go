package main

import "fmt"


func main() {

	defer func () {
		str := recover()
		fmt.Printf("Oups... j'ai récupéré l'erreur : %s\n", str)
	}()

	fmt.Println("Début du programme...")
	panic ("Une erreur s'est produite !!!")
	fmt.Println("Fin du programme...")
}
