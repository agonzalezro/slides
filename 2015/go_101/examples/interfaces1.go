package main

import "fmt"

type Developer interface { // HL
	LikesDevelopment() bool // HL
}
type (
	GoodDev      struct{}
	MercenaryDev struct{}
)

func (MercenaryDev) LikesDevelopment() bool { // HL
	return false
}

func (GoodDev) LikesDevelopment() bool { // HL
	return true
}

func CouldWorkHere(d Developer) bool { // HL
	return d.LikesDevelopment()
}

func main() {
	fmt.Println(CouldWorkHere(GoodDev{}), CouldWorkHere(MercenaryDev{}))
}
