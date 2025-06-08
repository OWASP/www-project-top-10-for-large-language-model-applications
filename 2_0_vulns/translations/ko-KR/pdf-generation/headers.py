import unicodedata
from collections import defaultdict

import pdfplumber
from bidi import get_display


def is_rtl_text(text):
    for ch in text:
        bidi = unicodedata.bidirectional(ch)
        if bidi in ('R', 'AL'):
            print(f"First strong character: {repr(ch)} → RTL")
            return True
        elif bidi == 'L':
            print(f"First strong character: {repr(ch)} → LTR")
            return False
    print("No strong character found, defaulting to LTR.")
    return False

# Added a function to solve the problem of Korean characters not being spaced
def join_line_with_spaces(line_chars, space_threshold=2.0):
    # Detect character spacing, insert spaces, and merge into one line
    text = ""
    prev_char = None
    for c in line_chars:
        if prev_char is not None:
            # Measure space between characters (current character x0 - previous character x1)
            gap = c['x0'] - prev_char['x1']
            if gap > space_threshold:  # Insert blank space if threshold is exceeded
                text += " "
        text += c['text']
        prev_char = c
    return text

def extract_lines_with_sizes(pdf_path):
    lines_with_sizes = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            # Extract characters with their properties
            chars = page.chars
            
            # Group characters into lines using document-top position
            lines = defaultdict(list)
            for char in chars:
                lines[round(char['doctop'])].append(char)
            
            # Analyze each line
            for ypos, line_chars in lines.items():
                if not line_chars:
                    continue
                
                # Sort characters left-to-right
                line_chars.sort(key=lambda x: x['x0'])
                
                # Extract text and average size for the line
                #text = ''.join(c['text'] for c in line_chars)
                text = join_line_with_spaces(line_chars, space_threshold=2.0)   # Calling a function to solve the Korean character spacing problem
                sizes = [c['size'] for c in line_chars if c['size']]
                avg_size = sum(sizes) / len(sizes) if sizes else 0
                
                lines_with_sizes.append({
                    'text': text.strip(),
                    'page': page_number,
                    'size': avg_size
                })
    
    return lines_with_sizes


# Usage example:
lines = extract_lines_with_sizes("body.pdf")
# Detect direction from the first line only
first_line_text = lines[1]['text']
document_is_rtl = is_rtl_text(first_line_text)
print("Detected direction:", "RTL" if document_is_rtl else "LTR")

combined_lines = []
i = 0
while i < len(lines):
    current = lines[i]
    combined_text = current['text']
    page = current['page']
    size = current['size']
    i += 1
    while i < len(lines) and abs(lines[i]['size'] - size) < 1e-3:
        next_text = lines[i]['text']
        if document_is_rtl:
            combined_text = next_text + ' ' + combined_text  # RTL
        else:
            combined_text += ' ' + next_text  # LTR
        i += 1
    combined_lines.append({'text': combined_text.strip(), 'page': page, 'size': size})

lines = combined_lines

toc = []
toc.append("| | |")
toc.append("|-----------|-------|")
for line in lines:
    # Normalize text for proper display in right-to-left languages (e.g., handle Arabic/Persian)
    line['text'] = get_display(line['text'])
    if line['size'] > 25:   # Change in value according to change in title font size
        # Main section
        toc.append(f"| **{line['text']}** | **{line['page']}** |")
    elif line['size'] > 20:
        # Sub section (indent with non-breaking space for clarity)
        toc.append(f"| {line['text']} | {line['page']} |")
    else:
        continue

print('\n'.join(toc))

# Now write the TOC
with open("toc.md", "a", encoding="utf-8") as f:
    f.write('\n')
    f.write('\n'.join(toc))