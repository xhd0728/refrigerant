from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from .utils.process import cal_refrigeration_params
from .models import Record
from .serializers import CalculateRecordSerializer


# Create your views here.
class ParamsCalculateView(APIView):
    def get(self, request):
        return Response(CalculateRecordSerializer(Record.objects.all(), many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        h_0 = request.data.get('h_0')
        h_1 = request.data.get('h_1')
        h_2 = request.data.get('h_2')
        h_3 = request.data.get('h_3')
        h_4 = request.data.get('h_4')
        v_1 = request.data.get('v_1')
        n_i = request.data.get('n_i')
        r = request.data.get('r')
        Q = request.data.get('Q')
        res_dict = cal_refrigeration_params(h_0, h_1, h_2, h_3, h_4, v_1, n_i, r, Q)
        if res_dict.get('error'):
            error = res_dict.get("error")
            param_required = res_dict.get("param_required")
            return Response({"msg": "缺少参数", "error": error, "param_required": param_required},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            json_data = json.dumps(res_dict)
            Record.objects.create(data=json_data)
            return Response({"msg": "ok", "data": res_dict}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": "存储失败", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        rid = request.data.get('rid')
        if not rid:
            return Response({"msg": "未获取到记录编号"}, status=status.HTTP_400_BAD_REQUEST)
        if not Record.objects.filter(id=rid).count():
            return Response({"msg": "记录不存在"}, status=status.HTTP_400_BAD_REQUEST)
        Record.objects.filter(id=rid).delete()
        return Response({"msg": "ok"}, status=status.HTTP_200_OK)
