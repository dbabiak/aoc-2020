package main

import (
	"github.com/dbabiak/aoc-2020/utils"
	"io/ioutil"
	"os"
	"strings"
)

const s = `
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
`

func parsed03() []string {
	f, err := os.Open("./data/d03.txt")
	utils.Check(err)
	buf, err := ioutil.ReadAll(f)
	s := strings.TrimSpace(string(buf))
	lines := strings.Split(s, "\n")
	return lines
}

func main() {
	//grid := strings.Split(strings.TrimSpace(s), "\n")
	grid := parsed03()
	dRow, dCol := 1, 3
	row := 0
	col := 0
	n := 0
	for {
		cell := grid[row][col]
		if cell == '#' {
			println("hit a tree", row, col)
			n += 1
		}

		row = (row + dRow)
		col = (col + dCol) % len(grid[0])
		// have we hit the bottom row on the grid?
		if row >= len(grid) {
			break
		}
	}
	println("done!", n)
}
