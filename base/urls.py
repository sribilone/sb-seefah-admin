from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

    
    path("", views.home, name="home"),
    path("superadmin/", views.adminHome, name="admin-home"), 
    
    path("server/", views.serverConf, name="server-conf"),
    path("datawarehouse/", views.dataWarehouse, name="data-warehouse"),
    path("usermanagement/", views.userManagemant, name="user-management"),
    path("userregistration/", views.userRegistration, name="user-registration"),
    path("userdelete/", views.userDelete, name="user-delete"),
    path("useredit/", views.userEdit, name="user-edit"),
    
    # path("register/", views.registerUser, name="register"),
    # path("room/<str:pk>/", views.room, name="room"),
    # path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    # path("delete-room/<str:pk>/", views.deleteRoom, name="delete-room"),
]
