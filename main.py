import re
import nltk
print(nltk.edit_distance("Превет", "Привет"))

'''text = 'От топота копыт пыль по полю летит'
text = text.lower()
match = re.search(r'по', text)
print(match, match.span(), match.string, match.group(), sep='\n')'''

def filter_text(text):
    text = text.lower()
    text = text.strip()
    pattern = r'[^\w\s]'
    text = re.sub(pattern,'', text)
    return text

print(filter_text("  Привет!!!:)  "))



