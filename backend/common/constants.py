# constants.py

from django.conf import settings
from rest_framework import serializers, generics, permissions, status
from rest_framework.test import APIClient
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.exceptions import PermissionDenied
from django.urls import reverse, resolve
from django.test import TestCase, RequestFactory
from django.contrib import admin
from datetime import timedelta


from django.contrib.auth import get_user_model

User = get_user_model()
