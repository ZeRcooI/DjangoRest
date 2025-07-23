from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializers


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()

        return Response({'posts': WomenSerializers(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exist'})

        serializer = WomenSerializers(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({'error': 'Method DELETE not allowed'})
    #
    #     return Response({'post': 'delete post ' + str(pk)})
