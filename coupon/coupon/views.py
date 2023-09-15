from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control


from .models import *

def index(request):
	offerobj=Offer.objects.all()
	catobj=NewCategory.objects.all()
	return render(request,'index.html',{'offerobj':offerobj,'catobj':catobj})
def cpadmin(request):
	
	if request.method=='POST':
		un=request.POST['username']
		pwd=request.POST['password']

		user=authenticate(username=un,password=pwd)
		if user:
			login(request, user)
			return redirect('/Dashboard/')
		else:
			msg='invalid username or password'
	return render(request,'login.html')


def brands(request):
	return render(request,'brands.html')

def dashboard(request):
	offerobj=Offer.objects.all()
	catobj=NewCategory.objects.all()
	catcontentobj=NewCategoryContent.objects.all()
	print(catcontentobj)
	return render(request,'dashboard.html',{'offerobj':offerobj,'catobj':catobj,'catcontentobj':catcontentobj})

def addCategory(request):
	if request.method=='POST':
		Categoryname=request.POST['ac_categoryname']
		Translatedcategoryname=request.POST['ac_transcatname']
		Parentpath=request.POST['ac_parentpath']
		Status=request.POST['ac_status']
		Description=request.POST['ac_description']
		Translatedesc=request.POST['ac_transdesc']
		Country=request.POST['ac_country']
		Pagetitle=request.POST['ac_pagetitle']
		Metadesc=request.POST['ac_metadesc']
		Metakeyword=request.POST['ac_metakeyword']
		Mpu=request.POST['ac_mpu']
		Cssclass=request.POST['ac_cssclass']
		Categoryicon=request.FILES['ac_categoryicon']
		categoryobj=NewCategory(categoryName=Categoryname,translatedCategoryName=Translatedcategoryname,parentPath=Parentpath,
			status=Status,description=Description,translatedDescription=Translatedesc,country=Country,
			pageTitle=Pagetitle,metaDescription=Metadesc,metaKeyword=Metakeyword,mpu=Mpu,cssClass=Cssclass,
			categoryIcon=Categoryicon)
		categoryobj.save()
		print("categoryAdded!")
	return redirect('/cp-admin/')

def EditCategory(request,id):
	cobj=NewCategory.objects.filter(id=id)
	a=[]
	for i in cobj:
		a.append(i.categoryIcon)
	print(a)
	if request.method=='POST':
		Categoryname=request.POST['ac_categoryname']
		Translatedcategoryname=request.POST['ac_transcatname']
		Parentpath=request.POST['ac_parentpath']
		Status=request.POST['ac_status']
		Description=request.POST['ac_description']
		Translatedesc=request.POST['ac_transdesc']
		Country=request.POST['ac_country']
		Pagetitle=request.POST['ac_pagetitle']
		Metadesc=request.POST['ac_metadesc']
		Metakeyword=request.POST['ac_metakeyword']
		Mpu=request.POST['ac_mpu']
		Cssclass=request.POST['ac_cssclass']
		
		categoryobj=NewCategory.objects.filter(id=id)
		categoryobj.update(categoryName=Categoryname,translatedCategoryName=Translatedcategoryname,parentPath=Parentpath,
			status=Status,description=Description,translatedDescription=Translatedesc,country=Country,
			pageTitle=Pagetitle,metaDescription=Metadesc,metaKeyword=Metakeyword,mpu=Mpu,cssClass=Cssclass,
			)
		return redirect('/Dashboard/')
	return render(request,'edit_category.html',{'cobj':cobj})
	

def addCategoryContent(request):
	offerobj=Offer.objects.all()
	catobj=NewCategory.objects.all()
	catcontentobj=NewCategoryContent.objects.all()
	if request.method=='POST':
		Merchant=request.POST['ncc_merchant']
		Merchantarticle=request.POST['ncc_merchantarticle']
		Categoriescurrent=request.POST['ncc_categories']
		Categoriesadd=request.POST['ncc_categoriesadd']
		Status=request.POST['ncc_status']
		Offertitle=request.POST['ncc_offertitle']
		Pagemetadesc=request.POST['ncc_pagedesc']
		Content=request.POST['ncc_content']
		print("done")
		categorycontentobj=NewCategoryContent(merchant=Merchant,merchantArticleUrl='Merchantarticle',
			categoriesCurrent=Categoriescurrent,categoriesAdd=Categoriesadd,status=Status,offerTitle=Offertitle,
			pageMetaDesc=Pagemetadesc,content=Content)
		categorycontentobj.save()
		print("done")
	return render(request,'dashboard.html')


