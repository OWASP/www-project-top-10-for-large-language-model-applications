#!/bin/bash

# Check if a directory and stylesheet filename are provided
if [ -z "$2" ] || [ "$1" != "--language" ]; then
    echo "Usage: $0 --language <language>"
    exit 1
fi
language="$2"

# Define directories and files
current_directory=$(pwd)
directory="$current_directory/../1_1_vulns/$language"
dir_name=$(basename "$directory")
generated_folder="$current_directory/generated"
tmp_folder="$generated_folder/tmp"
output_file="$tmp_folder/${dir_name}.md"
temp_pdf_file="$tmp_folder/${dir_name}.pdf"
pdf_file="$generated_folder/${dir_name}.pdf"
frontmatter="$current_directory/frontmatter.md"
stylesheet="$current_directory/styles/topten-$language.css"

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
md-to-pdf --basedir "$current_directory" --stylesheet "$stylesheet" "$output_file" 
mv "$temp_pdf_file" "$pdf_file"

if [ -f "$output_file" ] && [ "$3" != "--keep-markdown" ]; then
    echo "Deleting temporary Markdown file: $output_file"
    rm "$output_file"
fi

if [ -f "$pdf_file" ]; then
    echo -e "\n\n\033[32m###############################################################################################################\033[0m"
    echo -e "\033[32m###########################################    Success!!     ##################################################\033[0m"
    echo -e "\033[32m###############################################################################################################\033[0m\n"
    echo "PDF file generated: $pdf_file"
    echo -e "\n\033[32m###############################################################################################################\033[0m"
fi
