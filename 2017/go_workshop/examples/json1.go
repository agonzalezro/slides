package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type Person struct {
	Name string `json:"name"` // HL
}

func main() {
	var sentPeople = []Person{Person{"Rai"}, Person{"Alex"}} // HL
	payload, err := json.Marshal(sentPeople)                 // HL
	if err != nil {
		log.Panic(err) // Don't do this at home
	}

	fmt.Println(string(payload))

	var receivedPeople []Person
	if err := json.Unmarshal(payload, &receivedPeople); err != nil { // HL
		log.Panic(err)
	}

	for _, p := range receivedPeople {
		fmt.Println(p.Name) // HL
	}
}
