# Harbor Task: JSON-to-CSV Data Processor

## Reference

## New Hire Assignment: Create a Harbor Task : https://docs.google.com/document/d/1ud5mSZ81ON3LVHJtyemIaF81CNKZrFzL7WglR_hVhjU/edit?tab=t.b7k05m525zmc
## Harbor Task Creation - Quick Reference Cheat Sheet : https://docs.google.com/document/d/1ud5mSZ81ON3LVHJtyemIaF81CNKZrFzL7WglR_hVhjU/edit?tab=t.0

## 🌌 Project Overview
This project is an **AI Evaluation Task** built for the **Harbor Framework**. It simulates a Real-World Data Engineering scenario where an AI agent must process structured data in a sandboxed environment.

### 🎯 Key Objective
Create a task that validates an AI agent's ability to:
1.  Navigate a Linux filesystem.
2.  Parse structured JSON data.
3.  Perform conditional filtering (Business Logic).
4.  Export data to a standardized CSV format.

---

## 🏗️ Folder Structure Explanation
The repository follows the strict 5-layer requirement for Harbor Tasks:

| Folder/File | Purpose |
| :--- | :--- |
| `task.toml` | **Metadata**: Defines difficulty (Easy), category (Data Processing), and resource limits. |
| `instruction.md` | **Agent Instruction**: The prompt used by the AI to understand the task. Uses absolute paths. |
| `environment/`| **Sandboxing**: Contains the `Dockerfile` and `input.json`. This is the ONLY folder the agent "lives" in. |
| `solution/` | **Oracle Solution**: Contains `solve.sh` - the perfect reference solution used to grade agents. |
| `tests/` | **Validation**: Contains automated Pytest scripts to verify the agent's output is 100% accurate. |

---

## 🌐 Domains & Skills Used
*   **AI Benchmarking:** Creating standardized tests for Large Language Models (LLMs).
*   **ETL (Extract, Transform, Load):** Transforming raw JSON data into clean CSV reports.
*   **DevOps:** Docker containerization for secure, isolated code execution.
*   **Data Science / Python:** Using `Pandas` and `JSON` libraries for high-performance data handling.
*   **Shell Scripting:** Automating environment setup and solution execution.

---

## 🛠️ Modules & Dependencies
*   **Docker:** Containerization engine.
*   **Python 3.11:** Core execution language.
*   **Pytest:** Framework for automated verification.
*   **Pandas:** Library for CSV verification and data manipulation.
*   **Bash:** For orchestration scripts.

---

## 🚀 Working Structure (How to Run)
1.  **Initialize Environment:** Harbor builds the `environment/Dockerfile` creating a clean Linux workspace.
2.  **Input Injection:** A JSON file with 20 users is mounted at `/app/input.json`.
3.  **Agent Execution:** The AI Agent (or Oracle) reads instructions and writes `output.csv`.
4.  **Verification:** The `test_outputs.py` script runs inside the container, checking:
    *   If `output.csv` exists.
    *   If exactly 12 active users are filtered from the 20 inputs.
    *   If the headers match `name,email`.

---

## 📥 Output Screenshot / Verification
When the task is solved, the resulting CSV looks like this:
```csv
name,email
name,email
Manikandan,manikandan@example.com
Fam,Fam@example.com
Riched,riched@example.com
Donna Paulsen,donna@example.com
Jessica Pearson,jessica@example.com
Katrina Bennett,katrina@example.com
Samantha Wheeler,samantha@example.com
Sheila Sazs,sheila@example.com
Gretchen Bodinski,gretchen@example.com
Harold Gunderson,harold@example.com
Benjamin Sisko,benjamin@example.com
Odo Constable,odo@example.com
```
Validated with: `pytest tests/test_outputs.py` → **3 Passed**.
