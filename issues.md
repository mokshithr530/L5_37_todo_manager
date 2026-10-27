# Lab 5: Static Code Analysis — Issue Documentation

**Student Name:** Mokshithreddy Nallaballe  
**SRN:** PES2UG24CS284  
**Assigned Repository:** `L5_37_todo_manager`  
**File Analyzed:** `todo_manager.py`  

---

## 🔍 Identified Issues & Resolution Table

| Issue | Type | Line(s) | Tool | Severity | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Command Injection (CWE-78)** | Security | 57 | Bandit (`B605`) | **High** | `os.system("mail -s ... " + address + " < tasks.json")` executes a shell command with concatenated input, allowing shell injection vulnerabilities. | Eliminated `os.system` invocation; replaced with safe in-process notification logic and safe string formatting without shell interpretation. |
| **Unsafe Deserialization (CWE-502)** | Security | 3, 42, 47 | Bandit (`B403`, `B301`) | **Medium** | `pickle.load()` deserializes arbitrary Python bytecode from untrusted files, risking Remote Code Execution (RCE). | Replaced insecure `pickle` serialization with standard, structured `json.dump` and `json.load`. |
| **Cryptographically Weak Pseudo-Randomness (CWE-330)** | Security | 4, 70 | Bandit (`B311`) | **Low** | `random.choice()` uses Mersenne Twister, which is predictable and flagged for security-sensitive operations. | Replaced `random.choice()` with `secrets.choice()` from Python's standard cryptographic secrets module. |
| **Mutable Default Argument** | Bug / Quality | 11 | Pylint (`W0102`) | **Medium** | `def addTask(..., labels=[])` uses a mutable list default that persists state across consecutive function calls. | Changed default parameter to `labels=None` and initialized `labels = []` inside the function body if `None`. |
| **Non-PEP 8 Naming Conventions** | Style / Quality | 11, 12, 19, 27, 33, 40, 45, 50, 55 | Pylint (`C0103`) | **Low** | CamelCase function and variable identifiers (`addTask`, `completeTask`, `pendingTasks`, `taskId`, `fileName`) violate PEP 8 conventions. | Refactored all function and variable identifiers to snake_case (`add_task`, `complete_task`, `pending_tasks`, `task_id`, `file_name`). |
| **Inconsistent Return Statements** | Quality / Logic | 33-37 | Pylint (`R1710`) | **Low** | `findTask()` returns `taskId` when a match is found but implicitly falls through to `None`, causing inconsistent return signatures. | Added an explicit `return None` statement at the conclusion of the loop when no matching task exists. |
| **Missing File Encodings** | Quality | 41, 46, 51 | Pylint (`W1514`) | **Low** | `open()` invoked without explicitly defining `encoding`, which can cause platform-dependent decoding crashes. | Added explicit `encoding="utf-8"` parameter to all `open()` file context managers. |
| **Missing Module & Function Docstrings** | Documentation | 1, 11, 19, 27, 33, 40, 45, 50, 55, 60 | Pylint (`C0114`, `C0116`) | **Low** | Missing docstrings explaining module purpose, parameters, and return types across all definitions. | Added comprehensive PEP 257 docstrings for the module and all function definitions. |
| **Operator Spacing & Whitespace** | Style | 12, 74 | Flake8 (`E225`, `E231`) | **Low** | Missing whitespace around assignment operator `taskId=...` and after comma `print("...",len(...))`. | Added standard PEP 8 whitespace around assignment operators and after comma delimiters. |
| **Extraneous Blank Lines** | Style | 40 | Flake8 (`E303`) | **Low** | Three consecutive blank lines before function definition, exceeding PEP 8 limits. | Reduced blank lines to the standard 2 blank lines between top-level function definitions. |
| **Inline Comment Formatting** | Style | 69 | Flake8 (`E261`) | **Low** | Inline comment separated by only one space instead of the required minimum of two spaces. | Adjusted inline comment to maintain two leading spaces before the `#` delimiter. |
