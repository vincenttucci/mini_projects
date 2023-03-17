import openai
import tkinter as tk
from tkinter import ttk,scrolledtext

'''
VERSION 2.1

This program is desinged to take in a series of inputs 
about a job and returns an optimal cover letter for the job position.

The project is still being refined and is not intended to be used solely 
to generate a cover letter to be used in the workplace.
'''

openai.api_key = "YOUR_API_KEY_HERE"

'''
Input your existing data in here below. You can change
the data as youu see fit and add more categories.
This data is needed in order for the generated
response to be more tailored towards your experience.
'''
user_data = {
    "work_experience": "WORK EXPERIENCE HERE",
    "education": "EDUCATION EXPERIENCE HERE",
    "technical_skills": "TECHNICAL SKILLS HERE",
}

def generate_cover_letter():
    '''
    Gets input values from the GUI
    Formats the input to send to the AI
    Gets AI response
    Returns them in the output box
    '''
    job_title = job_title_entry.get()
    job_location = job_location_entry.get()
    company_name = company_name_entry.get()
    job_description = job_description_text.get("1.0", "end-1c")
    qualifications = qualifications_text.get("1.0", "end-1c")

    prompt = f"Create a cover letter for a job application based on the following details:\n"
    prompt += f"Job title: {job_title}\n"
    prompt += f"Job location: {job_location}\n"
    prompt += f"Company name: {company_name}\n"
    prompt += f"Job description: {job_description}\n"
    prompt += f"Qualifications: {qualifications}\n\n"
    prompt += f"Applicant's work experience: {user_data['work_experience']}\n"
    prompt += f"Applicant's education: {user_data['education']}\n"
    prompt += f"Applicant's technical skills: {user_data['technical_skills']}\n\n"
    prompt += f"Cover Letter:\n"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    cover_letter = response.choices[0].text.strip()
    cover_letter_text.delete("1.0", tk.END)
    cover_letter_text.insert(tk.END, cover_letter)

#SETTING UP THE GUI STUFF
root = tk.Tk()
root.title("Cover Letter Generator")
root.resizable(False, False)
font = ("Calibri", 10)

job_title_label = ttk.Label(root, text="Job Title:")
job_title_label.grid(column=0, row=0, padx=(20, 10), pady=(20, 10), sticky="w")
job_title_entry = ttk.Entry(root, width=60)
job_title_entry.grid(column=1, row=0, padx=(0, 20), pady=(20, 10), columnspan=2)

job_location_label = ttk.Label(root, text="Job Location:")
job_location_label.grid(column=0, row=1, padx=(20, 10), pady=10, sticky="w")
job_location_entry = ttk.Entry(root, width=60)
job_location_entry.grid(column=1, row=1, padx=(0, 20), pady=10, columnspan=2)

company_name_label = ttk.Label(root, text="Company Name:")
company_name_label.grid(column=0, row=2, padx=(20, 10), pady=10, sticky="w")
company_name_entry = ttk.Entry(root, width=60)
company_name_entry.grid(column=1, row=2, padx=(0, 20), pady=10, columnspan=2)

job_description_label = ttk.Label(root, text="Job Description:")
job_description_label.grid(column=0, row=3, padx=(20, 10), pady=10, sticky="nw")
job_description_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=5, font=font)
job_description_text.grid(column=1, row=3, padx=(0, 20), pady=10, columnspan=2)

qualifications_label = ttk.Label(root, text="Qualifications:")
qualifications_label.grid(column=0, row=4, padx=(20, 10), pady=10, sticky="nw")
qualifications_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=5, font=font)
qualifications_text.grid(column=1, row=4, padx=(0, 20), pady=10, columnspan=2)

generate_button = ttk.Button(root, text="Generate Cover Letter", command=generate_cover_letter)
generate_button.grid(column=0, row=5, padx=(20, 10), pady=(10, 20), columnspan=2)

cover_letter_label = ttk.Label(root, text="Generated Cover Letter:")
cover_letter_label.grid(column=0, row=6, padx=(20, 10), pady=10, sticky="nw")
cover_letter_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
cover_letter_text.grid(column=1, row=6, padx=(0, 20), pady=10, columnspan=2)

root.mainloop()
