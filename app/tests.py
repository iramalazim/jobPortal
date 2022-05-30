from django.urls.base import resolve
from django.http import request, response
from django.test import TestCase
from .models import *
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *
from .views import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User,auth
import datetime

from django.test import TestCase, Client
from django.urls import reverse
import json



class TestView(TestCase):

    def test_index(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func, index)
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_recruiter_home(self):
        url=reverse('recruiter_home')
        self.assertEquals(resolve(url).func, recruiter_home)

    def test_user_login(self):
        url=reverse('user_login')
        self.assertEquals(resolve(url).func, user_login)

    def test_add_job(self):
        url=reverse('add_job')
        self.assertEquals(resolve(url).func, add_job)

    def test_admin_login(self):
        url=reverse('admin_login')
        self.assertEquals(resolve(url).func, admin_login)

    def test_user_home(self):
        url=reverse('user_home')
        self.assertEquals(resolve(url).func, user_home)

    def test_template_user_signup(self):
        response=self.client.get(reverse('user_signup'))
        self.assertTemplateUsed(response, 'user_signup.html')

    def test_template_recruiter_login(self):
        response=self.client.get(reverse('recruiter_login'))
        self.assertTemplateUsed(response, 'recruiter_login.html')



class TestURL(TestCase):

    def test_admin_home(self):
        client=Client()
        response = client.get(reverse('admin_home'))
        self.assertEquals(response.status_code,302)

    def test_Logout(self):
        client=Client()
        response = client.get(reverse('Logout'))
        self.assertEquals(response.status_code,302)

    def test_recruiter_login(self):
        client=Client()
        response = client.get(reverse('recruiter_login'))
        self.assertEquals(response.status_code,200)

    def test_user_signup(self):
        client=Client()
        response = client.get(reverse('user_signup'))
        self.assertEquals(response.status_code,200)

    def test_view_users(self):
        client=Client()
        response = client.get(reverse('view_users'))
        self.assertEquals(response.status_code,302)

    def test_recruiter_pending(self):
        client=Client()
        response = client.get(reverse('recruiter_pending'))
        self.assertEquals(response.status_code,302)

    def test_job_list(self):
        client=Client()
        response = client.get(reverse('job_list'))
        self.assertEquals(response.status_code,302)

    def test_recruiter_all(self):
        client=Client()
        response = client.get(reverse('recruiter_all'))
        self.assertEquals(response.status_code,302)
