import os
import re
import shutil
import sys
from pathlib import Path


def print_error(message):
    print(f"ERROR: {message}", file=sys.stderr)

def clear_generated_folder(generated_path):
    try:
        generated_path.mkdir(exist_ok=True)
    except Exception as e:
        print_error(f"Could not create or access '{generated_path}': {e}")
        sys.exit(1)

    for item in generated_path.iterdir():
        if item.name != '.gitkeep' and item.is_file():
            try:
                item.unlink()
            except Exception as e:
                print_error(f"Failed to delete '{item}': {e}")
                sys.exit(1)

def get_llm_files(locale_path):
    llm_files = list(locale_path.glob('LLM[0-9][0-9]_*.md'))
    if not llm_files:
        print_error(f"No LLMXX_*.md files found in '{locale_path}'.")
        sys.exit(1)

    try:
        return sorted(llm_files, key=lambda f: int(re.search(r'LLM(\d+)_', f.name).group(1)))
    except Exception as e:
        print_error(f"Error sorting LLM files: {e}")
        sys.exit(1)

def combine_llm_files(llm_files, output_file):
    try:
        with output_file.open('w', encoding='utf-8') as body_file:
            for file in llm_files:
                try:
                    with file.open('r', encoding='utf-8') as f:
                        body_file.write(f.read())
                        body_file.write('\n\n')
                except Exception as e:
                    print_error(f"Failed to read '{file}': {e}")
                    sys.exit(1)
    except Exception as e:
        print_error(f"Failed to write to '{output_file}': {e}")
        sys.exit(1)

def safe_copy(src, dst):
    if not src.exists():
        print_error(f"Required file '{src.name}' not found in locale directory.")
        sys.exit(1)
    try:
        shutil.copy(src, dst)
    except Exception as e:
        print_error(f"Failed to copy '{src}' to '{dst}': {e}")
        sys.exit(1)

def prepend_frontmatter(frontmatter_file, target_file):
    if not frontmatter_file.exists():
        print_error(f"Frontmatter file '{frontmatter_file}' does not exist.")
        sys.exit(1)
    if not target_file.exists():
        print_error(f"Target file '{target_file}' does not exist for frontmatter prepend.")
        sys.exit(1)

    try:
        with frontmatter_file.open('r', encoding='utf-8') as f:
            front = f.read().rstrip()

        with target_file.open('r', encoding='utf-8') as f:
            main = f.read().lstrip()

        with target_file.open('w', encoding='utf-8') as f:
            f.write(front + "\n\n" + main)
    except Exception as e:
        print_error(f"Failed to prepend frontmatter from '{frontmatter_file}' to '{target_file}': {e}")
        sys.exit(1)

def process_locale_directory(locale_dir):
    locale_path = Path(locale_dir)
    if not locale_path.is_dir():
        print_error(f"Locale directory '{locale_path}' does not exist or is not a directory.")
        sys.exit(1)

    generated_path = Path('./generated')
    frontmatter_path = Path('./frontmatter')

    # Step 1: Clear ./generated except .gitkeep
    clear_generated_folder(generated_path)

    # Step 2: Get and sort LLMXX_*.md files
    llm_files = get_llm_files(locale_path)

    # Step 3: Combine into body.md
    body_md = generated_path / 'body.md'
    combine_llm_files(llm_files, body_md)

    # Step 4-6: Copy required files
    cover_md = generated_path / 'cover.md'
    toc_md = generated_path / 'toc.md'

    safe_copy(locale_path / 'ADD00_Cover.md', cover_md)
    safe_copy(locale_path / 'ADD01_Table_of_Contents.md', toc_md)
    safe_copy(locale_path / 'styles.css', generated_path / 'styles.css')

    # Step 7: Prepend frontmatter
    prepend_frontmatter(frontmatter_path / 'a4-body-frontmatter.md', body_md)
    prepend_frontmatter(frontmatter_path / 'a4-cover-frontmatter.md', cover_md)
    prepend_frontmatter(frontmatter_path / 'a4-toc-frontmatter.md', toc_md)

    print("Generation completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_book.py <locale_directory>")
        sys.exit(1)

    process_locale_directory(sys.argv[1])

