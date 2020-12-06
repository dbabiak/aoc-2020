import os
import re
from pprint import pprint
from typing import *

os.system('head data/d04.txt')

print('\n-------------------------------\n')

re.compile(r'([a-zA-Z]+):([a-zA-Z]+)')

def main() -> None:
  with open('data/d04.txt') as fp:
      rows = []
      row = None 
      for i, line in enumerate(map(str.strip, fp)):
          row = row or []
          if line:
            for kv in line.split(' '):
              k, v = kv.split(':')
              row.append((k,v))
          else:
            rows.append(dict(row))
            row = []
  print('part1', part1(rows)) 
  print('part2', part2(rows)) 


REQUIRED_FIELDS = [
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid',
]

def is_valid(row) -> bool:
  return all(k in row for k in REQUIRED_FIELDS)


def part1(rows: List[Dict]) -> int:
    return sum(
        all(k in row for k in REQUIRED_FIELDS)
        for row in rows
    )



def part2(passports: List[Dict]) -> int:
    predicates = {
      'byr': lambda x: 1920 <= int(x) <= 2002,
      'iyr': lambda x: 2010 <= int(x) <= 2020,
      'eyr': lambda x: 2020 <= int(x) <= 2030,
      'hgt': lambda x: (
           (x.endswith('cm') and (150 <= int(x[:-2]) <= 193))
        or (x.endswith('in') and ( 59 <= int(x[:-2]) <=  76))
      ),
      'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
      'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
      'pid': lambda x: re.match(r'^[0-9]{9}$', x),
      'cid': lambda _: True,
    }
    return sum(
      (
            all(k in passport for k in REQUIRED_FIELDS) 
        and all(predicates[k](v) for k, v in passport.items())
      )
      for passport in passports
    )


          
if __name__ == '__main__':
    main()
