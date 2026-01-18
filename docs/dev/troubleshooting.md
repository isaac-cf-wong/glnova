# Troubleshooting

This guide covers common issues you might encounter when using this template and how to resolve them.

## Setup Issues

### Pre-commit Hook Installation Fails

**Problem:** `pre-commit install` returns an error or hooks don't run on commit.

**Solutions:**

<!-- prettier-ignore-start -->

1. Ensure you're in the project root directory
2. Verify Python virtual environment is activated
3. Reinstall pre-commit:

    ```bash
    pip uninstall pre-commit
    pip install pre-commit
    pre-commit install
    pre-commit install --hook-type commit-msg
    ```

4. Check if `.git` directory exists (must be a git repository)
5. Try running manually: `pre-commit run --all-files`

<!-- prettier-ignore-end -->

### commitlint Not Running

**Problem:** Commit messages aren't validated despite `npm install` being run.

**Solutions:**

<!-- prettier-ignore-start -->

1. Verify `npm install` was successful:

    ```bash
    npm list @commitlint/config-angular
    ```

2. Re-install commitlint dependencies:

    ```bash
    npm install --save-dev @commitlint/cli @commitlint/config-angular
    ```

3. Reinstall pre-commit hooks:

    ```bash
    pre-commit install --hook-type commit-msg
    ```

4. Test manually:

    ```bash
    echo "invalid message" | commitlint
    echo "feat: valid message" | commitlint
    ```

<!-- prettier-ignore-end -->

### Virtual Environment Issues

**Problem:** Packages can't be found or dependencies conflict.

**Solutions:**

<!-- prettier-ignore-start -->

1. Create a fresh virtual environment:

    ```bash
    rm -rf .venv
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

2. Upgrade pip:

    ```bash
    python -m pip install --upgrade pip
    ```

3. Install dependencies:

    ```bash
    pip install -e ".[dev,docs,test]"
    ```

4. Verify installation:

    ```bash
    python -c "import glnova; print(glnova.__version__)"
    ```

<!-- prettier-ignore-end -->

### Python Version Mismatch

**Problem:** `python -m venv .venv` fails or tests don't run with wrong Python version.

**Solutions:**

<!-- prettier-ignore-start -->

1. Check your Python version:

    ```bash
    python --version
    ```

2. Ensure Python 3.10 or higher is installed
3. Use specific Python version when creating venv:

    ```bash
    python3.11 -m venv .venv
    ```

4. Or use uv for version management:

    ```bash
    uv venv --python 3.11
    source .venv/bin/activate
    ```

<!-- prettier-ignore-end -->

## Pre-commit Hook Issues

### Hooks Running Too Slowly

**Problem:** Pre-commit takes a very long time or times out.

**Solutions:**

<!-- prettier-ignore-start -->

1. Check which hooks are slow:

    ```bash
    pre-commit run --all-files --verbose
    ```

2. Consider excluding large files:

    ```yaml
    exclude: |
      (?x)^(
        large_data_file.csv|
        node_modules/
      )$
    ```

3. Run specific hooks:

    ```bash
    pre-commit run black --all-files  # Just black
    ```

<!-- prettier-ignore-end -->

### Formatting Changes After Commit

**Problem:** Pre-commit auto-fixes files, but you didn't expect it.

**Solutions:**

<!-- prettier-ignore-start -->

1. This is normal behavior - review the changes
2. Stage the new changes:

    ```bash
    git add .
    git commit -m "your message"  # Try again
    ```

3. Modify tool settings if behavior is unwanted (in `pyproject.toml`)
4. Disable specific hooks temporarily:

    ```bash
    SKIP=black,ruff pre-commit run --all-files
    ```

<!-- prettier-ignore-end -->

### "Unstaged Changes" After Running Hooks

**Problem:** Pre-commit modified files but they're not staged.

**Solutions:**

<!-- prettier-ignore-start -->

1. This is expected - review changes:

    ```bash
    git diff
    ```

2. Stage the changes:

    ```bash
    git add .
    ```

3. Try committing again
4. Or use `git add -A` to stage all changes before commit

<!-- prettier-ignore-end -->

## Getting Help

If you encounter issues not listed here:

<!-- prettier-ignore-start -->

1. **Check existing issues**: Search GitHub Issues for your problem
2. **Review logs carefully**: Error messages usually point to the root cause
3. **Search documentation**: Many issues are covered in specific tool docs
4. **Try minimal reproduction**: Isolate the problem to a single file/command
5. **Ask for help**: Open an [issue](https://github.com/isaac-cf-wong/glnova/issues/new/choose) with:
    - Your environment (Python version, OS)
    - Steps to reproduce
    - Full error message/logs
    - What you've already tried

<!-- prettier-ignore-end -->
