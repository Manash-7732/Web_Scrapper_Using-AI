# Web_Scrapper_Using-AII

# AI Web Scraper

AI Web Scraper is a web-based tool for scraping and extracting specific information from websites. It leverages **Selenium** for dynamic content retrieval, **BeautifulSoup** for content cleaning, and **LangChain** with **OllamaLLM** for AI-driven content parsing. The project is powered by **Streamlit** to provide an interactive and user-friendly interface.

## Features

- **Web Scraping**: Retrieve webpage content dynamically using Selenium.
- **Content Cleaning**: Use BeautifulSoup to remove unnecessary scripts, styles, and other clutter.
- **AI Parsing**: Extract specific data from cleaned content using LangChain and OllamaLLM.
- **Interactive UI**: Streamlit-based interface for user inputs and results visualization.

## How It Works

1. **Scraping the Website**:
   - The user inputs a website URL.
   - Selenium retrieves the HTML content of the page.

2. **Cleaning the Content**:
   - The page body is extracted using BeautifulSoup.
   - Scripts, styles, and other extraneous elements are removed.

3. **Parsing the Content**:
   - The cleaned content is split into manageable chunks.
   - LangChain's OllamaLLM parses the chunks based on a user-provided description of what to extract.

4. **Displaying the Results**:
   - Results are displayed in the Streamlit app for easy review.

## Requirements

The following dependencies are required to run the project:

## how to run
-streamlit run app.py
