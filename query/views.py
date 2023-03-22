import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Refrigerant
from .serializers import RefrigerantSerializer


# Create your views here.
class ParamsQueryView(APIView):
    def get(self, request):
        name = request.GET.get('name')
        if not name:
            return Response({"msg": "未获取到制冷剂名称"}, status=status.HTTP_400_BAD_REQUEST)
        if not Refrigerant.objects.filter(name=name).count():
            return Response({"msg": "制冷剂不存在"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(RefrigerantSerializer(Refrigerant.objects.filter(name=name), many=True).data,
                        status=status.HTTP_200_OK)

    def post(self, request):
        # print(request.data)
        param_list = ['name', 'code', 'formula', 'molecular_weight', 'curve_data', 'type', 'safety_index',
                      'env_impact_index']
        params = []
        for param in param_list:
            if not request.data.get(param):
                return Response({"msg": f"未获取到参数{param}的值"}, status=status.HTTP_400_BAD_REQUEST)
            params.append(request.data.get(param))
        try:
            Refrigerant.objects.create(name=params[0], code=params[1], formula=params[2],
                                       molecular_weight=params[3], curve_data=json.dumps(params[4]),
                                       type=params[5], safety_index=params[6], env_impact_index=params[7])
        except Exception as e:
            return Response({"msg": "创建失败", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)

    def delete(self, request):
        rid = request.data.get('rid')
        if not rid:
            return Response({"msg": "未获取到制冷剂编号"}, status=status.HTTP_400_BAD_REQUEST)
        if not Refrigerant.objects.filter(id=rid).count():
            return Response({"msg": "制冷剂不存在"}, status=status.HTTP_400_BAD_REQUEST)
        Refrigerant.objects.filter(id=rid).delete()
        return Response({"msg": "ok"}, status=status.HTTP_200_OK)


class ParamsQueryViews(APIView):
    def get(self, request):
        return Response(RefrigerantSerializer(Refrigerant.objects.all(), many=True).data, status=status.HTTP_200_OK)
