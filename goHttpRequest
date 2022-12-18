ckage main

import (
"fmt"
"io/ioutil"
"net/http"
"os"
)

func main() {
if len(os.Args) < 2 {
fmt.Println("Usage: go run main.go <url>")
os.Exit(1)
}

url := os.Args[1]

res, err := http.Get(url)
if err != nil {
	fmt.Println("Error making request:", err)
	os.Exit(1)
}
defer res.Body.Close()

body, err := ioutil.ReadAll(res.Body)
if err != nil {
	fmt.Println("Error reading response:", err)
	os.Exit(1)
}

fmt.Println(string(body))
}
