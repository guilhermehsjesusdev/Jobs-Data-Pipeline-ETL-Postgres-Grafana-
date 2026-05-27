from app.db.postgres import get_connection


def safe_value(v):
    if v is None or v == "None" or v == "":
        return None
    return v


class JobsRepository:

    @staticmethod
    def insert_curated(rows):

        if not rows:
            print("⚠️ Nenhum dado para inserir em jobs_curated")
            return

        conn = get_connection()
        cur = conn.cursor()

        for r in rows:

            category = safe_value(r.get("category"))
            company = safe_value(r.get("company"))
            job_date = safe_value(r.get("date"))
            total_jobs = r.get("total_jobs")

            # 🔥 LOG DE SEGURANÇA (opcional mas recomendado)
            if job_date == "None":
                job_date = None

            cur.execute("""
                INSERT INTO jobs_curated (category, company, job_date, total_jobs)
                VALUES (%s, %s, %s, %s)
            """, (
                category,
                company,
                job_date,
                total_jobs
            ))

        conn.commit()
        cur.close()
        conn.close()