from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here.
