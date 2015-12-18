package main

import "fmt"

func main(){

	var br bool

	for i:= 2; i<= 100;i++ {

		br = false

		for j := 2; j < i; j++ {

			if i % j == 0 {
				br = true
				break
			}


		}

		if br == false {
			fmt.Printf("%d est un nombre premier\n", i)
		}
	}
}
