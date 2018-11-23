import os
import json
import traceback
import logging
import zipfile 
import csv 
import copy 
import tempfile
import shutil
import zipfile 
import subprocess 
import string
import platform 
from datetime import datetime 
import threading
from pytz import timezone 
from dateutil import parser as dateparser 
from itertools import islice
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages


import pandas as pd 

# from .forms.annotation_form import AnnotationForm
# from .forms.labels_form import LabelForm
# from .models import AnnotationModel, LabelModel



def clip_app_view(request):
    return render(request, 
                  "pages/clip_app.html", 
                {
                  }) 