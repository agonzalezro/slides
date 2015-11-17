package main

import "fmt"

func output(whatever interface{}) { // HL
	switch v := whatever.(type) { // HL
	case string: // HL
		fmt.Println("A String: ", v)
	case int: // HL
		fmt.Println("Some int: ", v)
	default: // HL
		fmt.Println("I don't know what type is this one: ", v)
	}
}

func main() {
	output("this is some text")
	output(1)
	output(1.1)
}
