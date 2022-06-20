from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.DepartmentView.as_view(), name='departments'),
    path('departments/<int:pk>/sections/', views.DepartmentSectionView.as_view()),
    path('departments/<int:pk>/sections/<int:id>/employee/', views.DepartmentSectionEmployeeView.as_view()),

]
