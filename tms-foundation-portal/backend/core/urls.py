from django.urls import path

from .views import DonationListView, HealthCheckView, ImpactSummaryView

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("impact/summary/", ImpactSummaryView.as_view(), name="impact-summary"),
    path("donations/", DonationListView.as_view(), name="donation-list"),
]

