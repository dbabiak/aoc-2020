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

type Vector struct {
	dRow int
	dCol int
}

func countTrees(grid []string, v Vector) int {
	dRow, dCol := v.dRow, v.dCol
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
	return n
}

func part1(grid []string) int {
	return countTrees(grid, Vector{dRow: 1, dCol: 3})
}

func part2(grid []string) int {
	nTrees := []int{}
	vectors := []Vector{
		{ dRow: 1, dCol: 1, },
		{ dRow: 1, dCol: 3, },
		{ dRow: 1, dCol: 5, },
		{ dRow: 1, dCol: 7, },
		{ dRow: 2, dCol: 1, },
	}
	for _, v := range vectors {
		nTrees = append(nTrees, countTrees(grid, v))
	}

	// u_u
	acc := 1
	for _, x := range nTrees{
		acc *= x
	}
	return acc
}

func main() {
	grid := parsed03()
	println(part1(grid))
	println(part2(grid))
}
