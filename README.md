# 🚀 Jobs Data Pipeline

> Pipeline completo de engenharia de dados para coleta, transformação e análise de vagas de emprego remotas — com arquitetura Data Lake, PostgreSQL e dashboards no Grafana.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?style=flat-square&logo=grafana&logoColor=white)

---

## 📋 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Arquitetura](#-arquitetura)
- [Tecnologias](#️-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Rodar](#-como-rodar)
- [Queries Úteis](#-queries-úteis)
- [Pipeline ETL](#-pipeline-etl)
- [Conceitos Aplicados](#-conceitos-aplicados)

---

## 📌 Sobre o Projeto

Este projeto simula um ambiente real de engenharia de dados, implementando um **pipeline ETL completo** para ingestão, tratamento e análise de vagas de emprego remotas.

O sistema segue a arquitetura de **Data Lake em três camadas** (Raw → Clean → Curated), com persistência em PostgreSQL e visualização via Grafana — ideal como projeto de portfólio em **Data Engineering** e **Backend Data Pipelines**.

---

## 🧱 Arquitetura

```
API (Jobs Sources)
        │
        ▼
   Extract Layer          ← Coleta de dados das fontes
        │
        ▼
   Raw Data               ← Data Lake: dados brutos
        │
        ▼
   Transform Layer        ← Normalização + Curadoria
        │
        ▼
   Clean Data             ← Data Lake: dados normalizados
        │
        ▼
   Curated Data           ← Analytics-ready
        │
        ▼
   PostgreSQL             ← Data Warehouse
        │
        ▼
   Grafana                ← Dashboards & Visualizações
```

---

## ⚙️ Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.10+ | Pipeline ETL |
| PostgreSQL | 15 | Data Warehouse |
| Docker & Docker Compose | — | Orquestração de containers |
| Grafana | — | Dashboards e visualizações |
| psycopg2 | — | Conexão Python ↔ PostgreSQL |

---

## 📦 Estrutura do Projeto

```
jobs-data-pipeline/
│
├── app/
│   ├── extractors/       # Coleta de dados das APIs
│   ├── services/         # Normalização e regras de negócio
│   ├── transformers/     # Curadoria e agregações
│   ├── repositories/     # Persistência no PostgreSQL
│   ├── pipeline/         # Orquestração do ETL
│   ├── db/               # Conexão com o banco
│   └── utils/            # Helpers (JSON, etc.)
│
└── data_lake/
    ├── raw/              # Dados brutos extraídos da API
    ├── clean/            # Dados normalizados
    └── curated/          # Dados prontos para analytics
```

---

## 🚀 Como Rodar

### Pré-requisitos

- Docker e Docker Compose instalados

### 1. Subir o ambiente completo

```bash
docker-compose up --build -d
```

### 2. Verificar containers em execução

```bash
docker ps
```

### 3. Acessos

| Serviço | Endereço | Credenciais |
|---|---|---|
| PostgreSQL | `localhost:5432` | — |
| Grafana | `http://localhost:3000` | `admin` / `admin` |

---

## 📊 Queries Úteis (PostgreSQL)

### Vagas por categoria

```sql
SELECT category, COUNT(*) AS total
FROM jobs_curated
GROUP BY category
ORDER BY total DESC;
```

### Vagas por empresa

```sql
SELECT company, SUM(total_jobs) AS total
FROM jobs_curated
GROUP BY company
ORDER BY total DESC;
```

### Evolução diária de vagas

```sql
SELECT job_date, COUNT(*) AS total
FROM jobs_curated
GROUP BY job_date
ORDER BY job_date;
```

---

## 🔄 Pipeline ETL

O pipeline segue as seguintes etapas em sequência:

```
1. Extract    →  Consome APIs de vagas de emprego
2. Raw Save   →  Persiste os dados brutos no Data Lake
3. Normalize  →  Limpa e padroniza os dados (camada Clean)
4. Curate     →  Gera agregações e métricas (camada Curated)
5. Load       →  Salva os dados no PostgreSQL
6. Visualize  →  Alimenta os dashboards no Grafana
```

---

## 🧠 Conceitos Aplicados

- **ETL / ELT** — extração, transformação e carga de dados
- **Data Lake Architecture** — camadas Raw, Clean e Curated
- **Data Warehouse** — modelagem relacional para analytics
- **Data Cleaning** — tratamento de dados inconsistentes
- **Pipeline Orchestration** — controle de fluxo entre etapas
- **Dockerized Environment** — ambiente isolado e reproduzível

---

## 👨‍💻 Autor

Projeto de estudo desenvolvido para portfólio em **Data Engineering** e **Backend Data Pipelines**.

---

> ⭐ Se este projeto foi útil, considere deixar uma estrela no repositório!
