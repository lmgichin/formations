package main

import "fmt"

// ***
// fonction main
// ***

func main() {

	fmt.Println(average([]float64{9,8,7,5,21,4,2}))
	fmt.Println(getPi())

	if tot, bn := averageNotNull([]float64{1,2}); bn {
		fmt.Printf ("Total non nul : %.2f\n", tot)
	}


	fmt.Println(addInts(1,2,3,4,5))
	fmt.Println(addInts([]int{1,2,3}...))

	testClosure()

	genEven := makeEven()
	fmt.Println(genEven())
	fmt.Println(genEven())
	fmt.Println(genEven())
	fmt.Println(genEven())
	fmt.Println(genEven())
	fmt.Println(genEven())

}

// ***
// fonction de calcul de moyenne d'un slice de flottants
// ***

func average (xs []float64) float64 {

	total := 0.0

	for _, value := range xs {
		total += value
	}

	return total / float64(len(xs))
}

// ***
// fonction avec paramètre de retour nommé
// ***

func getPi() (vr float64) {

	vr = 3.14
	return
}

// ***
// fonctions avec multiples paramètres de retour
// ***

func averageNotNull(xs []float64) (float64, bool) {

	total := average(xs)

	return total, total != 0.0
}

// ***
// Fonction avec nombre d'arguments variable
// ***

func addInts(args ...int) int {

	tot := 0

	for _, v := range args {
		tot += v
	}

	return tot
}


// ***
// closure
// ***

func testClosure() {

	x := 0

	incr := func () int {
		x++
		return x
	}

	fmt.Println(incr())
	fmt.Println(incr())
	fmt.Println(x)
}

// ***
// générateur de nombres pairs
// ***

func makeEven() func() uint {

	i := uint(0)

	return func() (ret uint){
		ret = i
		i += 2
		return
	}
}
