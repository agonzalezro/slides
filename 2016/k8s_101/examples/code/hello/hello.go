package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		log.Println("GET 'hello jt' request to /")
		fmt.Fprintf(w, "Hello jt!")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	log.Printf("Listening on address :%s", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
