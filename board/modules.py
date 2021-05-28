from django.core import paginator
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post, Comment, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user_model
