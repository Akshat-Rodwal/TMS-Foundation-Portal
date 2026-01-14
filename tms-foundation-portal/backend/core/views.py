from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Donation, Program
from .serializers import DonationSerializer, ImpactSummarySerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"})


class ImpactSummaryView(APIView):
    def get(self, request):
        total_amount = Donation.objects.aggregate(sum=Sum("amount"))["sum"] or 0
        donation_count = Donation.objects.count()
        active_programs = Program.objects.filter(is_active=True).count()
        data = {
            "total_amount": total_amount,
            "donation_count": donation_count,
            "active_programs": active_programs,
        }
        serializer = ImpactSummarySerializer(data)
        return Response(serializer.data)


class DonationListView(generics.ListAPIView):
    queryset = Donation.objects.select_related("program").order_by("-created_at")
    serializer_class = DonationSerializer

