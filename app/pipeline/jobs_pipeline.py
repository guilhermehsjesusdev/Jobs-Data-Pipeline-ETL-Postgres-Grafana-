from datetime import datetime

from app.services.jobs_curated_service import JobsCuratedService
from app.extractors.jobs_extractor import JobsExtractor
from app.services.jobs_normalization_service import JobsNormalizationService
from app.utils.file_utils import save_json
from app.repositories.jobs_repository import JobsRepository
from app.repositories.company_repository import CompanyRepository


class JobsPipeline:

    def __init__(self, sources, max_jobs, storage_path="data_lake"):
        self.sources = sources
        self.max_jobs = max_jobs
        self.storage_path = storage_path

    def run(self):

        extractor = JobsExtractor(self.sources, self.max_jobs)
        raw_jobs = extractor.extract()

        date = datetime.now().strftime("%Y-%m-%d")

        # =========================
        # RAW
        # =========================
        print("\n===== RAW DEBUG =====")
        print("RAW SIZE:", len(raw_jobs))
        print("RAW EXEMPLO:", raw_jobs[:1])
        print("=====================\n")

        raw_path = f"{self.storage_path}/raw/jobs_{date}.json"
        save_json(raw_jobs, raw_path)

        # =========================
        # CLEAN
        # =========================
        clean_jobs = []

        for j in raw_jobs:
            try:
                clean_jobs.append(
                    JobsNormalizationService.normalize_job(
                        job=j,
                        source_name=j.get("source_name", "unknown"),
                        source_url=j.get("source_url", "unknown")
                    )
                )
            except Exception as e:
                print("\n❌ ERRO NA NORMALIZAÇÃO")
                print("ERRO:", e)
                print("JOB PROBLEMÁTICO:", j)

        print("\n===== CLEAN DEBUG =====")
        print("CLEAN SIZE:", len(clean_jobs))
        print("CLEAN EXEMPLO:", clean_jobs[:1])
        print("======================\n")

        clean_path = f"{self.storage_path}/clean/jobs_{date}.json"
        save_json(clean_jobs, clean_path)

        # =========================
        # CURATED
        # =========================
        curated_by_category = JobsCuratedService.build_by_category(clean_jobs)
        curated_by_company = JobsCuratedService.build_by_company(clean_jobs)
        curated_by_date = JobsCuratedService.build_by_date(clean_jobs)

        print("\n🚨 CURATED DEBUG")
        print("CATEGORY:", len(curated_by_category))
        print("COMPANY:", len(curated_by_company))
        print("DATE:", len(curated_by_date))

        curated_category_path = f"{self.storage_path}/curated/category_{date}.json"
        curated_company_path = f"{self.storage_path}/curated/company_{date}.json"
        curated_date_path = f"{self.storage_path}/curated/date_{date}.json"

        save_json(curated_by_category, curated_category_path)
        save_json(curated_by_company, curated_company_path)
        save_json(curated_by_date, curated_date_path)

        # =========================
        # COMPANY (ULTRA ROBUSTO)
        # =========================
        company_list = []

        for j in clean_jobs:

            company = j.get("company")

            # dict -> pega nome correto
            if isinstance(company, dict):
                company = company.get("name") or company.get("company")

            # list -> pega primeiro elemento válido
            if isinstance(company, list):
                company = next((c for c in company if c), None)

            # string inválida
            if not isinstance(company, str):
                continue

            company = company.strip()

            if not company:
                continue

            company_list.append({
                "name": company,
                "logo_url": None,
                "website": None,
                "url": None
            })

        print("\n🚨 COMPANY DEBUG:", len(company_list))

        # remove duplicados
        unique = {}
        for c in company_list:
            unique[c["name"]] = c

        company_list = list(unique.values())

        if company_list:
            CompanyRepository.insert_companies(company_list)
        else:
            print("⚠️ Nenhuma company válida para inserir")

        # =========================
        # LOAD (POSTGRES)
        # =========================
        print("\n🚀 SALVANDO CURATED NO POSTGRES...")

        if curated_by_category:
            JobsRepository.insert_curated(curated_by_category)

        if curated_by_company:
            JobsRepository.insert_curated(curated_by_company)

        if curated_by_date:
            JobsRepository.insert_curated(curated_by_date)

        # =========================
        # RESUMO FINAL
        # =========================
        print("\n📊 RESUMO FINAL")
        print("RAW:", len(raw_jobs))
        print("CLEAN:", len(clean_jobs))
        print("CURATED:", len(curated_by_category), len(curated_by_company), len(curated_by_date))
        print("COMPANIES:", len(company_list))

        print("\n✅ PIPELINE FINALIZADO COM SUCESSO")