from django.conf.urls import url

from app import views, epic_battle_math

urlpatterns = [
	url('^$', views.index, name='index'),
    url('^epic_battle/', epic_battle_math.fortress_battle, name='epic_battle'),

	]
