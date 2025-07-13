# NyxVision

**Nyx Vision** is a full-stack threat intelligence platform designed to process, enrich, and classify sensitive military or intelligence reports. Using Apache NiFi for data ingestion, Python for enrichment and scoring, and Spring Boot with PostgreSQL for secure storage and access, Nyx Vision transforms raw intelligence into actionable, structured data.

---

## 🚀 Features

- **Ingest Reports via Apache NiFi**  
  Automatically detects and processes incoming raw intelligence files.

- **Threat Scoring and Enrichment (Python)**  
  Uses YAML-configured keyword scoring and contextual modifiers to generate threat scores and classifications.

- **Data Storage (Python + Parquet + PostgreSQL)**  
  Transforms enriched reports into Parquet files and stores them in a relational database.

- **Backend API (Java Spring Boot)**  
  Exposes endpoints for querying and managing enriched reports with audit trails and metadata.

- **Frontend ( React)**  
  Displays reports, scores, and metadata for analysts or administrators.

---

## 🛠️ Tech Stack

- **Apache NiFi** – Data flow orchestration  
- **Python** – ETL, keyword scanning, and threat scoring  
- **YAML** – Configuration of keywords and modifiers  
- **Parquet** – Efficient intermediate file format  
- **PostgreSQL** – Secure data storage  
- **Spring Boot (Java)** – Backend API  
- **React** – User interface  

---

## ⚙️ How It Works

1. **Ingestion**:  
   Apache NiFi monitors a folder and moves raw reports to a processing directory.

2. **Enrichment & Scoring**:  
   A Python script scans the reports, assigns threat levels based on configured keywords, and outputs enriched JSON + Parquet files.

3. **Storage**:  
   Enriched data is inserted into PostgreSQL via SQLAlchemy using the `.to_sql()` method.

4. **Backend API**:  
   Spring Boot serves the data to the frontend or authorized consumers.

---

