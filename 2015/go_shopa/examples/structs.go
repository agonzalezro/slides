package main

import "fmt"

type Shopa struct {
	employees int
}

func main() {
	s := Shopa{
		employees: 2,
	}
	fmt.Println(s.employees)
}
