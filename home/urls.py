from django.conf.urls import url
from views import *


app_name = 'home'

urlpatterns = [
	url(r'^ad/$', postAd, name='postAd'),
	url(r'^search/$', search, name='search'),
	url(r'^wishlist/(?P<ad_id>[0-9]+)/$', wishlist, name='wishlist'),
	url(r'^remove/(?P<rm_id>[0-9]+)/$', remove, name='remove'),
	url(r'^delete/(?P<dl_id>[0-9]+)/$', deleteAd, name='deleteAd'),
	url(r'^myWish/$', myWish, name='myWish'),
	url(r'^myad/$', myad, name='myad'),
	url(r'^buyRequest/(?P<user_id>[-\w]+)/(?P<pr_id>[0-9]+)/$', buyRequest, name='buyRequest'),
	# url(r'^nbc/(?P<seller_id>[-\w]+)/(?P<buyer_id>[-\w]+)/(?P<p_id>[0-9]+)/$', nbc, name='nbc'),
	url(r'^nbc/(?P<seller_id>[-\w]+)/(?P<notification>[-\w]+)/$', nbc, name='nbc'),
	url(r'^notYet/(?P<no_id>[0-9]+)/$', notYet, name='notYet'),
	url(r'^jsonList/$', jsonList, name='jsonList'),

	
]