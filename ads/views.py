from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from ads.models import Category, Ad
# Create your views here.

def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})
