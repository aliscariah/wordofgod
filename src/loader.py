def load_bible(file_path="/Users/aleenascariah/personal/wordofgod/data/kjv.txt"):
    with open(file_path,"r") as f:
        text = f.read()
        return text 
    if file_path is None:
        raise ValueError("File path must be provided")
    
