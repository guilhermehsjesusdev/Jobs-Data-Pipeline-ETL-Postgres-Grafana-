from app.config import API_URLS, START_DATE, END_DATE, MAX_JOBS
from app.extractors.jobs_extractor import JobsExtractor
from app.utils.file_utils import save_json
from app.pipeline.jobs_pipeline import JobsPipeline
from datetime import datetime
from app.wait_for_db import wait_for_db
import os


def run():
    wait_for_db()
    print("=" * 50)
    print("INICIANDO EXTRAÇÃO")
    print(f"START_DATE: {START_DATE}")
    print(f"END_DATE: {END_DATE}")
    print("=" * 50)

    extractor = JobsExtractor(API_URLS, MAX_JOBS)

    jobs = extractor.extract()

    date = datetime.now().strftime("%Y-%m-%d")

    path = f"data_lake/raw/remotive/jobs_{date}.json"

    # garante que a pasta existe
    os.makedirs(os.path.dirname(path), exist_ok=True)

    save_json(jobs, path)

    print(f"\nTotal de vagas extraídas: {len(jobs)}")
    print(f"Arquivo salvo em {path}")

    # =========================
    # AQUI ENTRA O CLEAN (PIPELINE)
    # =========================
    print("\n🚀 INICIANDO CLEAN (PIPELINE)")

    pipeline = JobsPipeline(
        sources=API_URLS,
        max_jobs=MAX_JOBS
    )

    pipeline.run()