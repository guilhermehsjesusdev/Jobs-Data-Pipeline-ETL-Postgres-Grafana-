import requests

from app.services.jobs_normalization_service import JobsNormalizationService


class JobsExtractor:

    def __init__(self, urls, max_jobs):

        self.urls = urls
        self.max_jobs = max_jobs

    def extract(self):

        all_jobs = []

        for url in self.urls:

            print(f"\nConsumindo API: {url}")

            try:

                response = requests.get(url, timeout=10)

                response.raise_for_status()

                data = response.json()

                jobs = []

                if "jobs" in data:
                    jobs = data["jobs"][:self.max_jobs]

                elif "data" in data:
                    jobs = data["data"][:self.max_jobs]

                for job in jobs:

                    normalized_job = (
                        JobsNormalizationService.normalize_job(
                            job=job,
                            source_name=url.split("//")[-1].split("/")[0],
                            source_url=url
                        )
                    )

                    all_jobs.append(normalized_job)
                    print(f"Jobs encontrados em {url}: {len(jobs)}")

            except Exception as error:

                print(f"Erro ao consumir API {url}: {error}")

        return all_jobs