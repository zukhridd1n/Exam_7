from rest_framework.filters import BaseFilterBackend


class FilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        salary_from = request.query_params.get('salary_from', None)
        salary_to = request.query_params.get('salary_to', None)
        salary = request.query_params.get('salary', None)
        if salary_to:
            queryset = queryset.filter(salary__gte=salary_to)
        if salary_from:
            queryset = queryset.filter(salary__lte=salary_from)
        if salary:
            queryset = queryset.filter(salary=salary)
        return queryset