from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    salary = 0
    for job in data:
        try:
            if int(job['max_salary']) > salary:
                salary = int(job['max_salary'])
        except ValueError:
            salary

    return salary


def get_min_salary(path: str) -> int:
    data = read(path)
    salary = get_max_salary(path)

    for job in data:
        try:
            if int(job['min_salary']) < salary:
                salary = int(job['min_salary'])
        except ValueError:
            salary
    return salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError
        max_salary = int(job['max_salary'])
        min_salary = int(job['min_salary'])
        if min_salary > max_salary:
            raise
        compare_salary = int(salary)
    except Exception:
        raise ValueError
    
    return min_salary <= compare_salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
