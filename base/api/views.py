from rest_framework import generics, mixins
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser

# mixins
class mixins_list(mixins.ListModelMixin, mixins.CreatModelMixin, generics.GenericAPIView) : 
    queryset = User.objects.all() 
    serializer_class = UserSerializer

# get/post
    def get(self, request) : 
        return self.list(request)

    def post(self, request) : 
        return self.create(request)

# get/update/delete
class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView) :
      queryset = User.objects.all()
      serializer_class = UserSerializer

      def get(self, request, pk) : 
        return self.retrieve(request)

      def put(self, request, pk) : 
        return self.update(request)

      def delete(self, request, pk) : 
        return self.destroy(request)
  



