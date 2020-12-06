package main

import (
	"bufio"
	"github.com/dbabiak/aoc-2020/utils"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Passport struct {
	byr	int
	iyr	int
	eyr	int
	hgt string
	hcl string
	ecl string
	pid string
	cid string
}


func parsePassport(kvs map[string]string) *Passport {
	// do we want this to be dynamic?
	passport := Passport{}
	for k, v := range kvs {
		switch k {
		case "byr":
			n, err := strconv.Atoi(v)
			utils.Check(err)
			passport.byr = n

		case "iyr":
			n, err := strconv.Atoi(v)
			utils.Check(err)
			passport.iyr = n

		case "eyr":
			n, err := strconv.Atoi(v)
			utils.Check(err)
			passport.eyr = n

		case "hgt": passport.hgt = v
		case "hcl": passport.hcl = v
		case "ecl": passport.ecl = v
		case "pid": passport.pid = v
		case "cid": passport.cid = v
		}
	}
	return &passport
}
var r = regexp.MustCompile("([a-zA-Z]+):([a-zA-Z]+)")

func main() {
	f, err := os.Open("./data/d04.txt")
	utils.Check(err)
	scan := bufio.NewScanner(f)
	for i := 0 ; scan.Scan(); i++ {
		line := scan.Text()
		xs := strings.Split(line, "\n")
		for _, x := range xs {
			kv := r.FindStringSubmatch(x)
			k, v := kv[0], kv[1]
		}
	}
}