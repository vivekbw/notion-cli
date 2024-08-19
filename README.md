# Vivek Bhardwaj | NotionMail

Welcome to my submission for the Notion Take-home project!

## **Table of Contents**

- [Added Features](#improvements-made-added-features)
- [Installation](#installation)
- [Running Testing Suite](#running-tests)
- [Resources Used](#resources-used)
- [Areas of Improvement](#areas-of-improvement-my-wishlist-if-i-had-more-time)
- [Product and Technical Choices](#product-and-technical-choices)

---

Description: NotionMail is a **Python** CLI application that lets a user interact with the Notion API to send, read, and search messages, which are then stored in a Notion Database and have associated timestamps. 

## **Improvement's Made** _(added features!)_

- [x] All messages have timestamps to indicate when a message was sent
- [x] Added a [Testing Suite](#running-tests) to test basic program correctness
- [x] Search through all messages for a given phrase and Delete All Messages
- [x] A quick and easy script (setup.sh) to quickly get going with NotionMail!

---

## **Installation**

1. **Build and run the custom setup executable file:**

```bash
chmod +x setup.sh
./setup.sh
```

This executable is responsible for creating the virtual environment, installing all required packages, creating a template `.env` file, and providing basic startup instructions.

2. **Fill in `NOTION_TOKEN` and Database ID's in the newly created `.env` file:**
   - **Note:** `TEST_DATABASE_ID` is intended to store the `ID` of a separate database specifically for the [Testing Suite](#running-tests)
   - If you wish to use the same database for both the environments, please set `TEST_DATABASE_ID` to the same ID as `PROD_DATABASE_ID`

3. **Run the NotionMail Menu with:**
```bash
python menu.py
```
*Note: Or run `python3 menu.py` otherwise (based on local python config)*

---

## **Running Unit Tests**

The testing suite can be run with:

```bash
pytest
```

---

## **Resources Used**

1. [`click_` open-source Library](https://click.palletsprojects.com/en/8.1.x/)
2. [Notion API - Property Values](https://developers.notion.com/reference/property-value-object#title-property-values)
3. [ISO Time Conversion (Stack Overflow)](https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object)
4. [Subprocesses (for CLI error detection)](https://www.geeksforgeeks.org/python-subprocess-module/)
5. [Google's Python Doc-string Best Practices](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

**Time Spent:**

1. Reading Notion API Docs + Click Library: 20 minutes
2. Basic Features (Send + Read): 40 minutes
3. Search Functionality: 5 minutes
4. Timestamp Feature: 15 minutes
4. Add Testing Suite: 35 minutes
5. `setup.sh` Script File: 10 minutes
6. README writeup: 30 minutes

**Total:** 2 hours, 35 minutes

---

## **Areas of Improvement** _(my wishlist if I had more time!)_

1. **Improved Error Handling** + Expand the breadth and depth of the _testing suite_ by including more edge cases, and coverage for all the different potential inputs and outputs (really long messages, empty messages, API responses, etc.).
2. **Revamp the search feature:** Currently, the program only allows search by a phrase in the message. In the future, I'd like to be able to search by recipient, sender, or even by date range. Furthermore, implementing a better search logic (fuzzy search), would also improve the search experience.
3. **Enhance UX:** Add pagination to make viewing long list of messages more user friendly, introduce color-coded fields, and potentially create a graphical user interface to significantly improve the interface
4. **Caching:** Improve responsiveness and number of calls made to the Notion API (especially for search)

---

## **Product and Technical Choices**
- Having built Python CLI's in the past, one of the most critical technical choices I made here was using the `click_` library for a clean and expandable command-line utility. It's ability to define `arguments` and `commands` with ease made it a really good choice for NotionMail.
- In order to securely store project secrets like the Notion API token and database ID's, I used the `dotenv` library to load environment variables from a `.env` file.
- For improved technical onboarding to the CLI, I created a custom script `(setup.sh)` to make the user's ability to setup this project easier.
- Timestamp formatting was also added as a product choice because reading the ISO 8601 format time stamps are really hard for the user, and thus the `format_timestamp` function converts it to a readable format
- Given that the testing suite will be run very often, another technical choice I made was using separate databases for the testing suite vs. when using NotionMail generally (demonstrated in attached video).
- Unit tests were created with the help of `CliRunner` to create a simulation of CLI commands and their correctness.
- Modular Code Design: To ensure code maintainability, I separated API interactions in the `notion_wrapper.py` file, and CLI interface commands in `cli.py`
- Python Doc-strings were added based on industry standards (source: Google)