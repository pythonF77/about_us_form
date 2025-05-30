from django.urls import path, include
from .views import index_page,get_max_salary
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', index_page, name='index.page'),
    path('salary//<int:top>', get_max_salary, name='employee-list'),
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)