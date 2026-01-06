def resume_score(extracted_skills, job_skills):
    # Dono ko set mein convert karein taaki comparison fast ho
    resume_set = set([s.lower().strip() for s in extracted_skills])
    job_set = set([s.lower().strip() for s in job_skills])

    if not job_set:
        return 0

    # Kitne skills common hain
    matches = resume_set.intersection(job_set)
    
    score = (len(matches) / len(job_set)) * 100
    return round(score)