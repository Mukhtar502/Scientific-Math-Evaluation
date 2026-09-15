import pytest
from math_evaluator import (
    verify_mathematical_equivalence,
    evaluate_model_response,
    evaluate_benchmark_cases,
)
from benchmark_cases import BENCHMARK_CASES


def test_equivalent_expressions():
    assert verify_mathematical_equivalence("2*x + 3*x", "5*x") == True
    assert verify_mathematical_equivalence("sin(x)**2 + cos(x)**2", "1") == True


def test_non_equivalent_expressions():
    assert verify_mathematical_equivalence("x**2", "x**3") == False


def test_invalid_syntax():
    assert verify_mathematical_equivalence("2 * * x", "2*x") == False


def test_model_response_accepts_equivalent_expression():
    result = evaluate_model_response(
        model_output="(x - 2) * (x + 2)",
        expected_output="x**2 - 4",
        evaluation_type="expression"
    )
    assert result["passed"] is True


def test_model_response_rejects_non_equivalent_expression():
    result = evaluate_model_response(
        model_output="x**2",
        expected_output="x**3",
        evaluation_type="expression"
    )
    assert result["passed"] is False


def test_model_response_validates_equation_solution():
    result = evaluate_model_response(
        model_output="2.0",
        expected_output="2.0",
        evaluation_type="equation",
        function=lambda x: x**2 - 4,
        initial_guess=1.0
    )
    assert result["passed"] is True


def test_benchmark_summary_runs_successfully():
    summary = evaluate_benchmark_cases(BENCHMARK_CASES)
    assert summary["total_cases"] == 4
    assert summary["failed_cases"] >= 0
    assert summary["passed_cases"] + summary["failed_cases"] == summary["total_cases"]