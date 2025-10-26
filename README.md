## Day 3
- Handmade dynamic array with append/insert/pop/negative indices
- Installable package: `pip install -e .`
- CLI: `python -m tinylist a b c d`


## Day 5
- pytest 5/5 passed, 84 % → 100 % coverage
- speed shoot-out: numpy 0.00 s, list-comp 0.08 s, tinylist 0.40 s

## Day 6 

- 100 % typed with 'mypy --strict'
- pre-commit hooks (ruff lint + format)
- Github Actions CI badge -> [![CI]
  (https://github.com/Agastya910/pyboot/actions/workflows/ci.yml/badge.svg)]
  (https://github.com/Agastya910/pyboot/actions)

## Day 7 
- Infinite prime generator with yeild
- Memory profiling: generator 30x lighter than list
- itertools.islice + count + deque rolling average


### Day 8 
- Downloaded Iris CSV with requests + pathlib
- Loaded into TinyList[dict] with csv.DictReader
- Vectorised mean: pandas 0.096, Numpy 0.052 s, TinyList 0.098 s (150 rows) 

### Day 9 
- iris --summary
- Vectorized Jacobian softmax using numpy
- revision of generators, rolling prime generator
- revision of argparse

### Day 10

- revision of rolling average generator using deque
- implementation of CircularDeque from scratch
- benchmarked against python deque

