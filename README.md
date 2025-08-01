# AI-Assisted Programmer Roadmap

This roadmap is designed for self-learners who want to become **productive programmers** using AI as a coding assistant.  
It is divided into **4 stages**, each with **clear indicators** to track your progress.

---

## Example Usage
1) Run `table-multiplication.py` (uses default settings).  
2) Run `table-multiplication.py -r 5` (sets the number of rows to 5; number of columns still uses default settings ).  

## **Stage 1: Fundamentals**

**Goal:** Build a strong foundation in programming logic and basic Python.

**Indicators:**
- [v] I can write simple Python scripts without copying from AI.
- [v] I understand variables, loops, and conditions enough to predict code outputs.
- [v] I can read AI-generated code and explain what each line does.
- [v] I can solve basic problems like:
  - **Generate a multiplication table**
  - ~~Count vowels in a string~~
  - ~~Sort a list of numbers~~

**Example Script:**  
- [table-multiplication.py](table-multiplication.py)  
- [table-multiplication.txt](table-multiplication.txt) *(sample output)*

**About the Script:**  
- Generates a multiplication table from **1×1 up to N×M**.  
- Uses **dynamic indent** to format the table neatly.  
- Outputs the table to a `.txt` file.  
- Current version: **1.2**  
  - 1.1 → Static indent  
  - 1.2 → Dynamic indent based on largest cell  
  - 1.3 → *(Planned)* Dynamic indent per column

---

## **Stage 2: Build Small Projects**

**Goal:** Move from theory to small practical projects (50–200 lines).

**Planned Next Steps:**
- [v] Create multiple multiplication tables in one run.  
- [v] Save files with dynamic filenames, e.g., `table_10x5.txt`.  
- [v] Export a CSV version for real-world usage.  
- [v] Start building my first **small project** combining input, file handling, and logic.

### Stage 2.5: Small Project - Multiplication Table CLI Tool

- [v] CLI interface for rows/columns and output format selection  
- [v] Flexible output: text, CSV, or both  
- [v] CSV export uses `csv.writer` with headers  
- [v] Dynamic, descriptive filenames  
- [v] Input validation with clear error messages  
- [v] Logging or status feedback on run  
- [v] Defaults if no arguments provided  
- [v] Self-test or example mode
- [v] Clean function separation (generate, write_text, write_csv, main)  
- [v] Usage example documented in README  
- [?] (Optional) Basic automated test for correctness

---

## **Stage 3: Automation & Data Skills**

**Goal:** Handle real-world data and automate tasks.

**Planned Next Steps:**
- [ ] Read and write CSV files with Python's csv module
- [ ] Read and write Excel files with openpyxl or pandas
- [ ] Clean and transform data (remove duplicates, fix formats)
- [ ] Merge multiple CSV/Excel files into one dataset
- [ ] Fetch data from the web using requests
- [ ] Parse HTML using BeautifulSoup or lxml
- [ ] Automate repetitive file tasks (rename, move, delete files)
- [ ] Schedule scripts to run automatically (cron/Task Scheduler)
- [ ] Create a script that combines data fetching, processing, and saving
- [ ] Document how to run the automation script

---

## **Stage 4: AI + Human Synergy**

**Goal:** Build useful tools that combine automation and AI assistance.

**Planned Next Steps:**
- [ ] Learn how to use an AI API (OpenAI, Hugging Face, etc.)
- [ ] Integrate AI into a Python script to process or generate text
- [ ] Combine Stage 3 automation with AI features
- [ ] Build a CLI, GUI, or web interface for a tool
- [ ] Package the tool so others can use it easily
- [ ] Create a project that solves a real-world problem end-to-end
- [ ] Document the project in README.md with examples and instructions
- [ ] Share the project on GitHub or another platform

---

### ✅ How I Use This Repo
1. **Track my progress** through the stages.  
2. **Check off indicators** as I gain new skills.  
3. **Show my learning journey** with both code and documentation.  

---

Happy coding and growing with AI 🚀