import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tms_backend.settings')
django.setup()

from core.models import Program, Donation

def seed():
    print("Cleaning old data...")
    Donation.objects.all().delete()
    Program.objects.all().delete()

    print("Creating programs...")
    p1 = Program.objects.create(name="Education for All", category="Education", description="Providing books and uniforms.")
    p2 = Program.objects.create(name="Clean Water Initiative", category="Health", description="Installing water filters in villages.")
    p3 = Program.objects.create(name="Youth Skill Development", category="Livelihood", description="Vocational training for youth.")

    print("Creating donations...")
    Donation.objects.create(program=p1, amount=Decimal("5000.00"), donor_name="Amit Sharma")
    Donation.objects.create(program=p1, amount=Decimal("2500.00"), donor_name="Priya Singh")
    Donation.objects.create(program=p2, amount=Decimal("10000.00"), donor_name="Rahul Verma")
    Donation.objects.create(program=p3, amount=Decimal("7500.00"), donor_name="Anjali Gupta")
    Donation.objects.create(program=p2, amount=Decimal("1500.00"), donor_name="Anonymous")

    print("Success! Database populated.")

if __name__ == "__main__":
    seed()
