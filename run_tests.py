#!/usr/bin/env python3
"""
Test runner for the Mosaia Python SDK.

This script provides an easy way to run all tests or specific test categories.
"""

import sys
import subprocess
import argparse
from pathlib import Path


def run_pytest(args):
    """Run pytest with the given arguments."""
    cmd = [sys.executable, "-m", "pytest"] + args
    return subprocess.run(cmd, cwd=Path(__file__).parent)


def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description="Run Mosaia Python SDK tests")
    parser.add_argument(
        "--category", "-c",
        choices=["all", "unit", "integration", "utils", "functions", "auth", "models"],
        default="all",
        help="Test category to run (default: all)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--coverage", "--cov",
        action="store_true",
        help="Run with coverage report"
    )
    parser.add_argument(
        "--fast", "-f",
        action="store_true",
        help="Run only fast tests (skip slow markers)"
    )
    parser.add_argument(
        "pytest_args",
        nargs="*",
        help="Additional arguments to pass to pytest"
    )
    
    args = parser.parse_args()
    
    # Build pytest command
    pytest_args = []
    
    if args.verbose:
        pytest_args.append("-v")
    
    if args.coverage:
        pytest_args.extend(["--cov=mosaia", "--cov-report=term-missing"])
    
    if args.fast:
        pytest_args.append("-m")
        pytest_args.append("not slow")
    
    # Add category-specific arguments
    if args.category == "unit":
        pytest_args.extend(["-m", "unit"])
    elif args.category == "integration":
        pytest_args.extend(["-m", "integration"])
    elif args.category == "utils":
        pytest_args.extend(["-m", "utils"])
    elif args.category == "functions":
        pytest_args.extend(["-m", "functions"])
    elif args.category == "auth":
        pytest_args.extend(["-m", "auth"])
    elif args.category == "models":
        pytest_args.extend(["-m", "models"])
    
    # Add any additional pytest arguments
    pytest_args.extend(args.pytest_args)
    
    print(f"🧪 Running {args.category} tests...")
    print(f"Command: pytest {' '.join(pytest_args)}")
    print("=" * 60)
    
    # Run tests
    result = run_pytest(pytest_args)
    
    print("=" * 60)
    if result.returncode == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
