from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from app.serializers import UserSerializer, UserStatusSerializer


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserStatusAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = UserStatusSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
