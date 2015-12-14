package main

import (
	"fmt"
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
		<-done // HL
	}
}
