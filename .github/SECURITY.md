# Security Policy for PyCentral-Python-Automation-Toolkit

As a project managed by the Apex Technical Authority, security is treated as a **First-Class Citizen** throughout the entire development lifecycle. This toolkit adheres to Zero-Defect, Future-Proof standards, prioritizing dependency safety and secure coding practices.

## 1. Supported Versions

This repository actively supports the **latest stable release of Python (3.10+)** and maintains a strictly pinned dependency list managed via `uv`. We aim to patch critical vulnerabilities within 7 days of disclosure, provided a viable patch exists within the upstream libraries.

## 2. Vulnerability Reporting

We welcome responsible disclosure of security vulnerabilities. Please follow the process below to ensure prompt and effective remediation.

**DO NOT** report security issues through public GitHub Issues or Discussions. This ensures your report remains private until remediation is complete.

### Reporting Steps

1.  **Email Primary Maintainer:** Send a detailed report to `security@chirag127.dev` (placeholder for a real security contact, use `chirag127@users.noreply.github.com` if an alias is not available).
2.  **Encryption:** If the vulnerability is severe (e.g., RCE in a core script), consider using PGP encryption for the payload.
3.  **Include Details:** Your report **MUST** include:
    *   A clear, step-by-step description of how to reproduce the vulnerability.
    *   The affected script name(s) or feature(s).
    *   The potential impact (e.g., Data exposure, Denial of Service).
    *   Suggested remediation (if known).

## 3. Our Security Commitment (Apex Directives)

Our security posture is defined by proactive measures, deeply integrated into our CI/CD pipeline (`.github/workflows/ci.yml`):

*   **Dependency Scanning:** We mandate the use of tools like `safety` or integrated GitHub Dependabot scanning (managed via `badges.yml` configuration) to check all Python dependencies against known CVEs upon every push to the main branch.
*   **Static Analysis (Ruff):** All code is subjected to rigorous linting via **Ruff** with strict configuration, catching common security anti-patterns (e.g., use of `pickle` with untrusted data, insecure temporary file creation).
*   **Principle of Least Privilege:** All utility scripts are designed to operate only on the resources explicitly required for their function. Sensitive operations (API key handling) are isolated and environment-variable dependent.
*   **Input Validation:** For any script interacting with external data sources (files, network, or the Google Gemini API), robust validation layers are architected following **SOLID** principles, ensuring no untrusted input bypasses sanitation checks.

## 4. Remediation Timeline

Upon receiving a valid report, we adhere to the following timeline:

| Severity | Target Triage Time | Target Fix Time |
| :--- | :--- | :--- |
| **Critical** (RCE, PII Leak) | 24 Hours | 7 Days |
| **High** (Auth Bypass, Major DoS) | 48 Hours | 14 Days |
| **Medium** (Minor Info Leak) | 3 Days | 30 Days |
| **Low/Informational** | 7 Days | Next Major Release |

*Note: These timelines apply to the main branch only. Patches for older, deprecated versions may be handled on a best-effort basis.*

--- 

*This security policy is subject to periodic review under the direction of the Apex Technical Authority.* 