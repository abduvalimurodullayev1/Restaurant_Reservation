from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class RestaurantPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 250

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "per_page": self.page_size,
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "total": self.page.paginator.count,
                "results": data,
            }
        )
