# Control characters (0x00-0x1F and 0x7F)
suspicious_control_chars = set(chr(i) for i in range(0, 32)) | {chr(127)}

# Exclude: \t (0x09), \n (0x0A), \r (0x0D) as these are normal text formatting
common_chars = {'\t', '\n', '\r'}  # Tab, newline, carriage return

zero_width_chars = {
    '\u200B': 'Zero Width Space',
    '\u200C': 'Zero Width Non-Joiner',
    '\u200D': 'Zero Width Joiner',
    '\uFEFF': 'Zero Width No-Break Space',
    '\u2060': 'Word Joiner',
}

invisible_chars = {
    '\u00AD': 'Soft Hyphen',
    '\u061C': 'Arabic Letter Mark',
    '\u180E': 'Mongolian Vowel Separator',
    '\u2000': 'En Quad',
    '\u2001': 'Em Quad',
    '\u2002': 'En Space',
    '\u2003': 'Em Space',
    '\u2004': 'Three-Per-Em Space',
    '\u2005': 'Four-Per-Em Space',
    '\u2006': 'Six-Per-Em Space',
    '\u2007': 'Figure Space',
    '\u2008': 'Punctuation Space',
    '\u2009': 'Thin Space',
    '\u200A': 'Hair Space',
    '\u202F': 'Narrow No-Break Space',
    '\u205F': 'Medium Mathematical Space',
    '\u3000': 'Ideographic Space',
}

# Unicode tag character range (U+E0000 to U+E007F)
unicode_tag_char_range = (0xE0000, 0xE007F)