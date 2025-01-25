import fitz
import openai
openai.api_key = "api"  ###BILLING REQUIRED HERE BUY OPEN AI API
def extract_text_from_pdf(pdf_path): 
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_document:
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]  
                text += page.get_text("text")
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
def parse_resume_text(text):
    prompt = (
        "Extract and organize the following information from the provided resume text:\n\n"
        "1. Name\n"
        "2. College\n"
        "3. Education domain\n"
        "4. Certificates\n"
        "5. Projects\n"
        "6. Rate the resume out of 10.\n\n"
        "Resume text:\n\n" + text
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI specializing in extracting structured information from resumes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None
def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    if not text:
        print("Failed to extract text from the PDF.")
        return
    parsed_output = parse_resume_text(text)
    if parsed_output:
        print("Parsed Resume Information:\n")
        print(parsed_output)
    else:
        print("Failed to parse resume information.")
if __name__ == "__main__":
    pdf_path = "path_to_your_resume.pdf" ###### Update this with the path to your resume PDF
    main(pdf_path)
