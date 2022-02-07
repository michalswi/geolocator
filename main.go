package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
)

var logger = log.New(os.Stdout, "web-server ", log.LstdFlags|log.Lshortfile|log.Ltime|log.LUTC)
var port = getEnv("SERVER_PORT", "8080")

func main() {
	http.HandleFunc("/", locate)
	logger.Println("Server is ready to handle requests at port", port)
	logger.Fatal(http.ListenAndServe(":"+port, nil))
}

func locate(w http.ResponseWriter, r *http.Request) {

	if r.Method == "GET" {
		http.ServeFile(w, r, "index.html")
	}

	var request []string

	// Request line
	url := fmt.Sprintf("%v %v %v", r.Method, r.URL, r.Proto)
	request = append(request, url)

	// Header
	request = append(request, fmt.Sprintf("Host: %v", r.Host))
	for name, headers := range r.Header {
		// name = strings.ToLower(name)
		for _, h := range headers {
			request = append(request, fmt.Sprintf("%v: %v", name, h))
		}
	}

	fmt.Println(strings.Join(request, "\n"))

	// Body
	if r.Method == "POST" {
		body, _ := ioutil.ReadAll(r.Body)
		fmt.Println(string(body))
	}

	fmt.Println()
}

func getEnv(key, defaultValue string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		return defaultValue
	}
	return value
}
