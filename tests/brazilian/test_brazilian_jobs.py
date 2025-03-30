from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    translated = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    assert translated in read_brazilian_file("tests/mocks/brazilians_jobs.csv")
