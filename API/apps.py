import os
import joblib
from joblib import dump, load
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeRegressor.joblib")
    model = joblib.load(MODEL_FILE)
