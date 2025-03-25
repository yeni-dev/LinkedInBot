# LinkedInBot Connection Bot

This project is a Python-based LinkedIn automation bot using Selenium for browser automation. The bot automates LinkedIn searches, collects profile links, and displays them in a table. Future updates will add AI for personalized connection messages and intelligent decision-making.

## Features
- ✅ Automated login with cookies for session persistence.
- ✅ Perform LinkedIn searches using specified keywords.
- ✅ Apply search filters to find people.
- ✅ Collect and store profile links.
- ✅ Open and analyze profiles in new tabs.
- ✅ Display results using tabulate for clear viewing.
- ⬜ Intelligent AI-based profile analysis.
- ⬜ Generate personalized connection messages using AI.
- ⬜ Automate connection requests with messages.
- ⬜ Implement error handling and edge case management.

## Roadmap

### Phase 1: Core Automation (Completed)
- ✅ Implement login system using cookies.
- ✅ Perform automated LinkedIn search using input keywords.
- ✅ Apply people filter to narrow results.
- ✅ Scrape profile links.
- ✅ Display links in a formatted table.

### Phase 2: Profile Management (In Progress)
- ✅ Open profiles in new tabs for future data extraction.
- ⬜ Extract relevant profile data using AI.
- ⬜ Analyze and assess profile suitability.
- ⬜ Provide a summary of analyzed profiles.

### Phase 3: Connection Automation (Upcoming)
- ⬜ Generate personalized connection messages using AI.
- ⬜ Send automated connection requests.
- ⬜ Implement connection request tracking.

### Phase 4: Enhancements
- ⬜ Implement AI to detect and avoid bot detection.
- ⬜ Add logging and monitoring features.
- ⬜ Optimize browser management and memory usage.

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/LinkedInConnectionBot.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables by creating a `.env` file with your LinkedIn credentials:
    ```bash
    LINKEDIN_EMAIL=your_email
    LINKEDIN_PASSWORD=your_password
    ```
4. Run the bot:
    ```bash
    python main.py
    ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any feature suggestions or bug fixes.

## License
This project is licensed under the MIT License.

