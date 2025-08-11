# Mosaia Python SDK - Deployment Guide

This guide covers the complete process of building, testing, and deploying the Mosaia Python SDK package.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (latest version)
- Git

## Quick Start

### 1. Clone and Setup

```bash
git clone <repository-url>
cd mosaia-python-sdk
```

### 2. Install Development Dependencies

```bash
pip install -e .[dev]
```

### 3. Run the Complete Build Process

```bash
python build_and_deploy.py
```

This will:
- Check prerequisites
- Install dependencies
- Format code
- Run linting
- Execute tests
- Build the package
- Verify the package
- Test the installed package

## Manual Build Process

If you prefer to run each step manually:

### 1. Code Quality Checks

```bash
# Format code
make format

# Check formatting
make format-check

# Run linting
make lint

# Run tests
make test-cov
```

### 2. Build Package

```bash
# Clean previous builds
make clean

# Build package
make build
```

### 3. Verify Package

```bash
# Check package
make check
```

### 4. Test Built Package

```bash
# Install the built package
pip install dist/*.whl

# Test import
python -c "import mosaia; print('Package works!')"
```

## Deployment Options

### Option 1: Deploy to PyPI (Production)

#### Prerequisites
1. Create a PyPI account at [https://pypi.org](https://pypi.org)
2. Create an API token in your PyPI account settings
3. Set environment variables:

```bash
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="your-api-token"
```

#### Deploy

```bash
# Using the build script
python build_and_deploy.py --deploy

# Or manually
make deploy
```

### Option 2: Deploy to Test PyPI (Testing)

Test PyPI is useful for testing your package before publishing to production.

#### Prerequisites
1. Create a Test PyPI account at [https://test.pypi.org](https://test.pypi.org)
2. Create an API token
3. Set environment variables:

```bash
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="your-test-api-token"
```

#### Deploy

```bash
# Using the build script
python build_and_deploy.py --deploy --test

# Or manually
make deploy-test
```

### Option 3: Local Distribution

For internal use or testing, you can distribute the built files directly:

```bash
# Build the package
make build

# The distribution files are now in the `dist/` directory:
# - mosaia-1.0.0.tar.gz (source distribution)
# - mosaia-1.0.0-py3-none-any.whl (wheel distribution)

# Install from local files
pip install dist/mosaia-1.0.0-py3-none-any.whl
```

## GitHub Actions CI/CD

The repository includes a GitHub Actions workflow that automatically:

1. **Tests** on multiple Python versions (3.8-3.12)
2. **Builds** the package on main branch and releases
3. **Deploys** to PyPI on releases
4. **Updates** documentation on main branch

### Setup

1. **Enable GitHub Actions** in your repository settings
2. **Set PyPI API Token** as a repository secret:
   - Go to Settings → Secrets and variables → Actions
   - Add `PYPI_API_TOKEN` with your PyPI API token

### Triggering Deployments

- **Automatic**: Push to main branch or create a release
- **Manual**: Use the GitHub Actions tab to manually trigger workflows

## Version Management

### Updating Version

1. **Update version in `pyproject.toml`**:
   ```toml
   [project]
   version = "1.0.1"  # Increment version
   ```

2. **Update version in `setup.py`** (if still using it):
   ```python
   setup(
       version="1.0.1",
       # ... other settings
   )
   ```

3. **Create a Git tag**:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

4. **Create a GitHub release** to trigger automatic deployment

### Versioning Strategy

- **Major version** (1.x.x): Breaking changes
- **Minor version** (x.1.x): New features, backward compatible
- **Patch version** (x.x.1): Bug fixes, backward compatible

## Troubleshooting

### Common Issues

#### 1. Build Failures

```bash
# Clean and rebuild
make clean
make build
```

#### 2. Test Failures

```bash
# Run tests with verbose output
pytest tests/ -v -s

# Run specific test file
pytest tests/unit/test_api_client.py -v
```

#### 3. Import Errors

```bash
# Reinstall in development mode
pip uninstall mosaia
pip install -e .
```

#### 4. PyPI Upload Failures

```bash
# Check credentials
echo $TWINE_USERNAME
echo $TWINE_PASSWORD

# Test with Test PyPI first
make deploy-test
```

### Getting Help

1. **Check the logs** from the build script
2. **Review test output** for specific failures
3. **Check package structure** with `pip show mosaia`
4. **Verify dependencies** with `pip list`

## Best Practices

### Before Deployment

1. ✅ **All tests pass** locally and in CI
2. ✅ **Code is formatted** and linted
3. ✅ **Version is updated** in all files
4. ✅ **Documentation is updated**
5. ✅ **Changelog is updated**

### Deployment Checklist

- [ ] Code is tested and working
- [ ] Version numbers are consistent
- [ ] PyPI credentials are set
- [ ] Test PyPI deployment successful (if applicable)
- [ ] GitHub Actions are passing
- [ ] Documentation is updated

### Post-Deployment

1. **Verify installation**:
   ```bash
   pip install mosaia
   python -c "import mosaia; print(mosaia.__version__)"
   ```

2. **Test functionality** with the sandbox:
   ```bash
   python sandbox.py
   ```

3. **Monitor PyPI** for successful upload
4. **Update release notes** on GitHub
5. **Notify team** of new release

## Security Considerations

### API Keys and Tokens

- **Never commit** API keys or tokens to version control
- **Use environment variables** for sensitive data
- **Rotate tokens** regularly
- **Use Test PyPI** for testing deployments

### Package Security

- **Verify dependencies** are from trusted sources
- **Keep dependencies updated** to latest secure versions
- **Scan for vulnerabilities** using tools like `safety`

## Monitoring and Maintenance

### Health Checks

Regularly monitor:
- **Test coverage** (aim for >90%)
- **Build success rate** in CI/CD
- **Package download statistics** on PyPI
- **User feedback** and issues

### Maintenance Tasks

- **Monthly**: Update dependencies
- **Quarterly**: Review and update documentation
- **As needed**: Address security vulnerabilities
- **Before releases**: Update changelog and version

---

For additional support, see the [Contributing Guide](CONTRIBUTING.md) or open an issue on GitHub.
