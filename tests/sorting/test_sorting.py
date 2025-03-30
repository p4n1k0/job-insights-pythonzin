from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    mock_job_dict = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-06-08"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-07"},
    ]
    assert_result_min = [
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-07"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-06-08"},
    ]

    assert_result_max = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-06-08"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-07"},
    ]

    assert_result_date = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-06-08"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-07"},
    ]

    sort_by(mock_job_dict, "min_salary")
    assert mock_job_dict == assert_result_min

    sort_by(mock_job_dict, "max_salary")
    assert mock_job_dict == assert_result_max

    sort_by(mock_job_dict, "date_posted")
    assert mock_job_dict == assert_result_date
