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
        
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': WomenSerializers(post_new).data})
