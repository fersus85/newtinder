from django_filters.rest_framework import DjangoFilterBackend


class UserFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if ('first_name' in request.GET
                or 'last_name' in request.GET
                or 'gender' in request.GET):
            return super().filter_queryset(request, queryset, view)
        users = queryset

        return queryset
