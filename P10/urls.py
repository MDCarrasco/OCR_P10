"""P10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt import views as jwt_views
from P10.SoftDesk import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')
## generates:
# /projects/
# /projects/{pk}/

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'issues', views.IssueViewSet, basename='issues')
## generates:
# /projects/{project_pk}/issues/
# /projects/{project_pk}/issues/{pk}/

issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', views.CommentViewSet, basename='comments')
## generates:
# /projects/{project_pk}/issues/{issue_pk}/comments/
# /projects/{project_pk}/issues/{issue_pk}/comments/{pk}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path(r'', include(router.urls)),
    path(r'', include(project_router.urls)),
    path(r'', include(issue_router.urls)),
]
