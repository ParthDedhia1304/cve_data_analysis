# NLP-Powered CVE Analysis and Similarity Search Platform

[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)](https://www.mongodb.com/cloud/atlas)
[![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-blueviolet.svg)](https://www.pinecone.io/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-yellow)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
[![Deployment](https://img.shields.io/badge/Deployment-Render-lightgrey.svg)](https://render.com)

An intelligent web application designed to streamline the analysis of **Common Vulnerabilities and Exposures (CVEs)**. This project leverages Natural Language Processing (NLP) to provide a user-friendly dashboard, detailed CVE summaries, and a powerful similarity search to find related vulnerabilities based on natural language descriptions.


---

![Project Screenshot](https://github.com/user-attachments/assets/d9f8d8fb-9277-420a-ad6a-6b925d360f54)

## 🌟 Features

This project offers a comprehensive suite of tools for vulnerability analysis:

* **📊 Interactive Dashboard**: A user-friendly dashboard that visualizes key CVE metrics and trends using **Plotly**, including average CVSS scores, total vulnerabilities, and more.
* **🧠 NLP-Powered Summaries**: Utilizes **GROQ** with the **LLaMA 3.1 8B model** to generate clear, human-readable summaries of complex CVE details, including impact, exploitability, and potential patches.
* **🔎 Advanced Similarity Search**: Find the top 5 similar CVEs by describing a cyber attack in natural language. This feature is powered by a **RAG (Retrieval-Augmented Generation)** approach using vector embeddings stored in **Pinecone**.
* **📄 Detailed CVE Lookup**: Search for any specific CVE by its ID to get comprehensive information, including description, CVSS score, impact metrics, and references.
* **⚙️ Automated Data Pipeline**: The entire data workflow is automated, from **data extraction** from NVD sources to **cleaning, preprocessing, and storage** in **MongoDB Atlas**.

---

## 🛠️ Technology Stack

This project integrates a modern stack of technologies for a robust and efficient solution:

* **Backend**: **Flask** for the web server and API endpoints.
* **Database**:
    * **MongoDB Atlas**: Primary NoSQL database for storing structured CVE data.
    * **Pinecone**: High-performance vector database for similarity search.
* **Frontend**: **HTML**, **CSS (Tailwind CSS)**, and **JavaScript** for a responsive and interactive user interface.
* **NLP & Machine Learning**:
    * **GROQ with LLaMA 3.1 8B**: For fast and efficient NLP inference and text generation.
    * **Sentence-Transformers (`all-MiniLM-L6-v2`)**: For generating high-quality semantic vector embeddings.
    * **Transformers (BERT)**: Used for tokenization.
* **Data Visualization**: **Plotly** for creating interactive charts on the dashboard.
* **Deployment**: **Render** and **Gunicorn** for scalable deployment.

---

## ⚙️ System Workflow

The project follows a structured workflow from data collection to user interaction:

1.  **Data Extraction**: CVE data is automatically collected from NVD sources.
2.  **Data Cleaning**: The raw data is rigorously cleaned—handling missing values and filtering out irrelevant "REJECTED" entries.
3.  **Data Storage**: The cleaned CVE data is stored in **MongoDB Atlas**.
4.  **Embedding Generation**: The CVE descriptions are converted into vector embeddings using the `all-MiniLM-L6-v2` model.
5.  **Vector Indexing**: These embeddings are indexed in **Pinecone** for fast similarity search.
6.  **User Interaction**: Users access the Flask web application to view the dashboard, search for CVEs, or find similar vulnerabilities.

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.12 or higher
* A MongoDB Atlas account and connection string
* A Pinecone account and API key
* A GROQ API key

### Installation & Configuration

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/nlp-cve-analysis.git](https://github.com/yourusername/nlp-cve-analysis.git)
    cd nlpProject-main
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your API keys and database URI:
    ```
    MONGODB_URI="your_mongodb_connection_string"
    PINECONE_API_KEY="your_pinecone_api_key"
    GROQ_API_KEY="your_groq_api_key"
    ```
    *Note: The `.env` file is ignored by Git to protect your credentials.*

4.  **Run the Flask application:**
    ```bash
    python main.py
    ```

5.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 💡 Future Improvements

* **Real-time Data Pipeline**: Implement a real-time data pipeline to keep the CVE database continuously updated.
* **User Accounts**: Add user authentication to allow for personalized dashboards and saved searches.
* **Advanced Analytics**: Enhance the dashboard with more advanced analytics, such as threat forecasting and trend analysis.
* **Full RAG Implementation**: Expand the similarity search to a full RAG model that generates a comprehensive summary based on the retrieved CVEs.

---


