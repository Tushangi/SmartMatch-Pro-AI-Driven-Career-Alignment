import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.skill_extractor import extract_skills

def get_recommendations(resume_text):
    # 1. Jobs data load karna
    try:
        jobs = pd.read_csv("data/jobs.csv")
        # Ensure 'skills' column string format mein ho
        jobs['skills'] = jobs['skills'].fillna('').astype(str)
    except Exception as e:
        print(f"Error loading jobs.csv: {e}")
        return pd.DataFrame()

    # 2. Resume se sirf skills nikalna (Filtering)
    # Bina skills extract kiye recommendation accurate nahi hoti
    found_skills = extract_skills(resume_text)
    skills_query = " ".join(found_skills)

    if not skills_query:
        # Agar koi skill nahi mili toh top jobs default dikhayein
        return jobs.head(10)

    # 3. TF-IDF Vectorizer (CountVectorizer se zyada accurate)
    # Ye important words ko zyada weightage deta hai
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Corpus banayein (Jobs ki skills + Resume ki extracted skills)
    job_skills_list = jobs["skills"].tolist()
    all_content = job_skills_list + [skills_query]
    
    # Matrix generate karna
    tfidf_matrix = tfidf.fit_transform(all_content)

    # 4. Cosine Similarity calculate karna
    # Last vector (resume) ko baaki saare vectors (jobs) se compare karein
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # 5. Scores ko jobs dataframe mein add karna
    jobs["score"] = similarity_scores[0] * 100  # Percentage mein convert kiya

    # 6. Top 10 matches return karna (head(3) se badha kar 10 kiya)
    top_jobs = jobs.sort_values(by="score", ascending=False).head(10)

    return top_jobs