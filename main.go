package main

import (
	"fmt"
	"os/exec"
)

func main() {
	//fmt.Println("hello world")
	cmd := exec.Command("bash", "-c", "python3 web.py 'is Friday prayer mandatory for women and sick person ?' ")
	out, err := cmd.Output()

	if err != nil {
		println(err.Error())
		return
	}

	fmt.Println(string(out))
}
