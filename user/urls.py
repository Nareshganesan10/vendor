from django.urls import path
from user import views

urlpatterns = [
    # /api/vendors GET and POST
    path('vendors/', view=views.index, name="index"),

    # /api/vendors/{vendor_id}/ GET
    path('vendors/<int:vendor_id>', view=views.signup, name="signup"),
    
    # /api/vendors/{vendor_id}/ PUT
    path('vendors/<int:vendor_id>', view=views.signup, name="signup"),
   
    # /api/vendors/{vendor_id}/ DELETE 
    path('vendors/<int:vendor_id>', view=views.signup, name="signup"),
]