
from django.shortcuts import render, HttpResponse

import requests
import json

def index(request):
	return HttpResponse('NPC Calculator')

    