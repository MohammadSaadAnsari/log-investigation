# log-investigation (forensic log investigation)

## Dataset

Download from:
https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs (jo taran ne bheja hai, usko hi extract krlo)

Then:
open git bash:

write-                      
git clone https://github.com/MohammadSaadAnsari/log-investigation (ek local copy mil gayi tmko github repo ki)                            
cd log-investigation

make a folder-              
mkdir data 

!!!!!!CLOSE TERMINAL NOW!!!!!! (usmain paste mt krdena csv file plss)

(now after this, dataset(unzip krne ke baad jo csv file hai) paste krdo iss folder main)


now you can start working on training.py or analysis.py or app.py etc, in your branch. (try not to work directly on main, unless you are sure what you are editing is 100% correct)


Shreya:
Step: Track changes with Git

After making edits / adding files, do this in Git Bash:

git status


Shows what changed

git add .


Stages all changes

git commit -m "Added data folder and initial analysis file"


Saves changes locally

Step: Push changes to GitHub (optional)

You need write access to repo

Then:

git push


This updates the GitHub repo with your changes


SAAD: 18-12-25
To simply run the project and view the website.

# 1. Clone the repo (ignore if already done previously)
git clone https://<link-to-repo>
cd repo-name

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
