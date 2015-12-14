package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type Person struct {
	Name string
}

// START OMIT
func fill(queue chan<- Person, wg *sync.WaitGroup) { // HL
	defer close(queue)
	defer wg.Done()
	for _, name := range []string{"Mihai", "Victor", "Francesc", "Germán", "Alex"} {
		queue <- Person{name} // HL
		time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
	}
}

func visit(queue <-chan Person, wg *sync.WaitGroup) { // HL
	defer wg.Done()
	for p := range queue { // HL
		fmt.Println(p.Name, "is visiting")
	}
}

func main() {
	queue := make(chan Person, 2) // HL
	// ...
	// END OMIT

	var wg sync.WaitGroup
	wg.Add(2)

	go fill(queue, &wg)
	go visit(queue, &wg)

	wg.Wait()
}
