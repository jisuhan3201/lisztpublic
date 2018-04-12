from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllPlans(APIView):

    def get(self, request, format=None):

        all_plans = models.Plan.objects.all()
        serializer = serializers.PlanSerializer(all_plans, many=True)

        return Response(data=serializer.data)
