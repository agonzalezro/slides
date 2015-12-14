package main

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		go fmt.Println(i) // HL
	}
	// Something is going to go wrong...
}
