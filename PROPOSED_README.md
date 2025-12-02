# PyCentral-Python-Automation-Toolkit

<!-- HERO BANNER / LOGO: Replace with high-resolution project logo -->
<p align="center">
  <img src="https://raw.githubusercontent.com/chirag127/PyCentral-Python-Automation-Toolkit/main/assets/pycentral-hero.svg" alt="PyCentral Toolkit Hero Banner" width="100%"/>
</p>

<p align="center">
  <a href="https://github.com/chirag127/PyCentral-Python-Automation-Toolkit/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/chirag127/PyCentral-Python-Automation-Toolkit/ci.yml?branch=main&style=flat-square&label=Build%20Status" alt="Build Status">
  </a>
  <a href="https://codecov.io/gh/chirag127/PyCentral-Python-Automation-Toolkit">
    <img src="https://img.shields.io/codecov/c/github/chirag127/PyCentral-Python-Automation-Toolkit?style=flat-square&token=PYCENTRALCODECOV" alt="Code Coverage">
  </a>
  <a href="https://github.com/chirag127/PyCentral-Python-Automation-Toolkit/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg?style=flat-square" alt="License">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blueviolet?style=flat-square&logo=python" alt="Python Version">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/badge/Linter-Ruff-6E40A8?style=flat-square&logo=ruff" alt="Ruff Linter">
  </a>
  <a href="https://github.com/chirag127/PyCentral-Python-Automation-Toolkit/stargazers">
    <img src="https://img.shields.io/github/stars/chirag127/PyCentral-Python-Automation-Toolkit?style=flat-square" alt="GitHub Stars">
  </a>
</p>

***

> **⚡ Star ⭐ this repository** to track updates and support the development of high-velocity Python utilities.

## 💡 Project Overview: The Apex Automation Engine

**PyCentral** is the definitive, curated collection of professional-grade Python scripts for comprehensive automation, robust data processing, and general utility tasks. Engineered to the highest software architecture standards, this toolkit ensures repeatability, performance, and maintainability across diverse operational workflows, from desktop scripting to enterprise data pipelines.

This project serves as a foundational **Modular Monolith**, providing high-cohesion, low-coupling utilities ready for deployment or integration into larger systems.

## 🗺️ System Architecture

PyCentral adheres to a **Modular Monolith** pattern, segregating functionalities into distinct, independent packages (modules) accessible via a unified CLI and core library. This structure ensures clear domain separation and simplifies testing.

mermaid
C4Context
title PyCentral Architecture Overview

System_Boundary(pyc, "PyCentral Toolkit") {
    Container(cli, "CLI Interface", "Python/Click", "Entry point for all user interactions and scripts.")
    Container(core, "Core Utilities Module", "Python Libraries", "Reusable functions for file I/O, logging, configuration, and environment management.")
    Container(data_proc, "Data Processing Module", "Pandas/NumPy/uv", "Specialized modules for cleaning, transformation, and analysis of structured data.")
    Container(automation, "Automation & Scripting Module", "OS/System APIs", "Task-specific scripts (e.g., file reorganization, scheduled tasks, API polling).")
}

System(user, "Developer/User", "Interacts via the CLI or imports PyCentral as a library.")

Rel(user, cli, "Executes commands")
Rel(cli, core, "Uses core services")
Rel(cli, data_proc, "Invokes data tasks")
Rel(cli, automation, "Runs utility scripts")
Rel(data_proc, core, "Relies on data validation and logging")




## 📋 Table of Contents

1.  [Project Overview: The Apex Automation Engine](#-project-overview-the-apex-automation-engine)
2.  [System Architecture](#-system-architecture)
3.  [AI Agent Directives (Architectural Principles)](#-ai-agent-directives-architectural-principles)
4.  [Getting Started](#-getting-started)
5.  [Development and Quality Assurance](#-development-and-quality-assurance)
6.  [License](#-license)


***

## 🤖 AI Agent Directives (Architectural Principles)

<details>
<summary><strong>📐 SYSTEM SPECIFICATION: ARCHITECTURAL MANDATES FOR AI/DEVELOPER COGNITION</strong></summary>

This project operates under the **Apex Technical Authority** standard (December 2025). All future modifications, features, and refactoring efforts must align with the following principles derived from the project's foundational `AGENTS.md`.

### 1. Technology Stack & Toolchain

| Component | Tool / Standard | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Strict type hinting (mypy integration planned). |
| **Package Manager** | `uv` | Used for ultra-fast dependency resolution, environment management, and virtual environment creation. |
| **Linting/Formatting** | `Ruff` | Strict adherence to Ruff defaults. Pre-commit hooks are mandatory for formatting checks. |
| **Testing Framework** | `Pytest` | All units must be tested; required code coverage minimum is **95%**. |
| **CI/CD** | GitHub Actions | Automated build, lint, format, and test on all pushes to `main` and all Pull Requests. |

### 2. Architectural Principles

*   **Modular Monolith:** Maintain strict separation between `core`, `data_processing`, and specific `scripts`. Modules must interact through explicit interfaces to maintain low coupling.
*   **SOLID & DRY:** Strict adherence. Avoid global state and ensure every function has a single responsibility.
*   **Configuration Management:** All configuration must be externalized (e.g., `.ini`, environment variables, or dedicated `pycentral.config`). No hardcoding of paths or parameters.
*   **Idempotency:** Where feasible (especially in data transformation and file operations), scripts must be idempotent (running the script multiple times yields the same final result).

### 3. Verification & Execution Commands

Agents and developers must use the following commands for consistency and quality assurance:

| Task | Command | Description |
| :--- | :--- | :--- |
| **Setup Environment** | `uv venv` | Create and activate the virtual environment. |
| **Install Dependencies** | `uv sync` | Install or synchronize dependencies from `requirements.txt`. |
| **Run Tests (Full)** | `pytest --cov=pycentral` | Execute all unit and integration tests with coverage reporting. |
| **Lint & Format Check** | `ruff check .` | Run linting checks without fixing. |
| **Apply Formatting Fixes** | `ruff check --fix .` | Automatically fix formatting and trivial linting issues. |
| **Execute CLI Entry** | `python -m pycentral [command]` | Run the primary application entry point. |

</details>

***

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.10 or higher installed, along with `uv` (recommended package manager).

bash
# Install uv globally (if not already present)
curl -LsSf https://astral.sh/uv/install.sh | sh


### Local Setup

1.  **Clone the Repository:**
    bash
    git clone https://github.com/chirag127/PyCentral-Python-Automation-Toolkit.git
    cd PyCentral-Python-Automation-Toolkit
    

2.  **Initialize Environment & Install Dependencies:**
    bash
    # Create a virtual environment using uv
    uv venv
    source .venv/bin/activate
    
    # Install required dependencies
    uv sync
    

3.  **Run a Utility Test:**
    bash
    # Example: Run the core system check
    python -m pycentral info
    

## 🛠️ Development and Quality Assurance

PyCentral maintains stringent QA standards enforced by automated workflows.

| Script Command | Description | Tool | Target |
| :--- | :--- | :--- | :--- |
| `uv sync --dev` | Install development dependencies (Ruff, Pytest, coverage). | `uv` | Environment Setup |
| `ruff check .` | Execute fast linting and code analysis checks. | `Ruff` | Quality Control |
| `ruff format .` | Apply automatic code formatting corrections. | `Ruff` | Consistency |
| `pytest` | Run the standard unit and integration test suite. | `Pytest` | Verification |
| `pytest --cov` | Run tests and generate code coverage report. | `Coverage.py` | Metrics |

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License. See the [LICENSE](LICENSE) file for details.