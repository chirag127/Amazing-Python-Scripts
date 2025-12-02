# Contributing to PyCentral-Python-Automation-Toolkit

We welcome contributions to `PyCentral-Python-Automation-Toolkit`! To ensure a consistent and high-quality experience for all users and contributors, please adhere to the following guidelines.

## 1. Our Pledge

In the interest of fostering an open and welcoming environment, we, the maintainers and contributors, pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation. We are committed to a policy of zero tolerance for harassment of participants in any form.

## 2. Contribution Workflow

1.  **Fork the Repository:** Start by forking the `chirag127/PyCentral-Python-Automation-Toolkit` repository to your GitHub account.
2.  **Clone Your Fork:** Clone your forked repository locally:
    bash
    git clone https://github.com/chirag127/PyCentral-Python-Automation-Toolkit.git
    cd PyCentral-Python-Automation-Toolkit
    
3.  **Create a New Branch:** Create a descriptive branch for your changes:
    bash
    git checkout -b feat/your-feature-name # or fix/bug-description
    
4.  **Make Your Changes:** Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards (see Section 3).
5.  **Test Your Changes:** Run the test suite to ensure your changes haven't introduced regressions:
    bash
    # Ensure you have the necessary development dependencies installed
    # (refer to README.md for setup instructions)
    pytest
    
6.  **Lint and Format:** Ensure your code is properly formatted and linted:
    bash
    ruff check .
    ruff format .
    
7.  **Commit Your Changes:** Commit your changes with clear and concise messages:
    bash
    git add .
    git commit -m "feat: Add new automation script for X"
    
8.  **Push to Your Fork:** Push your branch to your forked repository:
    bash
    git push origin feat/your-feature-name
    
9.  **Open a Pull Request:** Navigate to the original repository (`chirag127/PyCentral-Python-Automation-Toolkit`) and open a new Pull Request from your branch. Provide a clear description of your changes and the problem they solve.

## 3. Coding Standards & Best Practices

We adhere to the Apex Technical Authority standards for code quality and consistency:

*   **Python Version:** Python 3.10+ is the minimum supported version.
*   **Linting & Formatting:** We use `Ruff` for both linting and formatting. All code must pass `ruff check .` and `ruff format .` without errors.
*   **Testing:** Comprehensive tests are crucial. All new features should have associated unit tests, and bug fixes should include tests that demonstrate the fix. Use `Pytest` for all testing.
*   **Modularity:** Follow the **Modular Monolith** architectural pattern. Aim for clear separation of concerns.
*   **AI Integration:** If working with AI components, ensure robust error handling, clear API contracts, and efficient processing. Refer to `AGENTS.md` for specific AI directives.
*   **Documentation:** Document your code thoroughly. Ensure docstrings are present for public functions and classes.
*   **Dependency Management:** Use `uv` for managing dependencies. Avoid direct modifications to `pyproject.toml` unless absolutely necessary for new major dependencies.
*   **Readability:** Prioritize clear, readable, and maintainable code. Follow PEP 8 guidelines where `Ruff` does not enforce a different standard.

## 4. Pull Request Guidelines

*   **Descriptive Titles:** Your pull request title should clearly state the purpose of the changes.
*   **Detailed Descriptions:** Explain *what* the change does and *why* it's needed. Reference any related issues.
*   **Link to Issues:** If your PR closes an issue, use keywords like `Closes #123` in the description.
*   **One PR Per Feature/Fix:** Avoid large, monolithic PRs. Break down changes into smaller, manageable units.
*   **CI Checks:** Ensure all continuous integration checks pass before submitting your PR.

## 5. Reporting Issues

When reporting an issue, please provide as much detail as possible:

*   **Clear Title:** Summarize the issue concisely.
*   **Environment:** Specify your operating system, Python version, and relevant library versions.
*   **Steps to Reproduce:** Provide a step-by-step guide to reproduce the bug.
*   **Expected vs. Actual Behavior:** Clearly describe what you expected to happen and what actually happened.
*   **Screenshots/Logs:** Include relevant screenshots or log output if applicable.

## 6. Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct (version 2.1). Please review the full text here: [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/CODE_OF_CONDUCT.html).

## 7. Thank You!

Thank you for contributing to `PyCentral-Python-Automation-Toolkit`. Your efforts help make this project better for everyone!
