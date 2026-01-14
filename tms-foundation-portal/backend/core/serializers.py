from rest_framework import serializers

from .models import Donation, Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ["id", "name", "category", "description", "is_active", "start_date"]


class DonationSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = Donation
        fields = ["id", "program", "amount", "donor_name", "created_at"]


class ImpactSummarySerializer(serializers.Serializer):
    total_amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    donation_count = serializers.IntegerField()
    active_programs = serializers.IntegerField()

