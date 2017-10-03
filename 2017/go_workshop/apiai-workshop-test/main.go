package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type Request struct {
	Result struct {
		Parameters struct {
			GivenName string `json:"given-name"`
		}
	}
}

type Response struct {
	Speech string `json:"speech"`
}

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	var req Request
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	resp := Response{
		Speech: "Hi " + req.Result.Parameters.GivenName,
	}
	bs, err := json.Marshal(resp)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
	}
	w.Write(bs)

}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/", HomeHandler)

	addr := ":8080"
	log.Println("Listening on " + addr)
	log.Println(http.ListenAndServe(addr, r))
}
