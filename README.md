# business-analyst-quiz

## Introduction 
Working within a public-sector consulting environment has taught me about how influential my work handling data and service delivery directly affects the clients work, as well as other key stakeholders. As a business analyst (BA), my role involves engaging with stakeholders through user sessions where I understand the as-is process of the business process, and these are then documented and translated into clear requirements. Much of this works on strong foundational skills and knowledge, such as how to handle confidential information and how to apply core BA techniques to support decision making.

The workplace environment I operate in is highly collaborative, receiving input from both colleagues and clients, and is very dynamic. Projects often involve multiple teams, each with different levels of technical understanding and exposure to data. Because of this, there is a continuous need for accessible learning tools to reinforce good practice, especially in areas such as ethical data handling, process awareness and basic analytical thinking. These topics underpin the conversations I have with colleagues and stakeholders, whether during a user story walkthrough or process mapping sessions - all tailored towards a starting business analyst. 

From my own experience starting in this role, I realised how much quicker my confidence would have grown if I’d had simple tools like this to reinforce the basics. If I were starting again, a quiz like this would have helped kick‑start my understanding of a my new business analyst role. My proposed MVP is a simple interactive quiz application, which addresses this and provides a lightweight, engaging way for staff to test and reinforce their understanding of these core concepts. The quiz focuses on ethics and data awareness, alongside basic BA tools and process-mapping principles. These areas were chosen because they represent everyday responsibilities within public-sector projects, yet they are often misunderstood or inconsistently applied. By presenting a mix of knowledge and scenario-based questions, the quiz encourages users to think about their own role - a significant aspect for employees within foundation.

## GUI Design (Figma Prototype)
The planned user interface follows a simple, linear user journey designed to make the quiz easy to understand and navigate. The flow consists of four core screens:

1. Home Screen – introduces the quiz, prompts the user to enter their name and provides a clear “Start Quiz” button.
2. Question Screen - displays one multiple‑choice question at a time, with clearly separated answer options and a progress indicator.
3. Results Screen – shows the user’s score, displays a piece chart and provides an option to export or restart.
4. Data Export Screen – allows users to save their results to a CSV file.

The design uses a clean layout with large buttons, high‑contrast colours, and minimal text to support accessibility. The screenshots are provided here below:


## Functional Requirements

| ID | Requirement Specification | Area Covered |
|----|---------------------------|--------------|
| FR‑1 | Start the quiz from the home screen | User Flow |
| FR‑2 | Load questions from a CSV file | Data Handling |
| FR‑3 | Display one question at a time with multiple‑choice answers | User Interface |
| FR‑4 | Validate user selections and track correct answers | Logic / Scoring |
| FR‑5 | Show final score at the end of the quiz | Output / Feedback |
| FR‑6 | Allow exporting results to a CSV file | Data Export |
| FR‑7 | Store quiz data persistently so results can be reviewed later | Data Persistence |
| FR‑8 | Handle invalid inputs gracefully (e.g., empty CSV, missing fields) | Error Handling |

## Non‑Functional Requirements

| ID | Requirement Specification | Area Covered |
|----|---------------------------|--------------|
| NFR‑1 | Engagement through design – clear layouts, consistent spacing, visually distinct buttons | Engagement / UI |
| NFR‑2 | Usability – simple, intuitive interface suitable for non‑technical staff | Usability |
| NFR‑3 | Accessibility – readable fonts, high contrast, keyboard‑friendly navigation | Accessibility |
| NFR‑4 | Performance – questions load instantly with no noticeable delays | Performance |
| NFR‑5 | Reliability – quiz should run without crashing or losing progress | Reliability |
| NFR‑6 | Maintainability – code structured using classes and pure functions | Maintainability |
| NFR‑7 | Portability – runs on any machine with Python installed | Portability |


## Tech Stack Outline
* Language: Python
* GUI Framework: Streamlit (lightweight, built‑in, ideal for MVPs)
* Data Storage: CSV files for questions and results
* Version Control: Git + GitHub repository
* Documentation: Markdown README, docstrings, inline comments
* Testing: Python unittest for pure functions (e.g., answer validation)
If you want alternatives, explore GUI framework comparisons.

## Testing Section 


## Documentation Section 
User Documentation
This quiz application is designed for staff within the organisation to quickly test their knowledge of business‑analysis concepts in a simple and intuitive way. The interface is built using Streamlit, meaning it runs in a web browser and requires no technical skills.

#### How to Use the Quiz
1. Open the application When launched, the quiz opens in your browser and displays a welcome screen.
2. Enter your name Your name is used to save your results for later review.
3. Start the quiz Select the Start Quiz button to begin.
4. Answer each question
    * One question appears at a time
    * Select one of the multiple‑choice options
    * The next question loads automatically
5. View your results At the end of the quiz, you will see:
    * Your score
    * A breakdown of correct/incorrect answers
    * A results chart
    * A personalised message based on your performance
6. Download your results You can export your score to a CSV file for training records.
7. Restart the quiz Select Restart Quiz to try again.
This workflow ensures the quiz is accessible to non‑technical staff, with clear navigation and minimal steps.

### Technical Documentation
This section explains how developers, maintainers, or assessors can run, test, and understand the codebase.

### Project Structure
business-analyst-quiz/

| File             | Description         |
|------------------|---------------------|
| main.py          | Streamlit UI        |
| quiz.py          | Quiz logic          |
| question.py      | Question model      |
| data_manager.py  | CSV loading/saving  |
| questions.csv    | Quiz questions      |
| results.csv      | Saved results       |
| test_quiz.py     | Unit tests          |


### How to Run the Application
1. Install dependencies:
pip install streamlit pandas matplotlib
1. Run the application:
streamlit run main.py
This launches the quiz in your browser.

### Running Unit Tests
Unit tests are located in test_quiz.py and use Python’s built‑in unittest framework.
Run all tests with:
python3 -m unittest test_quiz.py
These tests validate:
* Quiz scoring logic
* Question progression
* Reset behaviour
* Correct vs incorrect answer handling
Screenshots of passing tests should be included in the README as evidence.

### Code Explanation
question.py
Defines the Question class, which stores:
* question text
* four answer options
* the correct answer
* a method to check correctness

### quiz.py
Controls quiz flow:
* tracks current question
* updates score
* moves to next question
* resets the quiz
* exposes helper methods for UI

### data_manager.py
Handles:
* loading questions from questions.csv
* saving results to results.csv

### main.py
Implements the Streamlit interface:
* welcome screen
* question display
* answer buttons
* results screen
* pie chart visualisation
* CSV export

### Running Tests in Continuous Integration (CI)
The project supports CI pipelines such as GitHub Actions. A CI workflow can automatically:
* install dependencies
* run unit tests
* block merges if tests fail
This ensures the quiz remains reliable as new features are added.
If you want, I can generate a ready‑to‑use GitHub Actions CI YAML file.

## Evaluation Section 
