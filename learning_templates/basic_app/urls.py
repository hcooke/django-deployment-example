from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
# 'basic_app' needs to match the tag in relative_url_template.html
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
