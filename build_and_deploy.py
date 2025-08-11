#!/usr/bin/env python3
"""
Build, test, and deploy script for the Mosaia Python SDK.

This script automates the entire process of:
1. Building the package
2. Running tests
3. Checking code quality
4. Building distribution files
5. Deploying to PyPI (optional)
"""

import os
import sys
import subprocess
import argparse
import shutil
from pathlib import Path
from typing import List, Optional


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(message: str):
    """Print a formatted header message."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{message:^60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")


def print_step(message: str):
    """Print a step message."""
    print(f"\n{Colors.OKBLUE}🔧 {message}{Colors.ENDC}")


def print_success(message: str):
    """Print a success message."""
    print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")


def print_warning(message: str):
    """Print a warning message."""
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")


def print_error(message: str):
    """Print an error message."""
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")


def run_command(cmd: List[str], cwd: Optional[Path] = None, check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed with exit code {e.returncode}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        raise


def check_prerequisites():
    """Check if all required tools are installed."""
    print_step("Checking prerequisites...")
    
    required_tools = [
        ("python", "--version"),
        ("pip", "--version"),
        ("pytest", "--version"),
        ("black", "--version"),
        ("isort", "--version"),
        ("flake8", "--version"),
    ]
    
    missing_tools = []
    
    for tool, version_flag in required_tools:
        try:
            run_command([tool, version_flag], check=False)
            print_success(f"{tool} is available")
        except FileNotFoundError:
            missing_tools.append(tool)
            print_warning(f"{tool} is not available")
    
    if missing_tools:
        print_error(f"Missing required tools: {', '.join(missing_tools)}")
        print("Please install them using: pip install -e .[dev]")
        return False
    
    return True


def install_dev_dependencies():
    """Install development dependencies."""
    print_step("Installing development dependencies...")
    
    try:
        run_command([sys.executable, "-m", "pip", "install", "-e", ".[dev]"])
        print_success("Development dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print_error("Failed to install development dependencies")
        return False


def run_code_formatting():
    """Run code formatting tools."""
    print_step("Running code formatting...")
    
    try:
        # Run isort
        print("Running isort...")
        run_command([sys.executable, "-m", "isort", "mosaia/", "tests/"], check=False)
        print_success("isort completed")
        
        # Run black
        print("Running black...")
        run_command([sys.executable, "-m", "black", "mosaia/", "tests/"], check=False)
        print_success("black completed")
        
        return True
    except subprocess.CalledProcessError:
        print_error("Code formatting failed")
        return False


def run_linting():
    """Run linting tools."""
    print_step("Running linting...")
    
    try:
        # Run flake8
        print("Running flake8...")
        run_command([sys.executable, "-m", "flake8", "mosaia/", "tests/"], check=False)
        print_success("flake8 completed")
        
        return True
    except subprocess.CalledProcessError:
        print_warning("flake8 found some issues (continuing anyway)")
        return True


def run_tests():
    """Run the test suite."""
    print_step("Running tests...")
    
    try:
        # Run tests with coverage
        run_command([
            sys.executable, "-m", "pytest", 
            "--cov=mosaia", 
            "--cov-report=term-missing",
            "--cov-report=html",
            "-v"
        ])
        print_success("All tests passed")
        return True
    except subprocess.CalledProcessError:
        print_error("Some tests failed")
        return False


def clean_build_artifacts():
    """Clean previous build artifacts."""
    print_step("Cleaning build artifacts...")
    
    build_dirs = ["build", "dist", "*.egg-info"]
    
    for pattern in build_dirs:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"Removed {path}")
            elif path.is_file():
                path.unlink()
                print(f"Removed {path}")
    
    print_success("Build artifacts cleaned")


def build_package():
    """Build the package distribution files."""
    print_step("Building package...")
    
    try:
        # Build source distribution and wheel
        run_command([sys.executable, "-m", "build"])
        print_success("Package built successfully")
        return True
    except subprocess.CalledProcessError:
        print_error("Package build failed")
        return False


def check_package():
    """Check the built package."""
    print_step("Checking built package...")
    
    try:
        # Check the wheel
        wheel_files = list(Path("dist").glob("*.whl"))
        if wheel_files:
            run_command([sys.executable, "-m", "twine", "check", str(wheel_files[0])])
            print_success("Package check passed")
        else:
            print_error("No wheel files found")
            return False
        
        return True
    except subprocess.CalledProcessError:
        print_error("Package check failed")
        return False


def install_test_package():
    """Install the built package in a test environment."""
    print_step("Installing test package...")
    
    try:
        # Install the wheel
        wheel_files = list(Path("dist").glob("*.whl"))
        if wheel_files:
            run_command([sys.executable, "-m", "pip", "install", str(wheel_files[0])])
            print_success("Test package installed")
            return True
        else:
            print_error("No wheel files found")
            return False
    except subprocess.CalledProcessError:
        print_error("Test package installation failed")
        return False


def test_installed_package():
    """Test the installed package."""
    print_step("Testing installed package...")
    
    try:
        # Test basic import
        test_code = """
