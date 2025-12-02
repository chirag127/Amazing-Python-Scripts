# 🐛 Bug Report: System Integrity Alert

Thank you for identifying a potential deviation from the Zero-Defect standard. Please provide exhaustive detail below so the Apex Architecture team can rapidly deploy a patch.

---

## 1. Executive Summary (BLUF)

> **In one sentence, what is the observable defect?**

---

## 2. Environment Specification

To ensure accurate replication and patching, document the exact execution context.

*   **Repository Component/Script:** (e.g., `utils/data_cleaner.py`, `Notebook_03_ML_Training.ipynb`)
*   **Python Version:** (e.g., 3.11.5)
*   **Operating System:** (e.g., Linux Kernel 6.5, Windows 11, macOS Sonoma)
*   **Relevant Dependency Versions:** (List critical packages and their versions, e.g., `gemini-sdk==1.5.1`, `pandas==2.2.0`)

---

## 3. Detailed Defect Analysis

### 3.1. Steps to Reproduce

List the minimal, sequential actions required to trigger this failure. Be precise.

1.  Clone/checkout the repository (Specify commit SHA if applicable: `ABC123XYZ`).
2.  Execute the command or run the notebook cell:
    bash
    [Paste exact command line invocation here, e.g., python src/main.py --mode=batch]
    
3.  Observe the failure.

### 3.2. Expected Behavior

What was the system **designed** to do according to the architectural documentation?

---

### 3.3. Actual Behavior (The Failure Mode)

What did the system *actually* do? Include relevant error messages, stack traces, or unexpected output here. **Crucially, wrap tracebacks in triple backticks.**

text
[Paste Console Output or Stack Trace Here]


---

## 4. Verification & Compliance Check

As per Apex Protocol, please confirm the following:

*   [ ] I have verified this issue persists after running `ruff check`.
*   [ ] I have verified this issue persists after running the relevant `pytest` suite (if applicable to the script).
*   [ ] I have checked the latest `main` branch to ensure this isn't a stale issue.

## 5. Attachments (Optional)

If applicable, attach configuration files or truncated data samples necessary for debugging. Avoid sensitive data.
