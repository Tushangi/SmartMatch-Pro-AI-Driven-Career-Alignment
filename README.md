<h1><b>🚀 SmartMatch-Pro: AI-Driven Career Alignment Engine</h1></b>
<b>SmartMatch-Pro is an advanced recruitment solution designed to bridge the gap between candidate resumes and 100+ industry job roles. By leveraging Natural Language Processing (NLP) and Vectorization, the system extracts skills from resumes and identifies the most relevant career paths with high precision.</b>

----
<img width="1363" height="595" alt="image" src="https://github.com/user-attachments/assets/9652f11b-b662-480e-95f7-14d7253ec6f4" />

----

<h1><b>🌟 Key Impact Features</h1></b>
  
<b>* Deep Skill Extraction:</b> Utilizes Regex-based NLP to mine technical and soft skills from raw text (Capable of identifying 100+ professional skills).

<b>* Semantic Job Matching:</b> Employs TF-IDF Vectorization and Cosine Similarity to provide "Smart Scoring" rather than simple keyword counting.

<b>* Fuzzy Search Logic:</b> Intelligently handles variations like "Power BI" (resume) vs "powerbi" (database) to ensure 95%+ matching accuracy.

<b>* Scalable Architecture:</b> Optimized to process 100+ job entries from jobs.csv in milliseconds.

<b>* Live Document Preview:</b> A modern user interface that provides an instant PDF preview alongside real-time analysis results.

----

<h1><b>🛠️ Tech Stack</h1></b>
  
<b>* Backend:</b> Python (Flask)

<b>* AI/ML:</b> Scikit-learn (TF-IDF, Cosine Similarity), Pandas, NumPy

<b>* Parsing:</b> PyPDF2, Regular Expressions (Regex)

<b>* Frontend:</b> HTML5, CSS3 (Modern Dark Theme UI), JavaScript

----

<h1><b>📂 Project Structure</h1></b>
  
Plaintext

├── app.py              # Main Flask Application
├── data/
│   ├── jobs.csv        # Database of 100+ Job Roles & Required Skills
│   └── skills.txt      # Master List of 100+ Technical Keywords
├── utils/
│   ├── preprocess.py   # Text Cleaning & Normalization Logic
│   ├── skill_extractor.py # Regex-based Intelligent Skill Mining
│   ├── recommender.py  # TF-IDF & Vector Space Modeling
│   └── scorer.py       # Final Percentage Match Calculation
└── templates/          # UI Dashboard Files

----

<h1><b>⚙️ Installation & Setup</h1></b>
  
<b>* Clone the repository:</b>

Bash

git clone https://github.com/yourusername/SmartMatch-Pro.git

<b>* Install dependencies:</b>

Bash

pip install flask pandas scikit-learn pypdf2

<b>* Run the application:</b>

Bash

python app.py

<b>* Access the dashboard:</b>

Open http://127.0.0.1:5000 in your web browser.

----

<h1><b>📈 How It Works</h1></b>
  
<b>* Text Normalization:</b> Extracted PDF text is cleaned, stripped of noise, and converted to lowercase.

<b>* Keyword Mining:</b> The resume text is scanned against skills.txt to isolate exact professional competencies.

<b>* Vector Space Modeling:</b> Extracted skills are transformed into numerical vectors using TF-IDF.

<b>* Similarity Ranking:</b> The Cosine Similarity algorithm calculates a match score for every job role in the database and ranks the top 10 results.
