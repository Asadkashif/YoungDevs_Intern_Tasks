from django.contrib import admin
from django.urls import include, path  # Add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('intern/', include('intern.urls')),  # Add this line
]