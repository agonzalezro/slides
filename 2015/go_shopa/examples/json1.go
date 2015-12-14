package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type Person struct {
	Name string
}

func main() {
	payload := []byte(`[{"name":"Alex"},{"name":"Nicola"}]`) // HL

	var people []Person
	if err := json.Unmarshal(payload, &people); err != nil { // HL
		log.Panic(err) // Don't do this at home
	}

	for _, p := range people {
		fmt.Println(p.Name) // HL
	}
}
