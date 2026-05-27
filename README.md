# 🚀 Jobs Data Pipeline (ETL + Postgres + Grafana)

Este projeto implementa um pipeline completo de engenharia de dados para coleta, transformação e análise de vagas de emprego remotas.

O sistema segue uma arquitetura de Data Lake (Raw → Clean → Curated) com persistência em PostgreSQL e visualização via Grafana.

---

## 🧱 Arquitetura

API (Jobs Sources)
        ↓
   Extract Layer
        ↓
   Raw Data (Data Lake)
        ↓
   Transform Layer (Normalization + Curation)
        ↓
   Clean Data (Data Lake)
        ↓
   Curated Data (Analytics-ready)
        ↓
   PostgreSQL (Data Warehouse)
        ↓
   Grafana (Dashboards)

---

## ⚙️ Tecnologias

- Python 3.10+
- PostgreSQL 15
- Docker & Docker Compose
- Grafana
- psycopg2
- ETL Pipeline customizado

---

## 📦 Estrutura do Projeto

app/
 ├── extractors        -> Coleta de dados das APIs
 ├── services          -> Normalização e regras de negócio
 ├── transformers      -> Curadoria e agregações
 ├── repositories      -> Persistência no Postgres
 ├── pipeline          -> Orquestração do ETL
 ├── db                -> Conexão com banco
 ├── utils             -> Helpers (JSON etc.)

data_lake/
 ├── raw
 ├── clean
 ├── curated

---

## 🚀 Como rodar o projeto

### Subir ambiente completo

docker-compose up --build -d

---

### Ver containers

docker ps

---

### Acessos

Postgres:
localhost:5432

Grafana:
http://localhost:3000
user: admin
password: admin

---

## 📊 Queries úteis (Postgres)

### Vagas por categoria
SELECT category, COUNT(*) AS total
FROM jobs_curated
GROUP BY category
ORDER BY total DESC;

---

### Vagas por empresa
SELECT company, SUM(total_jobs) AS total
FROM jobs_curated
GROUP BY company
ORDER BY total DESC;

---

### Evolução diária de vagas
SELECT job_date, COUNT(*) AS total
FROM jobs_curated
GROUP BY job_date
ORDER BY job_date;

---

## 🔄 Pipeline ETL

1. Extract (APIs de vagas)
2. Salva RAW
3. Normaliza dados (CLEAN)
4. Gera dados CURATED
5. Salva no PostgreSQL
6. Alimenta dashboards Grafana

---

## 📈 Objetivo

Simular um ambiente real de engenharia de dados com:

- Pipeline ETL completo
- Data Lake (Raw → Clean → Curated)
- Banco relacional para analytics
- Dashboard BI (Grafana)
- Tratamento de dados inconsistentes

---

## 🧠 Conceitos aplicados

- ETL / ELT
- Data Lake Architecture
- Data Warehouse básico
- Data Cleaning
- Data Curated Layer
- Pipeline orchestration
- Dockerized environment

---

## 👨‍💻 Autor

Projeto de estudo para portfólio em Data Engineering / Backend Data Pipelines