# Setup Instructions

This document provides detailed instructions for setting up your environment to use the data validation and quality control scripts for the OWASP Top 10 for LLM AI Applications project. Follow these steps to prepare your system for running the provided Python scripts.

## Prerequisites

Ensure you have the following installed on your system before proceeding:

- Python 3.8 or higher: [Download Python](https://www.python.org/downloads/)
- pip: Should be installed with Python 3.4 or higher

## Installation

1. **Clone the Repository**

   First, clone the project repository to your local machine using Git:

2. **Create a Virtual Environment**

Navigate to the project directory and create a virtual environment:


3. **Activate the Virtual Environment**

- On Windows:

  ```
  .\venv\Scripts\activate
  ```

- On Unix or MacOS:

  ```
  source venv/bin/activate
  ```

4. **Install Required Libraries**

Install all the necessary Python libraries as specified in `requirements.txt`:


## Adapting the Scripts

To adapt the validation and quality control scripts to your specific dataset and environment, follow these guidelines:

- Review each script in the `src` directory to understand its functionality.
- Modify parameters, thresholds, and checks within each script as needed to suit your data characteristics.
- For adding custom validation checks, refer to the script documentation in the `docs` folder for guidance on extending script capabilities.

## Running the Scripts

To run a specific script, use the following command from the project root directory:


Replace `yourscriptname.py` with the name of the script you wish to run. Ensure your dataset files are placed in the designated input directories as per the script documentation.

## Troubleshooting

If you encounter any issues during setup or while running the scripts, please open an issue on the project GitHub page.

Thank you for contributing to the security and reliability of LLM AI applications.
