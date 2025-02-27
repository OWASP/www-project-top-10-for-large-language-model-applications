# Data Processing Scripts for OWASP Top 10 LLM Analysis

This repository contains a series of Python scripts designed for processing and categorizing data relevant to the study of OWASP Top 10 vulnerabilities in Large Language Models (LLMs). The scripts facilitate tasks such as combining CSV files, categorizing data based on various criteria, and applying these categorizations to a dataset.

## Script 1: Combining CSV Files

This script combines multiple CSV files into a single DataFrame. Ensure the correct paths are specified for your CSV files.

```python
import pandas as pd

# List of your CSV files with the correct path
csv_files = [
    'C:\\PATH1.csv',
    'C:\\PATH2.csv',
    'C:\\PATH3.csv',
    'C:\\PATH4.csv'
]

try:
    # Combine all CSV files into one DataFrame
    combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
    print("CSV files successfully combined.")
except Exception as e:
    print("An error occurred:", e)
```

## Script 2: Categorization Functions

These functions categorize text data based on predefined criteria such as research methods, focus areas, topics/themes, geographical and temporal focus.

```python
def categorize_research_methods(text):
    categories = []
    if 'case study' in text.lower():
        categories.append('Case Studies')
    if 'interview' in text.lower():
        categories.append('Interviews')
    if 'ethnography' in text.lower():
        categories.append('Ethnography')
    if 'content analysis' in text.lower():
        categories.append('Content Analysis')
    if 'survey' in text.lower() or 'questionnaire' in text.lower():
        categories.append('Surveys and Questionnaires')
    if 'experiment' in text.lower():
        categories.append('Experiments')
    if 'statistical analysis' in text.lower():
        categories.append('Statistical Analysis')
    if any(method in categories for method in ['Case Studies', 'Interviews', 'Ethnography', 'Content Analysis']) and any(method in categories for method in ['Surveys and Questionnaires', 'Experiments', 'Statistical Analysis']):
        categories.append('Mixed Methods')
    return ', '.join(categories)

def categorize_focus_areas(text):
    categories = []
    if 'risk assessment' in text.lower():
        categories.append('Risk Assessment')
    if 'expert opinion' in text.lower():
        categories.append('Expert Opinions')
    if 'technology assessment' in text.lower():
        categories.append('Technological Assessments')
    if 'policy' in text.lower() or 'regulation' in text.lower():
        categories.append('Policy and Regulation')
    return ', '.join(categories)

def categorize_topics_themes(text):
    categories = []
    if 'llm security' in text.lower():
        categories.append('LLM Security')
    if 'industry application' in text.lower():
        categories.append('Industry Applications')
    if 'emerging threat' in text.lower():
        categories.append('Emerging Threats')
    if 'solution' in text.lower() or 'mitigation' in text.lower():
        categories.append('Solutions and Mitigations')
    return ', '.join(categories)

def categorize_geographical_focus(text):
    categories = []
    if 'global' in text.lower():
        categories.append('Global')
    if 'regional' in text.lower() or any(region in text.lower() for region in ['asia', 'europe', 'america', 'africa']):
        categories.append('Regional')
    return ', '.join(categories)

def categorize_temporal_focus(text):
    categories = []
    if 'historical' in text.lower():
        categories.append('Historical Analyses')
    if 'current' in text.lower() or 'present' in text.lower():
        categories.append('Current Issues')
    if 'future' in text.lower() or 'prediction' in text.lower():
        categories.append('Future Predictions')
    return ', '.join(categories)
```

## Script 3: Applying Categorizations

This script applies the above categorization functions to the DataFrame created by combining CSV files.

```python
combined_df['Focus Areas'] = combined_df[' Description '].apply(categorize_focus_areas)
combined_df['Topics or Themes'] = combined_df[' Description '].apply(categorize_topics_themes)
combined_df['Geographical Focus'] = combined_df[' Description '].apply(categorize_geographical_focus)
combined_df['Temporal Focus'] = combined_df[' Description '].apply(categorize_temporal_focus)
```

---

## Contribution

We welcome contributions and suggestions to improve these scripts. Please feel free to fork the repository, make your changes, and submit a pull request. For any queries or suggestions, kindly open an issue in the repository.
