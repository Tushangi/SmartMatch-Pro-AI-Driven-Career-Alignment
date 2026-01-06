import re

def extract_skills(resume_text):
    try:
        with open("data/skills.txt", "r") as f:
            skills = [skill.strip().lower() for skill in f.readlines() if skill.strip()]
    except FileNotFoundError:
        return []

    resume_text = resume_text.lower()
    extracted = []

    for skill in skills:
        # Regex use karein taaki exact word match ho aur symbols (+, #) handle hon
        # \s* use karne se 'power bi' aur 'powerbi' dono match honge
        skill_reg = skill.replace(" ", r"\s*")
        pattern = r'\b' + re.escape(skill_reg).replace(r'\ ', r'\s*') + r'\b'
        
        if re.search(pattern, resume_text):
            extracted.append(skill)
            
    return list(set(extracted))