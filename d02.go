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

func part1(entries []*Entry) int {
	valid := 0

	for _, entry := range entries {
		if n := strings.Count(entry.word, string(entry.letter)); entry.lo <= n && n <= entry.hi {
			println(entry)
			valid += 1
		}
	}
	return valid
}

type Entry struct {
	lo     int
	hi     int
	letter rune
	word   string
}

func parse(line string) *Entry {
	entry := Entry{}
	_, err := fmt.Sscanf(line, "%d-%d %c: %s", &entry.lo, &entry.hi, &entry.letter, &entry.word)
	check(err)
	return &entry
}

func main() {
	fp, err := os.Open("data/d02.txt")
	check(err)

	scanner := bufio.NewScanner(fp)
	entries := []*Entry{}
	for scanner.Scan() {
		entries = append(entries, parse(scanner.Text()))
	}

	println(part1(entries))
}

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
