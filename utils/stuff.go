package utils

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func PathToLines(pathname string) []string {
	f, err := os.Open(pathname)
	Check(err)
	lines := []string{}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func Lines(s string) []string {
	return strings.Split(strings.TrimSpace(s), "\n")
}

func Check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
