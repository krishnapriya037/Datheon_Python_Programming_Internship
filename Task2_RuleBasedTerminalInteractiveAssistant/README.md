# Rule-Based Interactive Terminal Assistant

## Description

A Python-based chatbot that interacts with users through the terminal. It uses predefined rules and keyword matching to respond to greetings and frequently asked questions related to internship support.

## Features

* Recognizes common greetings.
* Answers frequently asked questions using a JSON dataset.
* Matches keywords in user queries.
* Provides a fallback response for unrecognized questions.
* Supports exit commands such as `bye`, `exit`, and `quit`.
* Handles missing dataset files and keyboard interruptions.

## Technologies Used

* Python
* JSON
* Regular Expressions

## Project Structure

```text
my_chatbot/
├── chatbot.py
├── data/
│   └── faq.json
└── README.md
```

## Requirements

* Python 3.7 or later
* No external libraries required.

## How to Run

1. Open a terminal in the `my_chatbot` directory.

2. Run the following command:

   ```bash
   python chatbot.py
   ```

3. Enter a greeting or question to interact with the chatbot.

4. Type `bye`, `exit`, or `quit` to end the conversation.

## Dataset

The `data/faq.json` file contains predefined greetings and frequently asked questions with their corresponding answers.

## Author

Krishnapriya P
