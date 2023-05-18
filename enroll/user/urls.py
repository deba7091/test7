from django.urls import path
from .views import  UserView
from .views import * 


urlpatterns = [
	path('api/user/', UserView.as_view(), name='user'),
    path('api/user/<int:id>',UserView.as_view(),name='user'),
    path('api/skills/',SkillView.as_view(),name='SkillsView'),
    path('api/skills/<int:id>',SkillView.as_view(),name='SkillsView'),
    path('api/user/skills/<int:id>',Combinedata.as_view(),name='UserskillView'),
    path('api/services/',listing.as_view(),name='SkillsView'),
    path('api/services/<int:id>',listing.as_view(),name='SkillsView'),
] 