from PyPDF2 import PdfReader
import re

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to extract Name, Email, Phone, Skills
def extract_info_from_text(text):
    name = text.strip().split('\n')[0]  # Assumes name is the first line
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.search(r'(\+?\d[\d\s\-]{8,}\d)', text)
    skills = re.findall(r'\b(Python|Java|C\+\+|SQL|HTML|CSS|JavaScript)\b', text, re.IGNORECASE)

    return {
        'name': name,
        'email': email.group() if email else None,
        'phone': phone.group() if phone else None,
        'skills': list(set([skill.capitalize() for skill in skills]))
    }

# Main function to test with a sample PDF
if __name__ == "__main__":
    file_path = "sample_resume.pdf"  # Make sure this file is in the same folder
    text = extract_text_from_pdf(file_path)
    info = extract_info_from_text(text)

    print("Extracted Information:")
    print("Name:", info['name'])
    print("Email:", info['email'])
    print("Phone:", info['phone'])
    print("Skills:", ", ".join(info['skills']))
