from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        return [item for item in csv.DictReader(file)]


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    data = read(path)
    types = []

    for job in data:
        if job["job_type"] not in types:
            types.append(job["job_type"])
    return types


get_unique_job_types('data/jobs.csv')


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobFiltered = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobFiltered.append(job)

    return jobFiltered
