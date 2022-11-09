from rest_framework.response import Response
import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from joblib import dump, load


class AutoPrediction(APIView):
    def post(self, request):
        data = request.data
        horsepower = data['Horse Power']
        enginesize = data['Engine Size']
        curbweight = data['Curb Weight']
        carwidth = data['Car Width']
        dtree_modelll = ApiConfig.model
        auto_predict = dtree_modelll.predict([[horsepower, enginesize, curbweight, carwidth]])[0]
        auto_predict = np.round(auto_predict, 1)
        response_d = {'Auto Prediction': auto_predict}
        return Response(response_d, status=200)
