# DevSecOps Demo Application

This is a demo application created for learning DevSecOps principles. It intentionally contains several security vulnerabilities for educational purposes.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Security Issues

This application contains several intentional security vulnerabilities:
- Hardcoded secrets
- SQL injection vulnerability
- Insecure JWT implementation
- Unsafe file upload
- Debug mode enabled in production
- Outdated dependencies

## Learning Objectives

1. Identify security vulnerabilities using automated tools
2. Understand the importance of secrets management
3. Learn about secure coding practices
4. Implement security fixes 