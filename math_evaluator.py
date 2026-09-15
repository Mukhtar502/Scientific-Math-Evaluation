import sympy as sp


def verify_mathematical_equivalence(ai_output_str, expected_output_str):
    """Return True when two mathematical expressions are symbolically equivalent."""
    try:
        x = sp.symbols("x")
        ai_expr = sp.sympify(ai_output_str)
        expected_expr = sp.sympify(expected_output_str)
        difference = sp.simplify(ai_expr - expected_expr)
        return difference == 0
    except (sp.SympifyError, TypeError, ValueError):
        return False


def evaluate_model_response(model_output, expected_output, evaluation_type, function=None, initial_guess=None):
    """Evaluate a model's mathematical answer against an expected output.

    Supported evaluation types:
    - expression: symbolic equivalence checking
    - equation: numerical root validation using a supplied function
    """
    result = {
        "passed": False,
        "evaluation_type": evaluation_type,
        "model_output": model_output,
        "expected_output": expected_output,
        "details": "",
    }

    if evaluation_type == "expression":
        passed = verify_mathematical_equivalence(str(model_output), str(expected_output))
        result["passed"] = passed
        result["details"] = (
            "Expressions are mathematically equivalent."
            if passed
            else "Expressions are not equivalent or input is invalid."
        )
        return result

    if evaluation_type == "equation":
        if function is None or initial_guess is None:
            result["details"] = "Equation evaluation requires a function and initial guess."
            return result

        try:
            from scipy.optimize import fsolve
            import numpy as np

            root = fsolve(function, initial_guess)
            residual = function(root)
            is_valid = np.isclose(residual, 0.0)
            result["passed"] = bool(is_valid)
            result["details"] = (
                f"Root found: {root[0]} with residual {residual[0]}"
            )
            return result
        except Exception as exc:
            result["details"] = f"Equation evaluation failed: {exc}"
            return result

    result["details"] = "Unsupported evaluation type."
    return result


def evaluate_benchmark_cases(cases):
    """Run a list of benchmark cases and return a summary of pass/fail results."""
    results = []
    for case in cases:
        payload = {
            "name": case.get("name", "unnamed_case"),
            "problem": case.get("problem", ""),
            "evaluation_type": case.get("evaluation_type", "expression"),
            "model_output": case.get("model_output"),
            "expected_output": case.get("expected_output"),
            "function": case.get("function"),
            "initial_guess": case.get("initial_guess"),
        }

        outcome = evaluate_model_response(
            model_output=payload["model_output"],
            expected_output=payload["expected_output"],
            evaluation_type=payload["evaluation_type"],
            function=payload["function"],
            initial_guess=payload["initial_guess"],
        )

        results.append({
            "name": payload["name"],
            "problem": payload["problem"],
            "passed": outcome["passed"],
            "details": outcome["details"],
        })

    return {
        "total_cases": len(results),
        "passed_cases": sum(1 for item in results if item["passed"]),
        "failed_cases": sum(1 for item in results if not item["passed"]),
        "results": results,
    }