package main

import "fmt"

type Shoper interface { // HL
	LikesFashion() bool // HL
}
type (
	CarShoper  struct{}
	ShoeShoper struct{}
)

func (s CarShoper) LikesFashion() bool { // HL
	return false
}

func (s ShoeShoper) LikesFashion() bool { // HL
	return true
}

func IsPossibleShopaClient(s Shoper) bool { // HL
	return s.LikesFashion()
}

func main() {
	fmt.Println(IsPossibleShopaClient(CarShoper{}), IsPossibleShopaClient(ShoeShoper{}))
}
