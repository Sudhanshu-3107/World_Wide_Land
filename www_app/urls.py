from django.urls import path
from.import views, agent_views, owner_views

urlpatterns =[
    path("",views.home,name='home'),
    path('owner_register/', owner_views.owner_register, name='owner_register'),
    path('owner_login/', owner_views.owner_login, name='owner_login'),
    path('upload_property/', owner_views.upload_property, name='upload_property'),
    path('agent_register/', agent_views.agent_register, name='agent_register'),
    path('agent_login/', agent_views.agent_login, name='agent_login'),
    path('agent_home/', agent_views.agent_home, name='agent_home'),
    path('member_login/', views.member_login, name='member_login'),
    path('member_home/', views.member_home, name='member_home'),
    path('agents/', views.agents, name='agents'),
    path('success_page/', views.success_page, name="success_page"),
    path('property_query/', views.property_query, name="property_query"),
    path('inquiry/<int:id>', views.inquiry, name="inquiry"),
    path('seeker_login/', views.seeker_login, name="seeker_login"),
    path('seeker_reg/', views.seeker_reg, name="seeker_reg"),
    path('properties/', views.properties, name="properties"),
    path('feedback/', views.feedback, name="feedback"),
    path('logout/', views.logout, name='logout'),
]