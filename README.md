# Plagg- Image & Text based PLagiarism Detector

Plagg is a full-stack academic plagiarism detection system that analyzes text documents and image based-question content(via OCR) to identify potential plagiarism using NLP and similarity matching techniques.
This project is my college major project. It focuses on modular architecture, extensibility and real-world plagiarism workflows. 

## Features
* Text-based plagiarism detection(DOCX, PDF)
* Image-based plagiarism detection using OCR
* Sentence-level similarity analysis
* Hybrid similarity engine
* Plagiarism percentage scoring
* FastAPI backend
* Next.js frontend dashboard
* Swagger UI for API testing
* Modular, production-style backend strucuture

## Tech Stack 

### Backend 
* Python
* FastAPI
* Pydantic
* NLTK/SpaCy
* Sentence Transformers
* Tesseract OCR
* OpenCV
* Uvicorn

### Frontend
Used V0 by vercel for generation and then integrated it 
* Next.js
* TypeScript
* Tailwind CSS
* Fetch API

## Project Architecture
![Architecture](https://github.com/Purushottam29/Plagiarism_Detector/blob/7dd2757dc4dc52e4296b96820fc557a6a62e983a/assets/Architecture.png)

## Project Structure
![Tree1](https://github.com/Purushottam29/Plagiarism_Detector/blob/7dd2757dc4dc52e4296b96820fc557a6a62e983a/assets/Tree1.png)
![Tree2](https://github.com/Purushottam29/Plagiarism_Detector/blob/7dd2757dc4dc52e4296b96820fc557a6a62e983a/assets/Tree2.png)
![Tree3](https://github.com/Purushottam29/Plagiarism_Detector/blob/7dd2757dc4dc52e4296b96820fc557a6a62e983a/assets/Tree3.png)
![Tree4](https://github.com/Purushottam29/Plagiarism_Detector/blob/7dd2757dc4dc52e4296b96820fc557a6a62e983a/assets/Tree4.png)
![Tree5](https://github.com/Purushottam29/Plagiarism_Detector/blob/7dd2757dc4dc52e4296b96820fc557a6a62e983a/assets/Tree5.png)

## Workflow
1. Upload Document
2. Ingestion
3. NLP Pipeline
4. Plagiarism Detection
5. Report Generation

## Current Status
* Backend Plagiarism logic is under active development
* A temporary UI mode is enabled to stimulate plagiarism percentage for presentation
* Sentence match result are currently hidden(by design for demo stability)

## How to run locally
### Backend
1. Create virtual environment and then install the dependencies form requirements file.
```bash
python3 -m venv plag
source plag/bin/activate
pip install -r requirements.txt
```
2. Start the backend go to swagger ui for backend testing by localhostlink/docs
```bash 
uvicorn app.main:app --reload
```

### Frontend
1. Install the package using
```bash
npm install
```
2. Run the frontend server
```bash
npm run dev
```

## Future Improvements
* AI-generated text detection
* Web-based corpus crawling
* Database-backed corpus storage
* Detailed sentence highlighting
* User authentication
* Model fine tuning for academic datasets

## Author
### Purushottam Choudhary
B.Tech Computer Science
* Github: https://github.com/Purushottam29
* LinkedIN: https://www.linkedin.com/in/purushottam-choudhary-166120373
* Mail: purushottamchoudhary2910@gmail.com
