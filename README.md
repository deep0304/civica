# CIVICA - AI for Active, Smart Citizens

CIVICA is an AI-powered assistant that helps Indian citizens understand their rights, access public schemes, report civic issues, and participate in governance. It translates government policies, RTI laws, and grievance redressal systems into simple, localized, and actionable responses.

## 🧠 Project Brief

CIVICA aims to:
- Educate users about their rights, legal duties, and civic procedures.
- Simplify complex government policies into accessible information.
- Provide state-wise guidance on reporting civic issues like waste, water, and corruption.
- Encourage participation in public campaigns and local governance initiatives.
- Enable real-time civic support using multilingual AI models.

## 🎯 SDG Alignment
CIVICA contributes to:
- **Sustainable Cities and Communities**
- **Climate Action**
- **Peace, Justice, and Strong Institutions**

---

## ⚙️ System Architecture

```
+------------------+           +--------------------------+           +------------------+
|   Frontend (UI)  |  ----->   |  Python HTTP Server      |  ----->   |  Watsonx RAG LLM |
|  (Web Interface) |  Query    |  - Receives user input   |  Query    |  (Deployed on     |
| (HTML/JS Static) |           |  - Forwards to Watsonx   |           |   IBM Cloud)      |
+------------------+           +--------------------------+           +------------------+
       ^                                                                 |
       |                                                                 v
       +------------------------------------------------------+         
       | Watsonx internally handles:                          |
       |  ✅ Civic Data Index (vectorized knowledge)          |
       |  ✅ Grounded answers via Retrieval + Generation       |
       +------------------------------------------------------+

```

- **Civic Sources**: Curated legal, policy, and governance datasets.
- **Data Pipeline**: Cleans, tokenizes, and indexes data into vector space.
- **Vector Store**: Stores state-wise documents for semantic search (FAISS, ChromaDB).
- **RAG LLM**: Watsonx-powered Retrieval-Augmented Generation using civic vectors.
- **Agent UI**: User interface to query, receive answers, and give feedback.

---

## 🚀 Deployment

**Tech Stack:**
- IBM Watsonx.ai for LLM grounded with the vector document for  (RAG functionality)
- Python backend (Flask-like using `app.py`)
- Static HTML/JS frontend served via `http.server`
- GitHub Actions for CI/CD

**Deployment Options:**
- IBM Cloud
- Local deployment using Python HTTP and app server
- REST API-based communication

---

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/civica.git
cd civica

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run backend
python3 app.py

# Start frontend (new terminal)
python3 -m http.server 8080
```

---

## ✅ Features

- RTI process guidance
- Grievance redressal steps (waste, water, corruption)
- Scheme eligibility explanations
- Real-time policy updates
- Local initiative discovery (tree drives, voting, etc.)

---

## 📚 Data Sources

- [MyGov](https://www.mygov.in/)
- [RTI Portal](https://rtionline.gov.in/)
- [PRS Legislative Research](https://prsindia.org/)
- [Nyaaya](https://nyaaya.org/)
- State municipal portals

---

## 🛡️ Ethical Considerations

- Anchored to verified data to reduce misinformation.
- User feedback loop for response refinement.
- No storage of personal data; privacy-first design.
- Inclusive content for youth, rural, and marginalized populations.

---

## 📈 Future Roadmap

- Add support for voice queries.
- Launch Android/iOS apps.
- Expand database to cover all Indian states.
- Partner with local governments and NGOs.
- AI-driven recommendation for civic actions.
