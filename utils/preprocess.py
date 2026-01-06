import re

def clean_text(text):
    text = text.lower()
    # Faltu symbols hatana lekin skills wale symbols (+, #) bachana
    text = re.sub(r'[^\w\s+#.]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text