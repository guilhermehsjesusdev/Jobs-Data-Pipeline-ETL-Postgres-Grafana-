from datetime import datetime, timezone


class JobsNormalizationService:

    @staticmethod
    def normalize_job(job, source_name, source_url):

        return {
            "source_name": source_name,
            "source_url": source_url,

            "ingestion_time_utc": datetime.now(timezone.utc).isoformat(),

            "title": job.get("title"),

            "company": job.get("company_name") or job.get("company"),

            "category": job.get("category"),

            "publication_date": job.get("publication_date") or job.get("date")
        }