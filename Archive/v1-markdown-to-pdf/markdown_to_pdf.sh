#!/bin/bash

# Ensure UTF-8 encoding in the environment
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Check if a directory and stylesheet filename are provided
if [ -z "$2" ] || [ "$1" != "--language" ]; then
    echo "Usage: $0 --language <language>"
    exit 1
fi
language="$2"

# Define directories and files
current_directory=$(pwd)
directory="$current_directory/../1_1_vulns/translations/$language"
dir_name=$(basename "$directory")
generated_folder="$current_directory/generated"
tmp_folder="$generated_folder/tmp"
output_file="$tmp_folder/${dir_name}.md"
temp_pdf_file="$tmp_folder/${dir_name}.pdf"
pdf_file="$generated_folder/${dir_name}.pdf"
frontmatter="$current_directory/frontmatter.md"
stylesheet="$current_directory/styles/topten-$language.css"
intro_file="${directory}/LLM00_Introduction.md"

# Check if file exists
if [[ -f "$intro_file" ]]; then
    # Use awk to handle multi-line patterns and extract the title, ensuring UTF-8 handling
    header_title=$(awk '/<div class="doctitle">/,/<\/div>/{ if ($0 ~ /<\/div>/) { print p; p=""; next } if ($0 ~ /<div class="doctitle">/) next; p=p $0 }' "$intro_file" | xargs)
    echo "Extracted header title: $header_title"
else
    echo "Error: File does not exist."
fi

# Check if the provided argument is a directory
if [ ! -d "$directory" ]; then
    echo "Error: '$directory' is not a directory."
    exit 1
fi

# Check if the provided stylesheet exists
if [ ! -f "$stylesheet" ]; then
    echo "Error: '$stylesheet' does not exist."
    exit 1
fi

# Create the 'generated' directory if it doesn't exist
if [ ! -d "$generated_folder" ]; then
    mkdir "$generated_folder"
fi

# Create the 'tmp' directory if it doesn't exist
if [ ! -d "$tmp_folder" ]; then
    mkdir "$tmp_folder"
fi

# Delete the PDF and Markdown file if they already exist
if [ -f "$pdf_file" ]; then
    echo "Deleting existing PDF file: $pdf_file"
    rm "$pdf_file"
fi
# Delete the PDF and Markdown file if they already exist
if [ -f "$pdf_file" ]; then
    echo "Deleting existing temporary PDF file: $temp_pdf_file"
    rm "$pdf_file"
fi
if [ -f "$output_file" ]; then
    echo "Deleting existing temporary Markdown file: $output_file"
    rm "$output_file"
fi

# Start with a clean output file
> "$output_file"

# Add the frontmatter if it exists
if [ -f "$frontmatter" ]; then
    cat "$frontmatter" >> "$output_file"
    echo "" >> "$output_file" # Adds a newline after the frontmatter
fi

# Sort markdown files alphabetically and concatenate them
for file in $(find "$directory" -maxdepth 1 -name '*.md' | sort); do
    # Skip the frontmatter
    if [[ "$file" != "$frontmatter" ]]; then
        cat "$file" >> "$output_file"
        echo "" >> "$output_file" # Adds a newline between files
    fi
done

echo "Combined markdown files into $output_file"

# Convert the combined Markdown file to PDF
md-to-pdf --basedir "$current_directory" --stylesheet "$stylesheet" --document-title "$header_title" "$output_file"
mv "$temp_pdf_file" "$pdf_file"

if [ -f "$output_file" ] && [ "$3" != "--keep-markdown" ]; then
    echo "Deleting temporary Markdown file: $output_file"
    rm "$output_file"
fi

if [ -f "$pdf_file" ]; then
    echo -e "\033[32m###############################################################################################################\033[0m"
    echo -e "\033[32m###########################################    Success!!     ##################################################\033[0m"
    echo -e "\033[32m###############################################################################################################\033[0m"
    echo "PDF file generated: $pdf_file"
    echo -e "\033[32m###############################################################################################################\033[0m"
    echo -e "\033[32m###############################################################################################################\033[0m"
fi
