from rest_framework import permissions
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.views import APIView

import requests


import requests

class UserActivationView(APIView):

    def get(self, request, uid, token):
        url = "http://127.0.0.1:8000/api/users/activation/"
        data = {'uid': uid, 'token': token}
        response = requests.post(url, data=data)
        return Response(response.text)