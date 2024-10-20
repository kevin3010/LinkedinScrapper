# Job Scraper Project

This is simple project that extract Job details from Linkedin Job URL and return Json object. The code was originally hacked from [JobSpy](https://github.com/Bunsly/JobSpy)

## Prerequisites

- Python 3.11 (Some of the libraries dont work with higher versions)
- `pip` (Python package installer)

## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv .env
    ```

3. **Activate the virtual environment:**

    - On macOS/Linux:

        ```sh
        source .env/bin/activate
        ```

    - On Windows:

        ```sh
        .env\Scripts\activate
        ```

4. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. **Run the main script:**

    ```sh
    python main.py
    ```

    This will execute the job scraper and print the job details from the provided LinkedIn URL.

## Project Structure

- [JobScapper.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FJobScapper.py%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FJobScapper.py%22%2C%22scheme%22%3A%22file%22%7D%7D): Contains the [`JobScrapper`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FJobScapper.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A6%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A23%7D%7D%5D%2C%22e56fa7c7-835f-4ca3-a4ab-a925a3c6135a%22%5D "Go to definition") class which is responsible for scraping job details.
- [jobScrapperUtils.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FjobScrapperUtils.py%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FjobScrapperUtils.py%22%2C%22scheme%22%3A%22file%22%7D%7D): Contains utility classes and functions such as [`RotatingProxySession`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FjobScrapperUtils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A24%2C%22character%22%3A6%7D%7D%5D%2C%22e56fa7c7-835f-4ca3-a4ab-a925a3c6135a%22%5D "Go to definition"), [`RequestsRotating`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FjobScrapperUtils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A45%2C%22character%22%3A6%7D%7D%5D%2C%22e56fa7c7-835f-4ca3-a4ab-a925a3c6135a%22%5D "Go to definition"), [`TLSRotating`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2FjobScrapperUtils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A80%2C%22character%22%3A6%7D%7D%5D%2C%22e56fa7c7-835f-4ca3-a4ab-a925a3c6135a%22%5D "Go to definition"), and logging setup.
- [main.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fkevin%2FProjects%2Fcurrent%2FLinkedinScrapper%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%7D): Entry point of the project which initializes and runs the job scraper.
- `requirements.txt`: Lists all the dependencies required for the project.

