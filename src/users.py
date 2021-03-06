from src.models import GitHubUserOrm, GitHubUser
from src.db import session


def get_paginated_users(
    rows_per_page: int, page_number: int
) -> tuple[list[GitHubUserOrm], int, int]:
    """
    :param rows_per_page: How many rows will a table page contain
    :param page_number: The actual page number to fetch
    :return: The user list, with the rows and page info
    """
    rows = rows_per_page if rows_per_page > 0 else 1
    page = page_number if page_number > 0 else 1

    raw_users = session.query(GitHubUserOrm).limit(rows).offset((page - 1) * rows).all()

    return [GitHubUser.from_orm(user).dict() for user in raw_users], rows, page
