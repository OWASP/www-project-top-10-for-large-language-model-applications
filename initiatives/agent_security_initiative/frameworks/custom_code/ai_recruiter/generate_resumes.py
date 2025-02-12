import os
import shutil
from faker import Faker
import random
import subprocess
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

def generate_work_experience():
    experiences = []
    current_date = datetime.now()
    
    for _ in range(random.randint(2, 5)):
        duration = random.randint(12, 48)  # months
        end_date = current_date
        start_date = end_date - timedelta(days=duration * 30)
        
        experience = {
            'company': fake.company(),
            'position': fake.job(),
            'start_date': start_date.strftime('%B %Y'),
            'end_date': end_date.strftime('%B %Y'),
            'description': [
                fake.bs(),
                f"Led team of {random.randint(3, 15)} people",
                f"Improved {fake.bs()} by {random.randint(20, 80)}%"
            ]
        }
        experiences.append(experience)
        current_date = start_date - timedelta(days=30)  # 1 month gap between jobs
    
    return experiences

def generate_education():
    degrees = ['Bachelor of Science', 'Master of Science', 'Bachelor of Arts', 'Master of Arts']
    fields = ['Computer Science', 'Information Technology', 'Software Engineering', 'Data Science']
    
    return {
        'degree': random.choice(degrees),
        'field': random.choice(fields),
        'university': f"{fake.city()} University",
        'graduation_year': random.randint(2010, 2023)
    }

def generate_skills():
    technical_skills = [
        'Python', 'Java', 'JavaScript', 'React', 'Node.js', 'Docker',
        'Kubernetes', 'AWS', 'Azure', 'GCP', 'SQL', 'MongoDB',
        'Machine Learning', 'CI/CD', 'Git', 'Agile', 'Scrum'
    ]
    
    return random.sample(technical_skills, random.randint(6, 10))

def generate_resume():
    person = {
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'location': f"{fake.city()}, {fake.state()}",
        'summary': fake.text(max_nb_chars=300),
        'work_experience': generate_work_experience(),
        'education': generate_education(),
        'skills': generate_skills()
    }
    
    markdown = f"""# {person['name']}

{person['email']} | {person['phone']} | {person['location']}

## Professional Summary

{person['summary']}

## Work Experience

"""
    
    for exp in person['work_experience']:
        markdown += f"### {exp['position']} at {exp['company']}\n"
        markdown += f"_{exp['start_date']} - {exp['end_date']}_\n\n"
        for desc in exp['description']:
            markdown += f"- {desc}\n"
        markdown += "\n"
    
    markdown += f"""## Education

### {person['education']['degree']} in {person['education']['field']}
_{person['education']['university']}, {person['education']['graduation_year']}_

## Technical Skills

{', '.join(person['skills'])}
"""
    
    return markdown, person['name']

def main():
    # Create resume collection directory if it doesn't exist
    os.makedirs('resume_collection', exist_ok=True)
    
    # Create temporary directory
    temp_dir = '/tmp/markdown_temp'
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Generate multiple resumes
        for i in range(5):
            resume_content, name = generate_resume()
            
            # Save as markdown
            md_filename = os.path.join(temp_dir, f"resume_{i}.md")
            with open(md_filename, 'w') as f:
                f.write(resume_content)
            
            # Convert to PDF using pandoc
            pdf_filename = f"resume_collection/{name.replace(' ', '_')}.pdf"
            subprocess.run(['pandoc', md_filename, '-o', pdf_filename])
    finally:
        # Clean up markdown files
        shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
