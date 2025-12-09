"""
Encoding/decoding logic for ASCII smuggling techniques.
"""

from charset import (
    zero_width_chars,
    invisible_chars,
    unicode_tag_char_range,
)


def encode_zero_width(text: str) -> str:
    """
    Encode text using zero-width characters.
    Each character is converted to its binary representation,
    then each bit is mapped to a zero-width character.
    
    0 = Zero Width Space (U+200B)
    1 = Zero Width Non-Joiner (U+200C)
    """
    zwsp = '\u200B'  # Zero Width Space (0)
    zwnj = '\u200C'  # Zero Width Non-Joiner (1)
    
    encoded = []
    for char in text:
        # Get 8-bit binary representation
        binary = format(ord(char), '08b')
        for bit in binary:
            encoded.append(zwsp if bit == '0' else zwnj)
    
    return ''.join(encoded)


def decode_zero_width(encoded: str) -> str:
    """
    Decode zero-width encoded text back to plaintext.
    """
    zwsp = '\u200B'
    zwnj = '\u200C'
    
    # Filter only zero-width chars
    bits = []
    for char in encoded:
        if char == zwsp:
            bits.append('0')
        elif char == zwnj:
            bits.append('1')
    
    # Convert bits to characters (8 bits per char)
    decoded = []
    for i in range(0, len(bits), 8):
        byte = ''.join(bits[i:i+8])
        if len(byte) == 8:
            decoded.append(chr(int(byte, 2)))
    
    return ''.join(decoded)


def encode_unicode_tags(text: str) -> str:
    """
    Encode ASCII text using Unicode tag characters (U+E0000 range).
    Each ASCII character is mapped to U+E0000 + ASCII code.
    
    This technique exploits the fact that tag characters are invisible
    but can carry ASCII data that LLMs may interpret.
    """
    tag_base = 0xE0000
    encoded = []
    
    for char in text:
        code = ord(char)
        if 0 <= code <= 127:  # ASCII range only
            encoded.append(chr(tag_base + code))
        else:
            # Non-ASCII chars pass through unchanged
            encoded.append(char)
    
    return ''.join(encoded)


def decode_unicode_tags(encoded: str) -> str:
    """
    Decode Unicode tag characters back to ASCII.
    """
    tag_start, tag_end = unicode_tag_char_range
    decoded = []
    
    for char in encoded:
        code = ord(char)
        if tag_start <= code <= tag_end:
            # Convert back to ASCII
            ascii_code = code - tag_start
            if 0 <= ascii_code <= 127:
                decoded.append(chr(ascii_code))
        else:
            decoded.append(char)
    
    return ''.join(decoded)


def encode_invisible_spaces(text: str) -> str:
    """
    Encode text by inserting invisible space characters between each character.
    Uses various Unicode space characters that appear invisible but carry data.
    
    This is a simpler technique - it just hides text within invisible chars.
    """
    # Use Hair Space (very thin, nearly invisible)
    hair_space = '\u200A'
    
    encoded = []
    for i, char in enumerate(text):
        # Encode char as sequence of invisible spaces based on ASCII value
        code = ord(char)
        # Use different invisible spaces to represent the character
        encoded.append(chr(0x2000 + (code % 16)))  # Low nibble
        encoded.append(chr(0x2000 + (code >> 4)))  # High nibble
    
    return ''.join(encoded)


def decode_invisible_spaces(encoded: str) -> str:
    """
    Decode invisible space encoded text.
    """
    decoded = []
    chars = list(encoded)
    
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            low = ord(chars[i]) - 0x2000
            high = ord(chars[i + 1]) - 0x2000
            if 0 <= low <= 15 and 0 <= high <= 15:
                decoded.append(chr((high << 4) | low))
    
    return ''.join(decoded)


def detect_hidden_content(text: str) -> dict:
    """
    Analyze text for hidden/smuggled content.
    Returns information about detected encoding types and decoded content.
    """
    results = {
        'has_zero_width': False,
        'has_unicode_tags': False,
        'has_invisible_spaces': False,
        'zero_width_decoded': '',
        'unicode_tags_decoded': '',
        'invisible_spaces_decoded': '',
        'suspicious_chars': [],
    }
    
    tag_start, tag_end = unicode_tag_char_range
    
    for char in text:
        code = ord(char)
        
        # Check for zero-width chars
        if char in zero_width_chars:
            results['has_zero_width'] = True
            
        # Check for Unicode tags
        if tag_start <= code <= tag_end:
            results['has_unicode_tags'] = True
            
        # Check for invisible spaces
        if char in invisible_chars:
            results['has_invisible_spaces'] = True
            
        # Track suspicious chars
        if char in zero_width_chars or char in invisible_chars or tag_start <= code <= tag_end:
            char_name = zero_width_chars.get(char) or invisible_chars.get(char) or f'Tag U+{code:04X}'
            results['suspicious_chars'].append({
                'char': repr(char),
                'code': f'U+{code:04X}',
                'name': char_name,
            })
    
    # Attempt decoding
    if results['has_zero_width']:
        try:
            results['zero_width_decoded'] = decode_zero_width(text)
        except:
            pass
            
    if results['has_unicode_tags']:
        try:
            results['unicode_tags_decoded'] = decode_unicode_tags(text)
        except:
            pass
            
    if results['has_invisible_spaces']:
        try:
            results['invisible_spaces_decoded'] = decode_invisible_spaces(text)
        except:
            pass
    
    return results

