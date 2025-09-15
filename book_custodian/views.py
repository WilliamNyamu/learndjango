from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Book Custodian Successfully Integrated")

custodians_data = {
    "name": "Maria",
    "age": 28,
    "department": "Theology",
    "salary": "50000"
}

def detail(request):
    return HttpResponse(f"<h2>{custodians_data.get("name", {})}, a {custodians_data.get("age", {})} year old lady works at the department of {custodians_data.get("department", {})} for a salary of ${custodians_data.get("salary", {})} per month.</h2>")