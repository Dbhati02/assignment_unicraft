# 🔍 Smart Company Web Scraper

A lightweight Flask-based web scraper to extract basic information from websites like company name, contact info, and more.

---

##  Implemented Features

- Input: Accepts multiple URLs (space-separated)
- Output: Extracts company name, homepage, and contact details (email)
- CSV export
- Creative UI (Bootstrap + Cow image fallback if no data found)
- Error handling
- Works in browser — zero coding required for user

---

## 🔬 Data Extraction Level

| Level        | Status |
|--------------|--------|
| Basic        | ✅ Done |
| Medium       | ✅ Done (Contact Info, Title) |
| Advanced     | ⚠️ Partial (Cow fallback, structure ready but not using APIs)

---

## 🚀 How to Run the Tool

### 1. Clone the Repo

```bash
git clone https://github.com/Dbhati02/assignment_unicraft.git

⚙️ Setup & Run Instructions
2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
🔄 Activate the environment:
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

3. Install Required Packages
pip install -r requirements.txt

4. Run the Flask App
python app.py
Then open your browser and visit:
👉 http://127.0.0.1:5000/

📁 Output Sample
Output CSV file is generated at: data/output.csv
Company Name,Website URL,Contact Info
Example Domain,https://example.com,N/A
Internet for people, not profit — Mozilla Global,https://mozilla.org,trademark-permissions@mozilla.com
Error,https://gnu.org,❌ Timed out


