# Financial Chatbot Prototype – Documentation

## 1. Overview

This chatbot prototype was developed as part of the BCG GenAI simulation.  
Its purpose is to demonstrate how rule-based logic can be used to transform structured financial data into interactive responses.

The chatbot responds to a predefined set of financial queries using simple if-else logic in Python.

---

## 2. How the Chatbot Works

The chatbot is implemented in `src/chatbot.py`.

Logic Flow:

1. The user runs the script using:
   python src/chatbot.py

2. The chatbot prompts the user to enter a predefined financial question.

3. The script uses if-elif-else statements to:
   - Match the user’s query
   - Return a predefined response based on the analyzed financial data

4. If the query does not match any predefined question, the chatbot returns:
   "Sorry, I can only provide information on predefined queries."

---

## 3. Predefined Queries Supported

The chatbot currently supports the following queries:

1. What is the total revenue for 2025?
2. How has net income changed from 2024 to 2025?
3. Which company had the highest revenue in 2025?
4. Which company had the highest net income in 2025?

These responses are based on financial data extracted from 10-K filings for:

- Microsoft
- Tesla
- Apple

---

## 4. Limitations

This is a simplified prototype with the following limitations:

- It only responds to exact predefined queries.
- It does not perform dynamic natural language understanding.
- It does not retrieve data dynamically from the dataset (responses are hardcoded).
- It does not maintain conversational context.
- It does not use machine learning or advanced NLP techniques.

This prototype demonstrates the foundational rule-based logic layer of a financial AI chatbot.

---

## 5. Future Improvements

Future improvements could include:

- Dynamic retrieval of data using pandas instead of hardcoded values.
- Basic natural language parsing for flexible queries.
- Integration with an LLM for improved conversational capabilities.
- Web interface using Flask for improved user experience.