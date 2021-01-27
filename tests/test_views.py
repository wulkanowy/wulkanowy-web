from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.csrf_token = Client(enforce_csrf_checks=True)
        self.list_url = reverse('home')
        self.detail_url = reverse('content')

    def test_views(self):
        #DEFAULT_VIEW
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/index.html')

        #CONTENT_VIEW
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 302)

        #ACCOUNT_MANAGER
        response = self.client.get(reverse('account_manager'))
        
        self.assertEquals(response.status_code, 302)

        #API
        data = {
            "loginName": "jan@fakelog.cf",
            "Password": "jan123",
            "Symbol": "powiatwulkanowy",
            "diaryUrl": "http://cufs.fakelog.cf/"
        }

        response = self.client.post(reverse('login'), content_type='application/xml', data=json.dumps(data))
        cookies_data = response.json()
        
        self.assertEquals(response.status_code, 200)

        students = cookies_data['data']['register_r']['data']
        #JAN
        jan_data = students[0]
        cookies_data['data']['register_r']['data'] = [jan_data]

        response = self.client.post(reverse('grades'), content_type='application/xml', data=json.dumps(cookies_data))
        self.assertEquals(response.status_code, 200)
        print(response.content)
        
        #JOANNA
        joanna_data = students[3]
        cookies_data['data']['register_r']['data'] = [joanna_data]

        response = self.client.post(reverse('grades'), content_type='application/xml', data=json.dumps(cookies_data))
        self.assertEquals(response.status_code, 200)
        print(response.content)