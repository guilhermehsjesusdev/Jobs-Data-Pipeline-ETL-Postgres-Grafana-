from collections import Counter


class JobsCuratedService:

    @staticmethod
    def build_by_category(jobs):

        counter = Counter(
            str(job.get("category", "unknown"))
            for job in jobs
        )

        return [
            {"category": k, "total_jobs": v}
            for k, v in counter.items()
        ]

    @staticmethod
    def build_by_company(jobs):

        counter = Counter(
            str(job.get("company", "unknown"))
            for job in jobs
        )

        return [
            {"company": k, "total_jobs": v}
            for k, v in counter.items()
        ]

    @staticmethod
    def build_by_date(jobs):

        counter = Counter(
            str(job.get("publication_date", "unknown"))[:10]
            for job in jobs
        )

        return [
            {"date": k, "total_jobs": v}
            for k, v in counter.items()
        ]