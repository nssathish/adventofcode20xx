import os


def parse(path: str, kwargs) -> list:
    link = os.path.realpath(path)
    if kwargs["separator"] == "\n":
        return _parse_lines(link)

    if kwargs["separator"] == ",":
        return _parse_csv(link)

    return []

def _parse_lines(link: str) -> list:
    with open(link) as f:
        lines = f.readlines()
        lines = [line.strip('\n') for line in lines]

    return lines

def _parse_csv(link: str) -> list:
    with open(link) as f:
        lines = f.readline()
        lines = [line.strip().split("-") for line in lines.split(",")]

    return lines