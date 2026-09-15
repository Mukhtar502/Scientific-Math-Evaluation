# Scientific Math Evaluation Toolkit

A Python-based evaluation framework for validating mathematical reasoning in AI-generated outputs.

## Project purpose

This project is designed to assess whether a model's mathematical answer is technically correct, using rigorous symbolic and numerical validation methods. It focuses on the kinds of checks needed for AI evaluation pipelines where correctness, precision, and edge-case handling matter.

The repository combines:

- symbolic equivalence checking with SymPy
- numerical verification with NumPy and SciPy
- unit tests for correctness and invalid-input handling
- a foundation for building broader AI math benchmarking workflows

## Why this matters for AI evaluation

When evaluating AI-generated mathematical responses, a correct answer is not just a string match. The system must assess whether the output is:

- mathematically equivalent to the expected result
- valid under symbolic manipulation
- numerically consistent when solved or approximated
- robust against malformed or non-equivalent input

This toolkit is a starting point for building that evaluation layer.

## Current functionality

### Symbolic equivalence checking

The core evaluator parses algebraic expressions and verifies whether two expressions are mathematically equivalent.

Example checks:

- `2*x + 3*x` vs `5*x`
- `sin(x)**2 + cos(x)**2` vs `1`
- invalid syntax such as `2 * * x` is rejected safely

### Numerical root validation

The repository also includes a numerical validation pattern for solving and checking equation roots using SciPy's `fsolve`.

This is useful for confirming that a model's numerical answer satisfies the equation it claims to solve.

## Project goals

This project is intended to evolve into a more formal benchmark or evaluation toolkit for scientific math tasks, with emphasis on:

- rigorous correctness checks
- reproducible evaluation criteria
- test-case design for mathematical reasoning tasks
- support for AI model output verification in educational and scientific contexts

## Relevant technologies

- Python
- SymPy for symbolic math
- NumPy for numerical operations
- SciPy for root-finding and numerical solving
- Pytest for validation tests

## Example use cases

- verifying whether a generated algebraic expression matches the expected answer
- checking whether a numerical solution actually satisfies a function
- building evaluation pipelines for comparing AI outputs to reference solutions
- creating test cases for mathematical reasoning benchmarks

## Roadmap

The repository is currently a strong foundation for a broader evaluation system. Planned extensions include:

- support for calculus and trigonometric evaluations
- more structured benchmark datasets
- problem-to-answer validation workflows
- richer edge-case and adversarial test coverage
- improved reporting for pass/fail evaluation outcomes

## Portfolio framing

This project demonstrates practical experience with:

- mathematical reasoning in Python
- scientific computing libraries
- automated validation
- test-driven development for correctness checks

It is a useful starting point for a portfolio focused on AI evaluation, scientific computing, and rigorous mathematical verification.
