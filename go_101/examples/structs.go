package main

import "fmt"

type jobAndTalent struct {
	employees int
}

func main() {
	jt := jobAndTalent{
		employees: 2,
	}
	fmt.Println(jt.employees)
}
