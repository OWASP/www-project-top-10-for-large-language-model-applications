# OWASP Top 10 for LLM - Literature Review

This repository is dedicated to the literature review of the OWASP (Open Web Application Security Project) Top 10 vulnerabilities as they pertain to Language Learning Models (LLMs). Our goal is to collect, categorize, and analyze academic papers, articles, and any form of literature that addresses these vulnerabilities in the context of LLMs.

## Project Description

The OWASP Top 10 is an awareness document that represents a broad consensus about the most critical security risks to web applications. Our focus extends this to the burgeoning field of LLMs, where security and reliability are of paramount importance. The literature review is a structured collection of all the relevant data to help researchers, developers, and security experts understand and address these risks.

The repository is structured as follows:
- `categorized_papers.csv`: A CSV file containing categorized literature details.
- `scripts/`: This directory contains all the Python scripts used for categorization.

## Categorization Scripts

The literature is categorized by several aspects, such as research methods, focus areas, topics/themes, geographical focus, and temporal focus. The following Python code is used to categorize the literature based on its content.

### Research Methods

```python
# The code block for categorize_research_methods
def categorize_research_methods(text):
    categories = []
    text = str(text).lower() if text is not None else ''
    if 'case study' in text:
        categories.append('Case Studies')
    if 'interview' in text:
        categories.append('Interviews')
    if 'ethnography' in text:
        categories.append('Ethnography')
    if 'content analysis' in text:
        categories.append('Content Analysis')
    if 'survey' in text or 'questionnaire' in text:
        categories.append('Surveys and Questionnaires')
    if 'experiment' in text:
        categories.append('Experiments')
    if 'statistical analysis' in text:
        categories.append('Statistical Analysis')
    if any(method in categories for method in ['Case Studies', 'Interviews', 'Ethnography', 'Content Analysis']) and any(method in categories for method in ['Surveys and Questionnaires', 'Experiments', 'Statistical Analysis']):
        categories.append('Mixed Methods')
    return ', '.join(categories)

def categorize_focus_areas(text):
    categories = []
    text = str(text).lower() if text is not None else ''
    if 'risk assessment' in text:
        categories.append('Risk Assessment')
    if 'expert opinion' in text:
        categories.append('Expert Opinions')
    if 'technology assessment' in text:
        categories.append('Technological Assessments')
    if 'policy' in text or 'regulation' in text:
        categories.append('Policy and Regulation')
    return ', '.join(categories)

def categorize_topics_themes(text):
    categories = []
    text = str(text).lower() if text is not None else ''
    if 'llm security' in text:
        categories.append('LLM Security')
    if 'industry application' in text:
        categories.append('Industry Applications')
    if 'emerging threat' in text:
        categories.append('Emerging Threats')
    if 'solution' in text or 'mitigation' in text:
        categories.append('Solutions and Mitigations')
    return ', '.join(categories)

def categorize_geographical_focus(text):
    categories = []
    text = str(text).lower() if text is not None else ''
    if 'global' in text:
        categories.append('Global')
    if 'regional' in text or any(region in text for region in ['asia', 'europe', 'america', 'africa']):
        categories.append('Regional')
    return ', '.join(categories)

def categorize_temporal_focus(text):
    categories = []
    text = str(text).lower() if text is not None else ''
    if 'historical' in text:
        categories.append('Historical Analyses')
    if 'current' in text or 'present' in text:
        categories.append('Current Issues')
    if 'future' in text or 'prediction' in text:
        categories.append('Future Predictions')
    return ', '.join(categories)

