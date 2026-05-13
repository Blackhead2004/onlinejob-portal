# Contributing to Online Job Portal

Thank you for your interest in contributing to the Online Job Portal project! We welcome contributions from the community and are grateful for every pull request, bug report, and feature suggestion.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Guidelines](#development-guidelines)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

---

## Code of Conduct

This project adheres to the Contributor Covenant code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB (local or Atlas)
- Git
- Basic understanding of Flask and MongoDB

### Setup Development Environment

1. **Fork the Repository**
   ```bash
   Click the "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/onlinejob-portal.git
   cd onlinejob-portal
   ```

3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection details
   ```

6. **Run the Application**
   ```bash
   python app.py
   ```

---

## Development Guidelines

### Code Style

- Follow **PEP 8** guidelines for Python code
- Use meaningful variable and function names
- Keep functions small and focused on a single task
- Add docstrings to functions and classes

### Python Code Example

```python
def validate_email(email):
    """
    Validate email format.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### Comments and Documentation

- Write clear comments for complex logic
- Update README.md if adding new features
- Document new database collections or fields
- Add docstrings to all functions

### Testing

- Test your changes locally before submitting
- Verify all existing features still work
- Test with different user roles (Admin, Company, Candidate)

---

## Making Changes

### Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New feature
- `bugfix/` - Bug fix
- `docs/` - Documentation update
- `refactor/` - Code refactoring
- `test/` - Adding tests

### Make Your Changes

1. Write clean, readable code
2. Follow the existing code structure
3. Make commits with clear messages
4. Keep commits focused and atomic

### Commit Messages

Write clear, descriptive commit messages:

```bash
# Good
git commit -m "Add user profile update functionality"
git commit -m "Fix: Resume download not working for PDF files"
git commit -m "Refactor: Simplify database connection logic"

# Avoid
git commit -m "Update"
git commit -m "Fix bug"
git commit -m "Changes"
```

---

## Submitting Changes

### Before Submitting

1. **Update Your Branch**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run Local Tests**
   - Test all user workflows
   - Verify no console errors
   - Check database operations

3. **Update Documentation**
   - Update README.md if needed
   - Add comments to complex code
   - Update database schema if changed

### Create a Pull Request

1. **Push Your Branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Go to GitHub and Create a PR**
   - Provide a clear title
   - Write a detailed description
   - Reference any related issues

### PR Title Format

```
[TYPE] Brief description

Examples:
[Feature] Add email notifications for job applications
[Bugfix] Fix pagination on job listings
[Docs] Update installation instructions
```

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Related Issue
Closes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update

## Changes Made
- Bullet point 1
- Bullet point 2

## Testing Done
- What tests were performed
- How to verify the changes

## Screenshots (if applicable)
Add screenshots for UI changes
```

---

## Reporting Bugs

### Before Reporting

- Check existing issues to avoid duplicates
- Update to the latest version
- Verify the bug with sample data

### Bug Report Format

Create an issue with the following:

```markdown
## Description
Brief description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happened

## Screenshots/Logs
Attach any relevant logs or screenshots

## Environment
- Python version
- OS (Windows/Mac/Linux)
- Browser (if applicable)
```

---

## Suggesting Enhancements

### Enhancement Suggestions

Create an issue with:

```markdown
## Description
Clear description of the enhancement

## Motivation
Why is this enhancement needed?

## Proposed Solution
How should this be implemented?

## Alternative Solutions
Any other ways to solve this?

## Additional Context
Any other relevant information
```

---

## Project Structure Overview

```
onlinejob-portal/
├── app.py              # Main Flask application
├── config.py           # Database configuration
├── templates/          # HTML templates
├── static/             # CSS, JavaScript files
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

---

## Common Development Tasks

### Adding a New Route

1. Add the route in `app.py`
2. Create corresponding HTML template in `templates/`
3. Test the functionality
4. Update README.md if needed

### Adding Database Fields

1. Update the collection schema in code comments
2. Update `app.py` to handle the new field
3. Document in README.md
4. Provide migration guidance

### Fixing a Bug

1. Create a bugfix branch
2. Write a test case for the bug
3. Fix the issue
4. Verify all tests pass
5. Submit PR with clear description

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [PEP 8 Style Guide](https://pep8.org/)
- [GitHub Pull Request Guide](https://docs.github.com/en/pull-requests)

---

## Questions?

- Open an issue for questions
- Check existing discussions
- Review the README.md

---

## Thank You! 🎉

Your contributions help make this project better for everyone. We appreciate your effort and look forward to working with you!

**Happy coding!** 🚀
