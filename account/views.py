from rest_framework.viewsets import ModelViewSet

from account.models import Account
from account.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    my_tags = ('account',)
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

