# Multimodal Testing Instruction Generator

- This project demonstrates a tool that generates detailed testing instructions based on screenshots and optional context using a multimodal LLM (Large Language Model). It provides a step-by-step guide to test various features of digital products.

## Features

- Upload multiple screenshots for analysis.
- Optional text input to provide additional context.
- Detailed test case generation including:
  - Description
  - Pre-conditions
  - Testing steps
  - Expected results

## Project Overview

This tool is designed to simplify the process of creating test cases for digital products by analyzing screenshots and generating clear, comprehensive testing instructions. It is particularly useful for quality assurance teams and developers who need to test various functionalities of an app or a website.

The project demonstrates its functionality using the **Red Bus** mobile app's features such as:
- Source, Destination, and Date Selection
- Bus Selection
- Seat Selection
- Pick-up and Drop-off Point Selection
- Offers, Filters, and Bus Information

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multimodal-testing-instruction-generator.git
   cd multimodal-testing-instruction-generator

## Installation

2. **Install Required Dependencies**
  - Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt

   ```
## Set up your environment variables:

3. **File**
 -  Ensure you have Python installed, then run:
   ```bash
  MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
   ```
4. **Run the app:**
  - Ensure you have Python installed, then run:
   ```bash
   python app.py
```
5.**Output**
- Open your browser and navigate to **http://localhost:5000**  to start using the app.

## How It Works
- 1.Upload multiple screenshots from your digital product.
- 2.Optionally, provide a brief description or context of the feature you're testing.
- 3.Click the Describe Testing Instructions button.
- 4.The backend processes the screenshots and generates a detailed step-by-step guide for testing each feature.
- 5.The output includes:
   - Test case descriptions
   - Pre-conditions
   - Testing steps
   -    Expected outcomes

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **LLM Integration**: Multimodal Large Language Model to process images and text
- **Flask-Mail**: For sending booking confirmations via email (optional feature)
- **Image Processing**: Used for extracting features from uploaded screenshots

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
