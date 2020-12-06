package main

import (
	"fmt"
	"github.com/dbabiak/aoc-2020/utils"
)

func findRowCol(s string) (int,int) {
	rowDirs := s[:7]
	colDirs := s[7:]
	lo := 0
	hi := 127
	mid := (lo + hi) / 2
	for _, x := range rowDirs {
		if x == 'F' {
			hi = mid
		} else {
			lo = mid + 1
		}
		mid = (lo + hi) / 2
	}
	row := mid

	lo = 0
	hi = 7
	mid = (lo + hi) / 2
	for _, x := range colDirs {
		if x == 'L' {
			hi = mid
		} else {
			lo = mid + 1
		}
		mid = (lo + hi) / 2
	}
	col := mid

	return row, col
}

func d5p1(lines []string) int {
	maxSeatId := 0
	for _, line := range lines {
		r, c := findRowCol(line)
		if seatId := r*8 + c; seatId > maxSeatId {
			maxSeatId = seatId
		}
	}
	return maxSeatId
}

func d5p2(lines []string) int {
	plane := [128][8]int{}
	for _, line := range lines {
		r, c := findRowCol(line)
		plane[r][c] = 1
	}
	for i, row := range plane {
		fmt.Printf("%3d %v\n", i, row)
	}
	return 0
}

func main() {
	xs := utils.PathToLines("data/d05.txt")
	println(d5p1(xs))
	println(d5p2(xs))
}
