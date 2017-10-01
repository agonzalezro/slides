package main

import "fmt"

type Company struct {
	name      string
	employees int
}

func main() {
	bbva := Company{
		name:      "BBVA",
		employees: 132000,
	}
	fmt.Println(bbva.employees)
}
