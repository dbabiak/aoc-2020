package main

import (
	"bufio"
	"bytes"
	"fmt"
	"github.com/dbabiak/aoc-2020/utils"
	"os"
	"os/exec"
	"regexp"
	"strconv"
	"strings"
)

var r = regexp.MustCompile("([a-zA-Z]+):([a-zA-Z]+)")

const ShellToUse = "bash"

func Shellout(command string) (error, string, string) {
	var stdout bytes.Buffer
	var stderr bytes.Buffer
	cmd := exec.Command(ShellToUse, "-c", command)
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr
	err := cmd.Run()
	return err, stdout.String(), stderr.String()
}

func system(cmd string) {
	err, sout, serr := Shellout(cmd)
	utils.Check(err)
	fmt.Fprint(os.Stdout, sout)
	fmt.Fprint(os.Stderr, serr)
}

func parsePassports(f *os.File) []map[string]string {
	passports := []map[string]string{}

	scanner := bufio.NewScanner(f)
	passport := map[string]string{}
	for i := 0; scanner.Scan(); i++ {
		line := scanner.Text()
		line = strings.TrimSpace(line)
		if len(line) > 0 {
			xs := strings.Split(line, " ")
			for _, x := range xs {
				kv := strings.Split(x, ":")
				passport[kv[0]] = kv[1]
			}
		} else {
			passports = append(passports, passport)
			passport = map[string]string{}
		}
	}
	return passports
}

var requiredKeys = []string{
	"byr",
	"iyr",
	"eyr",
	"hgt",
	"hcl",
	"ecl",
	"pid",
}

func d4p1(passports []map[string]string) int {
	n := 0
	for _, p := range passports {
		if hasAllKeys(p) {
			n += 1
		}
	}
	return n
}

func hasAllKeys(p map[string]string) bool {
	for _, k := range requiredKeys {
		if _, contains := p[k]; !contains {
			return false
		}
	}
	return true
}

func mustParseInt(s string) int {
	n, err := strconv.Atoi(s)
	utils.Check(err)
	return n
}

var hclRegex = regexp.MustCompile("^#[0-9a-f]{6}$")
var pidRegex = regexp.MustCompile("^[0-9]{9}$")

func d4p2(passports []map[string]string) int {
	var eyeColors = map[string]bool{
		"amb": true, "blu": true, "brn": true, "gry": true, "grn": true, "hzl": true, "oth": true,
	}
	validations := map[string]func(string) bool{
		"byr": func(x string) bool { n := mustParseInt(x); return 1920 <= n && n <= 2002 },
		"iyr": func(x string) bool { n := mustParseInt(x); return 2010 <= n && n <= 2020 },
		"eyr": func(x string) bool { n := mustParseInt(x); return 2020 <= n && n <= 2030 },
		"hgt": func(x string) bool {
			if strings.HasSuffix(x, "cm") {
				n := mustParseInt(x[:len(x) - 2])
				return 150 <= n && n <= 193
			} else if strings.HasSuffix(x, "in") {
				n := mustParseInt(x[:len(x) - 2])
				return 59 <= n && n <= 76
			} else {
				return false
			}
		},
		"hcl": func(x string) bool { return hclRegex.MatchString(x) },
		"ecl": func(x string) bool { _, contains := eyeColors[x]; return contains },
		"pid": func(x string) bool { return pidRegex.MatchString(x) },
		"cid": func(x string) bool { return true },
	}

	n := 0
	NextPassport:
	for _, passport := range passports {
		if !hasAllKeys(passport) {
			continue
		}

		for k, v := range passport {
			if pred := validations[k]; !pred(v) {
				continue NextPassport
			}
		}
		n += 1
	}
	return n
}

func main() {
	system("head data/d04.txt")
	println("\n---------------------\n")

	f, err := os.Open("data/d04.txt")
	utils.Check(err)
	passports := parsePassports(f)
	println("d4p1", d4p1(passports))
	println("d4p2", d4p2(passports))
}
