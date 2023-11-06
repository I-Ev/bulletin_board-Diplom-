from rest_framework import pagination


class AdPagination(pagination.PageNumberPagination):
    """
    Пагинация для списка объявлений.
    """
    page_size = 4
    page_query_param = 'page'