def editcategorycontent(request,id):
	data=NewCategoryContent.objects.filter(id=id)
	if request.method=='POST':
		Merchant=request.POST['ncc_merchant']
		Merchantarticle=request.POST['ncc_merchantarticle']
		Categoriescurrent=request.POST['ncc_categories']
		Categoriesadd=request.POST['ncc_categoriesadd']
		Status=request.POST['ncc_status']
		Offertitle=request.POST['ncc_offertitle']
		Pagemetadesc=request.POST['ncc_pagedesc']
		Content=request.POST['ncc_content']
		print("done")
		obj=NewCategoryContent.objects.filter(id=id)
		print(obj)
		print('done2')
		obj.update(merchant=Merchant,merchantArticleUrl=Merchantarticle,
		categoriesCurrent=Categoriescurrent,categoriesAdd=Categoriesadd,status=Status,offerTitle=Offertitle,
		pageMetaDesc=Pagemetadesc,content=Content)
		print('done3')
		return redirect('/Dashboard/')
	else:
		print('not updated')
	return render(request,'edit_category_content.html',{'data':data})

def addOffer(request):
	print('offer added succesfully!')
	catobj=NewCategory.objects.all()
	print(catobj)
	for i in catobj:
		print("print not work")
		print(i.categoryName)

	print(catobj)
	if request.method=='POST':
		Offerreference=request.POST['ao_offerreference']
		Offerimage=request.FILES['ao_offerimage']
		Merchant=request.POST['ao_merchant']
		Offertype=request.POST['ao_offertype']
		Offersubtype=request.POST['ao_offersubtype']
		Vouchercode=request.POST['ao_vouchercode']
		Categoriescurrent=request.POST['ao_categoriescurrent']
		Catid=request.POST['ao_categoriesadd']
		Status=request.POST['ao_status']
		MerchantofferURl=request.POST['ao_merchantofferurl']
		OfferclickURL=request.POST['ao_offerclickurl']
		Offerheadline=request.POST['ao_offerheadline']
		Offertitle=request.POST['ao_offertitle']
		Idealfeedsoffertitle=request.POST['ao_idealfeedsoffertitle']
		Rpoffertitle=request.POST['ao_rpoffertitle']
		Discounttype=request.POST['ao_discounttype']
		Discountvalue=request.POST['ao_discountvalue']
		Description=request.POST['ao_description']
		Idealfeedsdesc=request.POST['ao_idealfeedsdesc']
		RPdesc=request.POST['ao_rpdesc']
		Termcondition=request.POST['ao_termcondition']
		Mincartvalue=request.POST['ao_mincartvalue']
		Brandrestriction=request.POST['ao_brandrestriction']
		Userrestriction=request.POST['ao_userrestriction']
		Startdate=request.POST['ao_startdate']
		Enddate=request.POST['ao_enddate']
		Displayorderno=request.POST['ao_display']
		Saleevent=request.POST['ao_saleevent']
		Blazetext=request.POST['ao_blazetext']
		Createdby=request.POST['ao_createdby']
		Owneragency=request.POST['ao_owneragency']
		cobj=NewCategory.objects.get(id=Catid)
		offerobj=Offer(offerReferance=Offerreference,offerImage=Offerimage,merchant=Merchant,offerType=Offertype,
			offerSubType=Offersubtype,voucherCode=Vouchercode,categoriesCurrent=Categoriescurrent,categoriesAdd=cobj,
			status=Status,merchantOfferUrl=MerchantofferURl,offerClickUrl=OfferclickURL,offerHeadLine=Offerheadline,
			offerTitle=Offertitle,idealFeedsofferTitle=Idealfeedsoffertitle,RPofferTitle=Rpoffertitle,discountType=Discounttype,
			discountValue=Discountvalue,description=Description,idealfeedsDesc=Idealfeedsdesc,RPDesc=RPdesc,
			termCondition=Termcondition,minCartValue=Mincartvalue,BrandRestriction=Brandrestriction,userrestriction=Userrestriction,
			startDate=Startdate,endDate=Enddate,displayOrderNo=Displayorderno,saleEvent=Saleevent,blazeText=Blazetext,
			createdBy=Createdby,ownerAgency=Owneragency)
		offerobj.save()
		print('offer added succesfully!')
	return render(request,'dashboard.html',{'catobj':catobj})	
		
def offerpage(request):
	catobj=NewCategory.objects.all()
	
	return render(request,'addoffer.html',{'catobj':catobj})
def showpage(request,id):
	offerobj=Offer.objects.filter(id=id)
	catobj=NewCategory.objects.all()
	return render(request,'offerpage.html',{'offerobj':offerobj,'catobj':catobj})

def searchitem(request):
	item=[]
	usobj=Offer.objects.all()
	catobj=NewCategory.objects.all()
	if request.method=='POST':
		key=request.POST['keyword']
		for i in usobj:
			if key.lower() in i.offerTitle or key.capitalize() in i.offerTitle:
				item.append(i)
			elif key.lower() in i.description or key.capitalize() in i.description:
				item.append(i)
	return render(request,'search.html',{'item':item,'catobj':catobj})




def userlogin(request):
	return render(request,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def logout_call(request):
	logout(request)
	request.session['failed'] = 0
	request.session.set_expiry(1)
	return redirect('/cp-admin/')