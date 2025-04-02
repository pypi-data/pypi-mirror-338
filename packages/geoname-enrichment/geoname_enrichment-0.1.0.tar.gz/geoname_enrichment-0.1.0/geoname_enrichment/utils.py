
# -----------------------------------------------------------------------------
def needs_encoding_fixing(text):
    try:
        # Attempt a round-trip encode-decode cycle
        encoded = text.encode('latin1')
        decoded = encoded.decode('utf-8')
        # Return True if the decoded text looks different from the original
        return text != decoded
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Likely already correct UTF-8
        return False

# -----------------------------------------------------------------------------
def fix_encoding(text):
    try:
        # Decode from Latin-1 (or Windows-1252) and re-encode as UTF-8
        fixed_text = text.encode('latin1').decode('utf-8')
        return fixed_text
    except UnicodeDecodeError:
        # Return the original text if decoding fails
        return text




# -----------------------------------------------------------------------------
if __name__ == "__main__":
  import doctest
  doctest.testmod()
