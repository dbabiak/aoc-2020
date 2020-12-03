package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

const input = `
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
`

func part1(lines []string) int {
	valid := 0

	for _, line := range lines {
		var lo, hi int
		var letter rune
		var password string
		_, err := fmt.Sscanf(line, "%d-%d %c: %s", &lo, &hi, &letter, &password)
		if err != nil {
			log.Fatal(err)
		}
		if n := strings.Count(password, string(letter)); lo <= n && n <= hi {
			println(line)
			valid += 1
		}
	}
	return valid
}

func main() {
	fp, err := os.Open("data/d02.txt")
	check(err)

	scanner := bufio.NewScanner(fp)
	lines := []string{}
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	println(part1(lines))
}

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}