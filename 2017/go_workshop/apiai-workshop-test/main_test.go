package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http/httptest"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func payloadFromFixture(name string) ([]byte, error) {
	path := fmt.Sprintf("fixtures/%s.json", name)
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	return ioutil.ReadAll(f)
}

func TestMyNameIsAlex(t *testing.T) {
	assert := assert.New(t)

	payload, err := payloadFromFixture("myNameIsAlex")
	assert.NoError(err)

	w := httptest.NewRecorder()
	r := httptest.NewRequest("POST", "/", bytes.NewReader(payload))

	HomeHandler(w, r)

	var resp Response
	err = json.NewDecoder(w.Body).Decode(&resp)
	assert.NoError(err)
	assert.Equal(resp.Speech, "Hi Alex")
}
