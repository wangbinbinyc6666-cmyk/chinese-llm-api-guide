# Contributing to Chinese LLM API Guide

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## 📋 How to Contribute

### 1. Report Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in [GitHub Issues](#)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior
   - Screenshots (if applicable)

### 2. Submit Changes

#### Step 1: Fork the Repository

```bash
# Fork on GitHub, then clone
git clone https://github.com/YOUR_USERNAME/chinese-llm-api-guide.git
cd chinese-llm-api-guide
```

#### Step 2: Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

#### Step 3: Make Your Changes

- Follow the existing code style
- Add comments for complex logic
- Update documentation if needed

#### Step 4: Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature"  # or "fix: fix bug"
```

#### Step 5: Push to Your Fork

```bash
git push origin feature/your-feature-name
```

#### Step 6: Create a Pull Request

1. Go to the original repository
2. Click "New Pull Request"
3. Select your branch
4. Add a clear description
5. Submit the PR

## 📝 Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Formatting changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### Examples

```
feat: add streaming response support
fix: resolve authentication error
docs: update API reference
test: add unit tests for embeddings
```

## 🎨 Code Style

### Python

- Follow PEP 8
- Use type hints
- Add docstrings for functions

```python
def get_weather(location: str) -> dict:
    """
    Get the current weather for a location.

    Args:
        location: The city and state, e.g. "San Francisco, CA"

    Returns:
        Dictionary containing weather information
    """
    pass
```

### JavaScript

- Use ES6+ syntax
- Follow Airbnb Style Guide
- Add JSDoc comments

```javascript
/**
 * Get the current weather for a location
 * @param {string} location - The city and state
 * @returns {Promise<Object>} Weather information
 */
async function getWeather(location) {
  // implementation
}
```

## 🧪 Testing

Before submitting a PR:

1. Run existing tests
2. Add tests for new features
3. Ensure all tests pass

```bash
# Python
python -m pytest

# JavaScript
npm test
```

## 📚 Documentation

When adding new features:

1. Update the README if needed
2. Add examples in the `examples/` directory
3. Update API documentation if applicable

## ❓ Questions?

If you have questions about contributing:

1. Check existing documentation
2. Search GitHub Issues
3. Open a new issue with the "question" label

## 🙏 Thank You!

Every contribution helps make this project better. We appreciate your time and effort!

---

**Made with ❤️ by the community**
