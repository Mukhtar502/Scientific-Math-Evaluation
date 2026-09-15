BENCHMARK_CASES = [
    {
        "name": "algebra_equivalence",
        "problem": "Simplify the expression 2*x + 3*x.",
        "model_output": "5*x",
        "expected_output": "5*x",
        "evaluation_type": "expression",
    },
    {
        "name": "trigonometric_identity",
        "problem": "Simplify sin(x)^2 + cos(x)^2.",
        "model_output": "1",
        "expected_output": "1",
        "evaluation_type": "expression",
    },
    {
        "name": "quadratic_root_check",
        "problem": "Solve x^2 - 4 = 0.",
        "model_output": "2.0",
        "expected_output": "2.0",
        "evaluation_type": "equation",
        "function": lambda x: x**2 - 4,
        "initial_guess": 1.0,
    },
    {
        "name": "invalid_syntax_rejection",
        "problem": "Evaluate the malformed expression 2 * * x.",
        "model_output": "2 * * x",
        "expected_output": "2*x",
        "evaluation_type": "expression",
    },
]
