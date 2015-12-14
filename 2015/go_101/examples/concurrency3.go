package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup // HL

	for i := 0; i < 10; i++ {
		wg.Add(1) // HL
		go func(i int) {
			fmt.Println(i)
			wg.Done() // HL
		}(i)
	}

	wg.Wait() // HL
}
