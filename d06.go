package main

import (
	"fmt"
	"github.com/dbabiak/aoc-2020/utils"
	"strings"
)

func d6parse(lines []string) [][]string {
	groups := [][]string{}
	group := []string{}
	for _, line := range lines {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			groups = append(groups, group)
			group = []string{}
		} else {
			group = append(group, line)
		}
	}
	if len(group) > 0 {
		groups = append(groups, group)
	}
	return groups
}

func runeset(s string) map[rune]bool {
	m := map[rune]bool{}
	for _, c := range s {
		m[c] = true
	}
	return m
}

// number of answer questions
func d6p1(groups [][]string) int {
	n := 0
	for _, group := range groups {
		answeredQs := runeset(group[0])
		for _, answer := range group[1:] {
			for _, c := range answer {
				answeredQs[c] = true
			}
		}
		n += len(answeredQs)
	}
	return n
}

func d6p2(groups [][]string) int {
	n := 0
	for _, group := range groups {
		commonAnswers := runeset(group[0])
		for _, answer := range group[1:] {
			for k, _ := range commonAnswers {
				if !strings.ContainsRune(answer, k) {
					commonAnswers[k] = false
				}
			}
		}
		for _, v := range commonAnswers {
			if v {
				n += 1
			}
		}
	}
	return n
}

func main() {
	lines := utils.PathToLines("data/d06.txt")
	groups := d6parse(lines)
	fmt.Printf("%v\n", d6p1(groups))
	fmt.Printf("%v\n", d6p2(groups))
}
