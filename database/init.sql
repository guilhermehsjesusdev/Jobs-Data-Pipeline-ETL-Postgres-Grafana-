-- =========================================
-- DATABASE INIT - JOBS DATA PLATFORM
-- =========================================

-- cria tabela principal de CURATED
CREATE TABLE IF NOT EXISTS jobs_curated (
    id SERIAL PRIMARY KEY,

    category TEXT,
    company TEXT,
    job_date DATE,

    total_jobs INTEGER NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DIM COMPANY
CREATE TABLE IF NOT EXISTS dim_company (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    logo_url TEXT,
    website TEXT,
    url TEXT
);

-- índice para performance (Grafana vai usar isso)
CREATE INDEX IF NOT EXISTS idx_jobs_curated_category
ON jobs_curated(category);

CREATE INDEX IF NOT EXISTS idx_jobs_curated_company
ON jobs_curated(company);

CREATE INDEX IF NOT EXISTS idx_jobs_curated_date
ON jobs_curated(job_date);

-- =========================================
-- TABELA RAW (opcional - para auditoria)
-- =========================================

CREATE TABLE IF NOT EXISTS jobs_raw (
    id SERIAL PRIMARY KEY,
    source_name TEXT,
    source_url TEXT,
    payload JSONB,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- índice JSON (útil para debug)
CREATE INDEX IF NOT EXISTS idx_jobs_raw_payload
ON jobs_raw USING GIN (payload);