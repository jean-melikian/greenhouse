from base64 import b64decode

from django.contrib.auth import authenticate
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, serializers
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from greenhouseApp.models import SensorsEntry
from greenhouseApp.serializers import SensorsEntrySerializer
from .auth import get_or_create_token, get_basic_auth, check_request_token


def model_list(request, model_type, serializer_type):
	is_token_valid = check_request_token(request)

	print(request.method, request.body)

	if not issubclass(model_type, models.Model) or not issubclass(serializer_type, serializers.ModelSerializer):
		return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	if request.method == 'GET':
		obj = model_type.objects.all()

		serializer = serializer_type(obj, many=True)
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		if not is_token_valid:
			return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		serializer = serializer_type(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def model_details(request, pk, model_type, serializer_type):
	is_token_valid = check_request_token(request)

	if not issubclass(model_type, models.Model) or not issubclass(serializer_type, serializers.ModelSerializer):
		return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	try:
		obj = model_type.objects.get(pk=pk)
	except model_type.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = serializer_type(obj)
		return JsonResponse(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		if not is_token_valid:
			return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		serializer = serializer_type(obj, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_200_OK)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		if not is_token_valid:
			return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

		obj.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def sensorsEntry_list(request):
	return model_list(request, SensorsEntry, SensorsEntrySerializer)


@csrf_exempt
def sensorsEntry_details(request, pk):
	return model_details(request, pk, SensorsEntry, SensorsEntrySerializer)


@csrf_exempt
def login(request):
	basic = get_basic_auth(request)
	if basic is not None:
		log = b64decode(bytes(basic, 'ascii')).decode('ascii').split(':')
		user = authenticate(username=log[0], password=log[1])
		if user is not None:
			token = get_or_create_token(user)
			return JsonResponse(data={'token': token.hash})
	return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
