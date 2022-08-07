from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import status
from django.http import Http404

from api.models import User, Record, Auth
from api.serializer import UserSerializer, RecordSerializer, AuthSerializer

# Create your views here.
import cloudinary.uploader


class loginView(APIView):
    def post(self, request, format=None):
        try:
            auth = Auth.objects.get(username=request.data.get('username'))
            serializer = AuthSerializer(auth, data=request.data)
            if serializer.is_valid():
                print(serializer.data.get('password'))
                print(request.data.get('password'))
                if(serializer.data.get('password') == request.data.get('password')):
                    return Response({"status": status.HTTP_200_OK, "data": "Login success"}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": status.HTTP_401_UNAUTHORIZED, "data": "Invalid password"}, status=status.HTTP_200_OK)
            else:
                return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "data": serializer._errors}, status=status.HTTP_200_OK)
        except:
            return Response({"status": status.HTTP_401_UNAUTHORIZED, "data": "Invalid email"}, status=status.HTTP_200_OK)


class UserView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def get(self, request, userID=-1, format=None):
        try:
            if(userID != -1):
                user = User.objects.get(userID=userID)
                serializer = UserSerializer(user)
                return Response({"status": status.HTTP_200_OK, "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "data": "UserID required"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": status.HTTP_404_NOT_FOUND, "data": "Invalid userID"}, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        user_data = request.data
        res = cloudinary.uploader.upload(
            user_data['image'], folder="JHON CLINIC/")
        user_data.image = res.get('secure_url')
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(userID=pk)
            serializer = UserSerializer(user, data=request.data)
            print(request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": status.HTTP_200_OK, "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"status": status.HTTP_404_NOT_FOUND, "data": serializer._errors}, status=status.HTTP_200_OK)
        except:
            return Response({"status": status.HTTP_404_NOT_FOUND, "data": "Invalid userID"}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(userID=pk)
            user.delete()
            return Response({"status": status.HTTP_200_OK, "data": "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": status.HTTP_404_NOT_FOUND, "data": "Invalid userID"}, status=status.HTTP_200_OK)


class recordView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def get(self, request, userID=-1, format=None):
        if(userID != -1):
            records = Record.objects.filter(userID=userID).order_by('-date')
        else:
            records = Record.objects.all().order_by('-date')
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        record_data = request.data
        serializer = RecordSerializer(data=record_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            record = Record.objects.get(recordID=pk)
            serializer = RecordSerializer(record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise Http404

    def delete(self, request, pk, format=None):
        try:
            record = Record.objects.get(recordID=pk)
            record.delete()
            return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)
        except:
            raise Http404
