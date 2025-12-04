# PyAutomation-Utility-Scripts-Python-Lib

## 1. APEX ARCHITECT OVERVIEW & INTENT

This repository is designated as a **Retired Product** from the Apex Portfolio, now preserved as a high-value asset named `PyAutomation-Utility-Scripts-Python-Lib`. It houses a mature, curated collection of Python utilities, originally designed for streamlining developer workflows, complex data processing tasks, and general operational automation.

**Purpose:** To serve as a high-quality, modular Python library containing battle-tested scripts for common engineering productivity bottlenecks.

**Status:** Archived (High-Value Reference Asset).

## 2. VISUAL AUTHORITY & STATUS (December 2025 Standard)

<!-- BADGES BLOCK START -->
[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/PyAutomation-Utility-Scripts-Python-Lib/ci.yml?style=flat-square&logo=github)](https://github.com/chirag127/PyAutomation-Utility-Scripts-Python-Lib/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/PyAutomation-Utility-Scripts-Python-Lib?style=flat-square&token=XXXXXXXXX)](https://codecov.io/gh/chirag127/PyAutomation-Utility-Scripts-Python-Lib)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/PyAutomation-Utility-Scripts-Python-Lib?style=flat-square)](https://github.com/chirag127/PyAutomation-Utility-Scripts-Python-Lib)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
<!-- BADGES BLOCK END -->

<br>

⭐ **Star** this Repo if you find these utilities beneficial for your future reference needs!

---

## 3. BLUF: VALUE PROPOSITION

`PyAutomation-Utility-Scripts-Python-Lib` offers a modular Python library providing robust, ready-to-deploy solutions for complex data manipulation, developer workflow automation, and cross-platform scripting tasks, adhering strictly to Pythonic best practices.

## 4. ARCHITECTURAL MAP

The architecture follows a **Modular Monolith** pattern suitable for consumable libraries, ensuring that dependencies are clearly isolated and core logic remains testable and independent.

text
PyAutomation-Utility-Scripts-Python-Lib/
├── core/              # Core processing modules (data transformation, file I/O adapters)
├── data_pipelines/    # Specific, complex ETL/processing workflows
├── cli_tools/         # Entry points for CLI execution (using Click/Typer if applicable)
├── tests/             # Pytest suites for all modules
├── .venv/
├── pyproject.toml     # Project metadata and dependency specification (using uv)
└── README.md


## 5. TABLE OF CONTENTS

1. [APEX ARCHITECT OVERVIEW & INTENT](#1-apex-architect-overview--intent)
2. [VISUAL AUTHORITY & STATUS (December 2025 Standard)](#2-visual-authority--status-december-2025-standard)
3. [BLUF: VALUE PROPOSITION](#3-bluf-value-proposition)
4. [ARCHITECTURAL MAP](#4-architectural-map)
5. [TABLE OF CONTENTS](#5-table-of-contents)
6. [CORE PRINCIPLES & TOOLCHAIN (AGENTS.md Integration)](#6-core-principles--toolchain-agentsmd-integration)
7. [DEVELOPMENT STANDARDS & USAGE](#7-development-standards--usage)
8. [LICENSE](#8-license)

---

## 6. CORE PRINCIPLES & TOOLCHAIN (AGENTS.md Integration)

<details>
<summary>▶️ **APEX AGENT DIRECTIVES & ARCHITECTURE BLUEPRINT**</summary>

### 6.1. SYSTEM IDENTITY & DIRECTIVES

**Role:** Senior Principal Software Architect (40+ Years Experience).
**Prime Directive:** Enforce Zero-Defect, High-Velocity standards. All modules must be traceable, testable, and idempotent where appropriate.

### 6.2. CONTEXT-AWARE APEX TECH STACKS (LATE 2025)

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** Python 3.10+ mandatory. Dependency management via **`uv`** (fast resolver/installer). Linting/Formatting enforced by **`Ruff`** (superset of Pylint/Black/isort).
    *   **Testing:** Comprehensive unit and integration testing using **`Pytest`** exclusively. Mocking via `pytest-mock`.
    *   **Architecture:** **Modular Monolith** adhering to clean separation of core logic from I/O concerns (Ports & Adapters simplified for library structure).

### 6.3. MANDATORY ARCHITECTURAL PATTERNS

1.  **SOLID Principles:** Strictly adhered to, especially Single Responsibility (SRP) for utility functions.
2.  **DRY (Don't Repeat Yourself):** All common logic must be abstracted into the `core/` module.
3.  **YAGNI (You Aren't Gonna Need It):** Avoid over-engineering abstract layers unless immediately required by a complex pipeline.
4.  **Type Hinting:** Full and rigorous static typing using Python's native type system (PEP 484/526).

### 6.4. VERIFICATION COMMANDS (CI/CD Alignment)

To ensure local environment compliance with CI standards:

bash
# 1. Create and activate virtual environment
mkdir .venv && source .venv/bin/activate

# 2. Install dependencies using uv (assuming project setup requires specific tools)
# Note: Actual installation depends on pyproject.toml specifics
python -m uv pip install -e .[dev]

# 3. Check Formatting and Linting (Ruff)
ruff check . --fix
ruff format .

# 4. Run Unit Tests (Pytest)
pytest

# 5. Check Type Compliance (Mypy is often preferred but Ruff handles many checks)
# Assuming mypy is installed as a dev dependency
pytest --mypy


</details>

## 7. DEVELOPMENT STANDARDS & USAGE

### 7.1. LOCAL SETUP (For Reference/Forking)

While this is an archived product, the reference setup is as follows:

bash
# 1. Clone Repository
git clone https://github.com/chirag127/PyAutomation-Utility-Scripts-Python-Lib.git
cd PyAutomation-Utility-Scripts-Python-Lib

# 2. Setup Environment (using recommended uv)
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Dependencies (Dev & Core)
# This assumes a functional pyproject.toml setup for local development
pip install -e .[dev]

# 4. Run Initial Verification (CI Check)
pytest
ruff check .


### 7.2. UTILITY EXECUTION SCRIPTS (Reference)

| Script/Module | Description | Example Invocation |
| :--- | :--- | :--- |
| `core.file_handler` | Robust file reading/writing abstraction. | `python -m core.file_handler read ./data.csv` |
| `data_pipelines.aggregator` | Batch aggregation logic for structured data. | `pytest tests/pipelines/test_aggregator.py` |
| `cli_tools.runner` | Entry point for CLI execution simulation. | `python cli_tools/runner.py --mode process` |

## 8. LICENSE

This repository is licensed under the **CC BY-NC 4.0** license. Attribution is required, and commercial use is strictly prohibited.

See the [LICENSE](LICENSE) file for full details.