from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1


class CustomPagination(PageNumberPagination):
    """
    Custom pagination class that extends the PageNumberPagination class
    provided by Django REST framework.

    This class provides a custom response format that includes links to
    the next and previous pages, the total number of items in the queryset,
    the current page number, the page size, and the results for the current page.
    """

    page = 1
    page_size = 30
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        """
        Return a custom paginated response that includes links to the next and
        previous pages, the total number of items in the queryset, the current
        page number, the page size, and the results for the current page.

        Args:
            data (list): The list of objects for the current page.

        Returns:
            Response: A Response object with the custom paginated response format.
        """
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "total": self.page.paginator.count,
                "page": int(self.request.GET.get("page", DEFAULT_PAGE)),
                "page_size": int(self.request.GET.get("page_size", self.page_size)),
                "results": data,
            }
        )
