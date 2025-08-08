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
+----------------+         +------------------+        +-----------------+
|  Civic Sources |         | Data Pipeline &  |        |  Vector Store   |
| (MyGov, PRS,   |   -->   |  Cleaning        |  -->   | (FAISS/Chroma)  |
|  RTI, Nyaaya)  |         +------------------+        +-----------------+
       |                                                        |
       |                                                        v
       |                                                +--------------+
       |--------------------------------------------->  |   RAG LLM    |
                                                        |  (Watsonx)   |
                                                        +--------------+
                                                               |
                                                               v
                                                      +------------------+
                                                      |  CIVICA Agent UI |
                                                      |   (Web/Mobile)   |
                                                      +------------------+
```

- **Civic Sources**: Curated legal, policy, and governance datasets.
- **Data Pipeline**: Cleans, tokenizes, and indexes data into vector space.
- **Vector Store**: Stores state-wise documents for semantic search (FAISS, ChromaDB).
- **RAG LLM**: Watsonx-powered Retrieval-Augmented Generation using civic vectors.
- **Agent UI**: User interface to query, receive answers, and give feedback.

---

## 🚀 Deployment

**Tech Stack:**
- IBM Watsonx.ai for LLM fine-tuning and RAG
- Chroma / FAISS for vector storage
- Python (FastAPI) backend
- React Native frontend (WIP)
- Data crawlers for automated updates
- GitHub Actions for CI/CD

**Deployment Options:**
- IBM Cloud
- Dockerized microservices
- REST and WebSocket APIs
- Edge-ready for mobile and kiosk devices

---

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/civica-agent.git
cd civica-agent

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn main:app --reload

# (Optional) Start frontend
cd frontend && npm install && npm run dev
```

---

## ✅ Features

- Multilingual civic Q&A (state-specific)
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
