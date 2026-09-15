# Scientific Math Evaluation Toolkit

A Python-based project for evaluating whether AI-generated mathematical answers are logically and numerically correct.

## Project overview

This repository contains a lightweight evaluation framework for checking mathematical outputs against expected solutions. The goal is to move beyond simple string matching and validate whether a model's response is actually mathematically equivalent, numerically valid, or invalid under realistic edge cases.

The project is designed around a common AI evaluation pattern:

- a model produces a mathematical answer
- the answer is checked against an expected result
- the evaluator applies symbolic or numerical validation
- the result is recorded as pass or fail
- benchmark cases are used to test behavior across multiple scenarios

## Why this project matters

AI systems often produce answers that look plausible but are not mathematically correct. This toolkit addresses that by combining:

- symbolic equivalence checks with SymPy
- numerical verification with NumPy and SciPy
- validation logic for equation-style tasks
- test-driven checks for correctness, edge cases, and invalid input

This makes it a useful foundation for evaluating reasoning quality in educational, scientific, or AI-assessment workflows.

## Current capabilities

### 1) Symbolic expression validation

The evaluator can determine whether two expressions are mathematically equivalent.

Examples:

- 2*x + 3*x vs 5\*x
- sin(x)^2 + cos(x)^2 vs 1
- malformed expressions like 2 \* \* x are rejected safely

### 2) Equation-solving validation

The toolkit can also validate a numerical solution for an equation using a supplied function and initial guess. This pattern supports root-finding checks such as solving x^2 - 4 = 0.

### 3) Benchmark runner

The project includes a benchmark structure that runs multiple evaluation cases and reports totals for passed and failed cases.

## Repository structure

```text
Scientific-Math-Evaluation/
├── README.md
├── math_evaluator.py
├── benchmark_cases.py
├── test_evaluators.py
├── requirements.txt
└── .gitignore
```

## Quick start

### Prerequisites

- Python 3.10+
- pip

### 1) Clone the repository

```bash
git clone https://github.com/Mukhtar502/Scientific-Math-Evaluation.git
cd Scientific-Math-Evaluation
```

### 2) Create and activate a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Run tests

```bash
pytest
```

### 5) Use the evaluator

```python
from math_evaluator import verify_mathematical_equivalence

result = verify_mathematical_equivalence("2*x + 3*x", "5*x")
print(result)  # True
```

You can also evaluate a full benchmark case set:

```python
from benchmark_cases import BENCHMARK_CASES
from math_evaluator import evaluate_benchmark_cases

summary = evaluate_benchmark_cases(BENCHMARK_CASES)
print(summary)
```

## Example use cases

- checking whether a generated algebraic expression matches the expected answer
- validating a model's numerical solution to an equation
- comparing AI outputs against reference mathematical reasoning
- building reusable benchmark cases for math evaluation tasks

## Portfolio value

This project demonstrates practical experience with:

- Python-based scientific computing
- symbolic math and numerical validation
- automated testing with pytest
- designing evaluation logic for AI-generated outputs
- building reusable benchmark pipelines for reasoning tasks

It is a strong portfolio project for roles involving AI evaluation, data science, scientific computing, and applied machine learning.

## Roadmap

Planned extensions include:

- broader support for calculus and advanced symbolic checks
- richer benchmark datasets
- clearer reporting for pass/fail evaluation summaries
- more edge-case coverage for malformed inputs and adversarial responses

## License

This project is currently provided as a personal portfolio and evaluation prototype without a formal license file.
