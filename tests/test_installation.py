import sys
import subprocess
import pkg_resources
import pytest

def test_package_installation():
    """Test that the Mosaia package can be installed and imported."""
    # Try to install the package in development mode
    process = subprocess.run([
        sys.executable, 
        "-m", 
        "pip", 
        "install", 
        "-e", 
        ".",
        "--use-pep517"
    ], capture_output=True, text=True)
    
    assert process.returncode == 0, f"Package installation failed: {process.stderr}"
    
    # Verify the package can be imported
    try:
        import mosaia
    except ImportError as e:
        pytest.fail(f"Failed to import package: {e}")
    
    # Check package version
    try:
        version = pkg_resources.get_distribution('mosaia').version
        assert version, "Package version is empty"
    except pkg_resources.DistributionNotFound as e:
        pytest.fail(f"Could not determine package version: {e}")

if __name__ == "__main__":
    success = test_package_installation()
    if success:
        print("\nAll tests passed! 🎉")
    else:
        print("\nSome tests failed! 😢")
        sys.exit(1)
