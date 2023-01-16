from django.contrib import admin
from django.urls import path
from food import views


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('fd', views.fd),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  

