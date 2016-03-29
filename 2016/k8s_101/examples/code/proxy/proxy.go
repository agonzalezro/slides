package main

import (
	"flag"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

var targetHost string

func proxyHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("GET 'proxy' request to /")
	log.Printf("Proxying to '%s'...", targetHost)

	resp, err := http.Get(targetHost)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write(b)
}

func main() {
	flag.Parse()

	if len(flag.Args()) < 1 {
		log.Println("target host needed as argument!")
		os.Exit(-1)
	}
	targetHost = flag.Args()[0]

	http.HandleFunc("/", proxyHandler)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	log.Printf("Listening on address :%s", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