import mosaia
print(f"Mosaia SDK version: {mosaia.__version__}")
print("✅ Package imported successfully!")
"""
        
        result = subprocess.run([
            sys.executable, "-c", test_code
        ], capture_output=True, text=True, check=True)
        
        print(result.stdout)
        print_success("Installed package test passed")
        return True
    except subprocess.CalledProcessError:
        print_error("Installed package test failed")
        return False


def deploy_to_pypi():
    """Deploy the package to PyPI."""
    print_step("Deploying to PyPI...")
    
    # Check if we have PyPI credentials
    if not os.getenv("TWINE_USERNAME") or not os.getenv("TWINE_PASSWORD"):
        print_warning("PyPI credentials not found in environment variables")
        print("Set TWINE_USERNAME and TWINE_PASSWORD to deploy to PyPI")
        return False
    
    try:
        # Upload to PyPI
        run_command([sys.executable, "-m", "twine", "upload", "dist/*"])
        print_success("Package deployed to PyPI successfully!")
        return True
    except subprocess.CalledProcessError:
        print_error("PyPI deployment failed")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Build, test, and deploy Mosaia Python SDK")
    parser.add_argument(
        "--skip-format", 
        action="store_true", 
        help="Skip code formatting"
    )
    parser.add_argument(
        "--skip-lint", 
        action="store_true", 
        help="Skip linting"
    )
    parser.add_argument(
        "--skip-tests", 
        action="store_true", 
        help="Skip running tests"
    )
    parser.add_argument(
        "--deploy", 
        action="store_true", 
        help="Deploy to PyPI after successful build"
    )
    parser.add_argument(
        "--clean", 
        action="store_true", 
        help="Clean build artifacts before building"
    )
    
    args = parser.parse_args()
    
    print_header("Mosaia Python SDK - Build & Deploy")
    
    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check prerequisites
    if not check_prerequisites():
        sys.exit(1)
    
    # Install dev dependencies
    if not install_dev_dependencies():
        sys.exit(1)
    
    # Clean build artifacts if requested
    if args.clean:
        clean_build_artifacts()
    
    # Run code formatting
    if not args.skip_format:
        if not run_code_formatting():
            sys.exit(1)
    
    # Run linting
    if not args.skip_lint:
        if not run_linting():
            sys.exit(1)
    
    # Run tests
    if not args.skip_tests:
        if not run_tests():
            sys.exit(1)
    
    # Build package
    if not build_package():
        sys.exit(1)
    
    # Check package
    if not check_package():
        sys.exit(1)
    
    # Test installed package
    if not install_test_package():
        sys.exit(1)
    
    if not test_installed_package():
        sys.exit(1)
    
    # Deploy to PyPI if requested
    if args.deploy:
        if not deploy_to_pypi():
            sys.exit(1)
    
    print_header("Build & Deploy Complete!")
    print_success("🎉 Package has been built, tested, and is ready for distribution!")
    
    if args.deploy:
        print_success("🚀 Package has been deployed to PyPI!")
    else:
        print("💡 To deploy to PyPI, run: python build_and_deploy.py --deploy")
    
    print("\n📦 Distribution files are available in the 'dist/' directory")
    print("🔧 To install in development mode: pip install -e .")
    print("📚 To install the built package: pip install dist/*.whl")


if __name__ == "__main__":
    main()
