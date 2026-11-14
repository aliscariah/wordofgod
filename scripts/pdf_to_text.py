from pypdf import PdfReader

reader = PdfReader("/Users/aleenascariah/personal/wordofgod/data/kjv.pdf")
print(len(reader.pages))
print(reader.pages[250].extract_text())
pages_text = [page.extract_text() for page in reader.pages]
combined_text = "\n".join(pages_text)
with open("/Users/aleenascariah/personal/wordofgod/data/kjv.txt", "w") as f:
    f.write(combined_text)
    
