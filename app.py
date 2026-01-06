from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader
from utils.preprocess import clean_text
from utils.recommender import get_recommendations
from utils.skill_extractor import extract_skills
from utils.scorer import resume_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        file = request.files.get("resume")
        if file and file.filename.endswith(".pdf"):
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            try:
                reader = PdfReader(path)
                text = "".join(page.extract_text() for page in reader.pages)
                
                # 1. Clean & Extract
                cleaned = clean_text(text)
                found_skills = extract_skills(cleaned)
                
                # 2. Get Job Recommendations
                jobs_df = get_recommendations(cleaned)

                # 3. Calculate Scores
                if jobs_df is not None:
                    for _, job in jobs_df.iterrows():
                        # Job skills ko saaf karke list banana
                        job_skills_list = job["skills"].lower().replace(',', ' ').split()
                        
                        score = resume_score(found_skills, job_skills_list)
                        
                        results.append({
                            "title": job["job_title"],
                            "score": int(score)
                        })

                # 4. Sort: Highest Match Top Par
                results = sorted(results, key=lambda x: x['score'], reverse=True)
                
            except Exception as e:
                print(f"Error: {e}")

    return render_template("index.html", results=results)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)