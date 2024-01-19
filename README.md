# SkillTrendScraper
Python web scraper for extracting top job keywords and trends sought by recruiters from job portals.


#### Code folder structure.

```
SkillTrendScraper
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── scraper.py
│   └── utils.py
├── logs/
│   └── scraper.log
├── .gitignore
├── README.md
```


# SkillTrendScraper Details

SkillTrendScraper is a Python web scraper designed to extract top job keywords and trends from job portals. It provides a flexible and configurable solution for collecting valuable insights into recruiter searches.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Scrapes job portals for top keywords and trends used by recruiters.
- Configurable logging and project settings using a YAML configuration file.
- Flexible structure for easy extension and customization.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/SkillTrendScraper.git
   cd SkillTrendScraper
    ```

2. **Install dependencies:**
 
    ```
    pip install -r requirements.txt
    ```

3. **Configuration**

    Modify the conf.yaml file in the root directory to customize logging and project settings.


5. **Usage**

    Run the main script to start the scraping process:

    ```bash
    python main.py
    ```
    The scraper will extract top keywords and trends from the configured job portal.


5. **Contributing**

   Feel free to contribute by opening issues or creating pull requests. Follow the Contributing Guidelines.


6. **License**

    This project is licensed under the MIT License - see the LICENSE file for details.

    ```
    Make sure to replace placeholders like `your-username` with your actual GitHub username. Customize the sections and content based on the specific details of your project. Additionally, consider adding a `CONTRIBUTING.md` file with guidelines for contributors and a `LICENSE` file specifying the project's license terms.
    ```