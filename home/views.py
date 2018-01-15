from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from blockchain import Block
from blockchain import create_genesis_block, next_block

wishlist1 = []
ledger = [create_genesis_block()]
#json_list = []


def postAd(request):
	if request.method == 'GET':
		return render(request, 'post.html')
	elif request.method == 'POST':
		post = request.POST
		file = request.FILES
		ad = Advertisment()

		ad.user = request.user
		ad.title = post.get('title')
		ad.category = post.get('category')
		ad.description = post.get('description')
		ad.name = post.get('name')
		ad.price = post.get('price')
		ad.mobileNumber = post.get('number')
		ad.address = post.get('address')
		ad.image = request.FILES.get('image')

		ad.save()

		return redirect('/home')



def search(request):
	query = request.GET.get('search', '')
	if query:
		qset = (
				Q(title__icontains=query) |
				Q(category__icontains=query) 

			)
		result = Advertisment.objects.filter(qset).distinct()
	else:
		result = Advertisment.objects.all()

	return render(request, 'home.html', {'ad' : result})	


def wishlist(request, ad_id):
	
	ad = Advertisment.objects.get(pk=ad_id)
	if ad:
		wishlist1.append(ad)
	else :
		pass

	return render(request, 'wishlist.html', {'wishlist' : wishlist1} )




def myWish(request):
	return render(request, 'wishlist.html', {'wishlist' : wishlist1})


def remove(request, rm_id):
	ad = Advertisment.objects.get(pk=rm_id)	
	try:
		wishlist1.remove(ad)
	except:
		pass
	return render(request, 'wishlist.html', {'wishlist' : wishlist1})	



def myad(request):
	u = request.user
	ad = Advertisment.objects.filter(user=u)

	return render(request, 'myad.html', {'myad' : ad})	


def deleteAd(request, dl_id):
	ad = Advertisment.objects.get(pk=dl_id)
	ad.delete()
	return redirect('/home')


def buyRequest(request, user_id, pr_id):
	response = {}
	buyer1 = user_id
	print "heeeeeee"
	# print buyer
	ad = Advertisment.objects.get(pk=pr_id)
	seller = ad.user.username
	print seller
	response["buyer"] = buyer1
	response["seller"]=seller
	response["product_id"] = pr_id
	#return redirect('/home')
	n = Notification()
	n.not_user = ad.user
	# n.buy_er = user_id
	hola = "%s-want-to-buy-%s" % (buyer1, ad.title)
	n.notification = hola
	# n.product = pr_id
	n.save()
	return JsonResponse(response)


def nbc(request, seller_id, notification):
	# from, to, product id, product title
	data={}
	noti = notification.split('-')
	buyer_id = noti[0]
	p_id = noti[-1]
	data["from"] = seller_id
	data["to"] = buyer_id
	data["product"] = p_id
	last_ledger = ledger[-1]
	new_block = next_block(last_ledger)
	new_block.data = data
	new_block.hash = new_block.hash_block()

	not1 = Notification.objects.filter(notification=notification)
	not1.delete()
	log = BlockChain()
	log.log = new_block.data
	log.save()

	# ledger.append(new_block)
	# new_ledger = []
	# for x in ledger:
	# 	new_ledger.append(x.data)
	# json_list = new_ledger	
	x = JsonResponse(log.log, safe=False)
	return redirect('/home')


def notYet(request, no_id):
	notif = Notification.objects.filter(pk=no_id)
	notif.delete()
	return redirect('/home')


def jsonList(request):
	json_list = BlockChain.objects.all()
	return render(request, 'blockchain.html', { 'list' : json_list })
