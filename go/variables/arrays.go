package main

import "fmt"


func main(){

	// test avec des types array

	tab := [12]uint32 {8,9,7,5,2,7,5,2,3,6,4,5}
	var total uint32

	for i := 0; i < len(tab); i++{
		total += tab[i]
	}

	for i, value := range tab {
		fmt.Printf("Index = %d value = %d\n", i, value )
	}
	fmt.Printf("Total = %d\n", total)

	// tests avec des types slices

	var sl  []uint32

	fmt.Printf("Lg = %d\n", len(sl))
	sl = append (sl, 3, 4, 5)
	fmt.Printf("Lg = %d\n", len(sl))

	sl2 := make ([]float64, 5)
	sl2[1] = 3.14
	fmt.Println(sl2)

	sl3 := tab[1:5]
	fmt.Println(sl3)
	sl3 = append(sl3,99)
	fmt.Println(sl3)
	fmt.Println(tab[5])


	// tests avec map

	//var acro map[string]string
	acro := make(map[string]string)
	acro["LMA"] = "Luc Maignan"
	fmt.Println(acro["LMA"])

	value, res := acro["LMA"]
	fmt.Printf("Value = %s Return = %b\n", value, res)
	chaine := "Donnez du whisky à ce vieux juge qui fume..."
    stats  := make(map[uint8]int)

	for i :=0; i <len(chaine); {
		stats[chaine[i]] += 1
		i++
	}

	for key, value := range stats {
		fmt.Printf("'%c' -> %d\n", key, value)
	}


	acro2 := map[string]map[string]string {
		"LMA" : map[string]string {
				"NOM" : "Maignan",
				"PRENOM" : "Luc",
		},
	}

	acro2["VHU"] = map[string]string {
		"NOM" : "Hugo",
		"PRENOM" : "Victor",
	}


	if val, ok := acro2["VHU"]; ok {
		fmt.Printf("Nom  = %s Prenom = %s\n",val["NOM"], val["PRENOM"])
	}
}
