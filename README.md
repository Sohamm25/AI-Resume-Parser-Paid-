# Resume Parser

This Python script extracts text from a PDF resume and uses OpenAI's GPT-3.5 language model to parse and organize the relevant information.

## Features

- Extracts text from a PDF resume file
- Parses the resume text to extract the following information:
  - Name
  - College
  - Education domain
  - Certificates
  - Projects
  - Overall resume rating (out of 10)
- Provides a structured and easy-to-read output of the parsed information

## Requirements

- Python 3.6 or higher
- `fitz` library (PyMuPDF) for PDF extraction
- OpenAI API key for text parsing

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/resume-parser.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Obtain an OpenAI API key:
   - Create an account on [OpenAI](https://openai.com/) if you haven't already.
   - Generate an API key by following the instructions in the [OpenAI documentation](https://platform.openai.com/docs/api-reference/authentication).

## Usage

1. Update the `pdf_path` variable in the `main()` function with the path to your resume PDF file.

2. Run the script:

   ```
   python resume_parser.py
   ```

3. The script will extract the text from the PDF and use the OpenAI API to parse the resume information. The parsed output will be printed to the console.

## Customization

- You can change the OpenAI model used for parsing by modifying the `model` parameter in the `parse_resume_text()` function. The available models are listed in the [OpenAI documentation](https://platform.openai.com/docs/models).
- You can customize the information extracted from the resume by modifying the `prompt` variable in the `parse_resume_text()` function.

## Billing and Limitations

Using the OpenAI API requires a paid subscription. You will need to set up billing in your OpenAI account before running the script. Refer to the [OpenAI pricing page](https://openai.com/pricing/) for more information on the available plans and pricing.

Additionally, there are usage limits and rate limits for the OpenAI API. Ensure that you are aware of these limits and adjust your usage accordingly to avoid any unexpected charges.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
