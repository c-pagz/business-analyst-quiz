# business-analyst-quiz

## Introduction 
Working within a public-sector consulting environment has taught me about how influential my work handling data and service delivery directly affects the clients work, as well as other key stakeholders. As a business analyst (BA), my role involves engaging with stakeholders through user sessions where I understand the as-is process of the business process, and these are then documented and translated into clear requirements. Much of this works on strong foundational skills and knowledge, such as how to handle confidential information and how to apply core BA techniques to support decision making.

The workplace environment I operate in is highly collaborative, receiving input from both colleagues and clients, and is very dynamic. Projects often involve multiple teams, each with different levels of technical understanding and exposure to data. Because of this, there is a continuous need for accessible learning tools to reinforce good practice, especially in areas such as ethical data handling, process awareness and basic analytical thinking. These topics underpin the conversations I have with colleagues and stakeholders, whether during a user story walkthrough or process mapping sessions - all tailored towards a starting business analyst. From my own experience starting in this role, I realised how much quicker my confidence would have grown if I’d had simple tools like this to reinforce the basics. If I were starting again, a quiz like this would have helped kick‑start my understanding of a my new business analyst role. My proposed MVP is a simple interactive quiz application, which addresses this and provides a lightweight, engaging way for staff to test and reinforce their understanding of these core concepts. The quiz focuses on ethics and data awareness, alongside basic BA tools and process-mapping principles. These areas were chosen because they represent everyday responsibilities within public-sector projects, yet they are often misunderstood or inconsistently applied. By presenting a mix of knowledge and scenario-based questions, the quiz encourages users to think about their own role - a significant aspect for employees within foundation.

## GUI Design (Figma Prototype)
The planned user interface follows a simple, linear user journey designed to make the quiz easy to understand and navigate. The flow consists of four core screens:

1. Home Screen – introduces the quiz, prompts the user to enter their name and provides a clear “Start Quiz” button.
2. Question Screen – displays one multiple‑choice question at a time, with clearly separated answer options and a progress indicator.
3. Results Screen – shows the user’s score, displays a piece chart and provides an option to export or restart.
4. Data Export Screen – allows users to save their results to a CSV file.

The design uses a clean layout with large buttons, high‑contrast colours, and minimal text to support accessibility. The screenshots are provided here below:

## Functional Requirements
* Start the quiz from the home screen.
* Load questions from a CSV file.
* Display one question at a time with multiple‑choice answers.
* Validate user selections and track correct answers.
* Show final score at the end of the quiz.
* Allow exporting results to a CSV file.
* Store quiz data persistently so results can be reviewed later.
* Handle invalid inputs gracefully (e.g., empty CSV, missing fields).

## Non‑Functional Requirements
* Engagement through design - clear layouts, consistent spacing, and visually distinct buttons 
* Usability - simple, intuitive interface suitable for non‑technical staff.
* Accessibility - readable fonts, high contrast, keyboard‑friendly navigation.
* Performance - questions load instantly; no noticeable delays.
* Reliability - quiz should run without crashing or losing progress.
* Maintainability - code structured using classes and pure functions.
* Portability - runs on any machine with Python installed.

## Tech Stack Outline
* Language: Python
* GUI Framework: Streamlit (lightweight, built‑in, ideal for MVPs)
* Data Storage: CSV files for questions and results
* Version Control: Git + GitHub repository
* Documentation: Markdown README, docstrings, inline comments
* Testing: Python unittest for pure functions (e.g., answer validation)
If you want alternatives, explore GUI framework comparisons.
