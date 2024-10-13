from django.contrib import admin
from django.urls import path
from authentication.views import signup, logout_view, login_view, detail_section, UpdateDetails, DeleteAccount
from home.views import home, CreatePost,feedSection
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name= "signup"),
    path('user/<str:username>', home, name="home" ),
    path("create/", CreatePost, name="create"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name= "login"),
    path("details/", detail_section, name="details"),
    path("updatedetails/", UpdateDetails, name= "updatedetails" ),
    path("user/delete/", DeleteAccount, name = "delete"),
    path("feed/", feedSection, name="feed")
]
