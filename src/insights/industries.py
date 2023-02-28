from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries = []

    for job in data:
        if job['industry'] != '' and job['industry'] not in industries:
            industries.append(job['industry'])

    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobFitered = []

    for job in jobs:
        if job['industry'] == industry:
            jobFitered.append(job)

    return jobFitered
