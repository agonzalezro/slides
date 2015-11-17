package main

import (
	"fmt"
	"log"
	"math/rand"
	"time"
)

func doit(i int, done chan bool) {
	time.Sleep(time.Duration(rand.Intn(3)) * time.Second)
	fmt.Println(i)
	done <- true // HL
}

func main() {
	done := make(chan bool, 1) // HL

	for i := 0; i < 10; i++ {
		go doit(i, done) // HL
	}

	for i := 0; i < 10; i++ {
		select { // HL
		case <-done: // HL
			continue
		case <-time.After(time.Second * 3): // HL
			log.Println("Too... much... waiting...")
			return
		}
	}
}
