# Contributing Guide

## Getting Started

1. Fork the Repository
   ```bash
   git clone https://github.com/yourusername/wifi-monitor.git
   cd wifi-monitor
   ```

2. Create Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Development Setup

### Prerequisites
- Python 3.6+
- Nmap
- SQLite
- Git

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Include docstrings
- Add comments for complex logic

### Testing
1. Run tests:
   ```bash
   python -m pytest tests/
   ```

2. Add new tests for new features

## Making Changes

1. Create Branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make Changes
   - Write clean, documented code
   - Follow project structure
   - Update documentation
   - Add tests

3. Commit Changes
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

## Documentation

1. Update Documentation
   - Add/modify markdown files in docs/
   - Update API documentation
   - Include usage examples

2. Build Documentation
   ```bash
   mkdocs serve  # Test locally
   mkdocs build  # Build static site
   ```

## Pull Requests

1. Push Changes
   ```bash
   git push origin feature/your-feature-name
   ```

2. Create Pull Request
   - Clear description
   - Reference issues
   - List changes made

3. Code Review
   - Address feedback
   - Update PR as needed
   - Maintain discussion

## Best Practices

### Code
- Keep functions focused
- Use meaningful names
- Handle errors appropriately
- Add logging where needed

### Documentation
- Clear explanations
- Code examples
- Configuration details
- Update README.md

### Testing
- Unit tests
- Integration tests
- Test edge cases
- Document test cases

## Getting Help

- Open an issue
- Join discussions
- Read documentation
- Ask questions 