package main

import (
	"errors"
	"log"
)

var NamedError = errors.New("Is this an exception?") // HL

func breakSomething() error {
	return NamedError // HL
}

func main() {
	err := breakSomething()
	switch err {
	case NamedError: // HL
		log.Println("Failed as expected")
	default: // HL
		log.Panic("I didn't expect this!")
	}

	if err := breakSomething(); err == NamedError { // HL
		log.Println("This failed as expected as well!")
	}
}
