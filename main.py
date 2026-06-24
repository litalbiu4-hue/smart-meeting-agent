import pandas as pd
import os
from collections import Counter

print("Recruitment Interview Agent Started")

# =====================================
# READ CANDIDATES
# =====================================

df = pd.read_excel("candidates.xlsx")

print(f"\nFound {len(df)} candidates\n")

results = []
all_emails = []

# =====================================
# PROCESS CANDIDATES
# =====================================

for _, row in df.iterrows():

    candidate_id = row["Candidate_ID"]
    name = row["Full_Name"]
    email = row["Email"]
    phone = row["Phone"]
    position = row["Position"]
    region = row["Region"]
    experience = row["Experience_Years"]
    education = row["Education"]
    skills = row["Skills"]

    # =====================================
    # CALCULATE SCORE
    # =====================================

    score = 0

    # Experience

    if experience >= 8:
        score += 60
    elif experience >= 5:
        score += 50
    elif experience >= 3:
        score += 30
    else:
        score += 10

    # Education

    if str(education).upper() == "MA":
        score += 30

    elif str(education).upper() == "BA":
        score += 20

    # Skills

    skills_text = str(skills).lower()

    if "python" in skills_text:
        score += 10

    if "power bi" in skills_text:
        score += 10

    if "excel" in skills_text:
        score += 5

    # =====================================
    # LEVEL
    # =====================================

    if experience >= 6:
        level = "Senior"

    elif experience >= 3:
        level = "Mid"

    else:
        level = "Junior"

    # =====================================
    # INTERVIEW STATUS
    # =====================================

    if score >= 80:
        interview_status = "High Priority"

    elif score >= 60:
        interview_status = "Interview"

    else:
        interview_status = "Review"

    # =====================================
    # EMAIL
    # =====================================

    subject = f"Interview Invitation - {position}"

    body = f"""
Candidate: {name}

Position: {position}

Region: {region}

Level: {level}

Score: {score}

Status: {interview_status}
"""

    email_text = f"""
==================================================
Candidate ID: {candidate_id}
Name: {name}
Email: {email}

Subject:
{subject}

{body}
==================================================
"""

    all_emails.append(email_text)

    # =====================================
    # RESULTS
    # =====================================

    results.append({

        "Candidate_ID": candidate_id,
        "Full_Name": name,
        "Position": position,
        "Region": region,
        "Experience_Years": experience,
        "Education": education,
        "Level": level,
        "Score": score,
        "Interview_Status": interview_status

    })

# =====================================
# SAVE EMAILS
# =====================================

with open(
    "generated_emails.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("\n".join(all_emails))

print("generated_emails.txt created")

# =====================================
# RESULTS EXCEL
# =====================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="Score",
    ascending=False
)

results_df.to_excel(
    "candidate_results.xlsx",
    index=False
)

print("candidate_results.xlsx created")

# =====================================
# OPTIONAL GMAIL ANALYSIS
# =====================================

if os.path.exists("gmail_inbox_report.txt"):

    senders = []

    with open(
        "gmail_inbox_report.txt",
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    for line in content.splitlines():

        if line.startswith("FROM:"):

            sender = line.replace(
                "FROM:",
                ""
            ).strip()

            senders.append(sender)

    counter = Counter(senders)

    print("\nTOP SENDERS\n")

    for sender, count in counter.most_common(5):
        print(sender, ":", count)

# =====================================
# SUMMARY
# =====================================

print("\n========================")
print("PROJECT SUMMARY")
print("========================")

print(
    f"Candidates Processed: {len(results_df)}"
)

print(
    f"Highest Score: {results_df['Score'].max()}"
)

print(
    f"Average Score: {results_df['Score'].mean():.1f}"
)

print(
    f"High Priority Candidates: "
    f"{len(results_df[results_df['Interview_Status']=='High Priority'])}"
)

print("\nFiles Created:")

print("generated_emails.txt")
print("candidate_results.xlsx")

print("\nProcess completed successfully.")