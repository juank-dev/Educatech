from django.urls import include, path

from .views import classroom, students, teachers


urlpatterns = [
    path('', classroom.home, name='home'),
    path('students/', students.ProductListView.as_view(), name='students'),
    path('teachers/', teachers.homepage, name='teachers'),
    path('students/search/', students.ProductSearchListView.as_view(), name='search'),
    path('students/<slug:slug>/', students.ProductDetailView.as_view(), name='product'),
]

