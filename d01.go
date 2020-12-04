package main

import (
	"github.com/dbabiak/aoc-2020/utils"
	"strconv"
)

const s = `
1721
979
366
299
675
1456
`

func fizz(xs []int, target int) (int, bool) {
	for i, x := range xs {
		for _, y := range xs[i + 1:] {
			if x + y == target {
				return x * y, true
			}
		}

	}
	return 0, false
}

func d1p1(xs []int) int {
	n, ok := fizz(xs, 2020)
	if !ok {
		panic("wat")
	}
	return n
}

func d1p2(xs []int) int {
	for i, x := range xs {
		if n, ok := fizz(xs[i + 1:], 2020 - x); ok {
			return n * x
		}
	}
	panic("wat")
}

func main() {
	lines := utils.PathToLines("data/d01.txt")

	xs := []int{}
	for _, line := range lines {
		n, err := strconv.Atoi(line)
		utils.Check(err)
		xs = append(xs, n)
	}

	println(d1p1(xs))
	println(d1p2(xs))
}