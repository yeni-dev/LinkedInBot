# LinkedIn Automation Tool

## Overview
This demonstration project is a Python-based automation tool that interacts with LinkedIn using Selenium and `webdriver`. Its core functionality is automating connection requests to LinkedIn profiles based on search terms, with randomized delays to mimic human interaction and reduce detection risk.

The script:
- Logs into LinkedIn using stored credentials or session cookies.
- Performs searches for specified keywords.
- Filters results to "People."
- Iterates through search result pages, automatically sending connection requests.
- Implements runtime limits, randomized typing, and scrolling delays for stealth.

## Features
- **Cookie-Based Login**: Saves and reuses session cookies to avoid repeated credential entry.
- **Search Automation**: Randomly selects from a list of keywords and performs searches.
- **Connection Automation**: Automatically clicks "Connect" buttons and confirms requests.
- **Stealth Mode**: Randomized typing, delays, and scrolling patterns to simulate human behavior.
- **Error Handling**: Handles modal dialogs, missing buttons, and timeouts gracefully.
- **Runtime Control**: Restricts automation to a defined duration (default: 10 minutes).

## Potential Future Features
- **Job Search Automation**  
  Automate job searches with filters (e.g., location, remote, experience level) and export results.
- **Auto-Messaging**  
  Send customized introductory messages with connection requests.
- **Profile Scraping**  
  Extract structured data (name, title, location, company) for analysis or lead generation.
- **Connection Management**  
  Track who accepted requests and maintain connection growth analytics.
- **Integration with Databases/CRMs**  
  Store contacts and job listings directly into databases or CRM systems.
- **GUI Dashboard**  
  Build a simple interface for non-technical users to configure searches and view results.


## Installation
1. Clone the repository and navigate into it:
   bash
   git clone https://github.com/yeni-dev/LinkedInTool.git && cd LinkedInTool


2. Install the required dependencies:

   bash
   pip install -r requirements.txt

3. Create a `.env` file in the project root and add your LinkedIn credentials:
   
   LINKEDIN_EMAIL=your_email
   
   LINKEDIN_PASSWORD=your_password
  
5. Run the tool:

   bash
   python3 linkedin_tool.py
   

