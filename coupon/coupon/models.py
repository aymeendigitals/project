from django.db import models
from django.contrib.auth.models import User

class NewCategoryContent(models.Model):
	merchant=models.CharField(max_length=100)
	merchantArticleUrl=models.CharField(max_length=100)
	categoriesCurrent=models.CharField(max_length=100)
	categoriesAdd=models.CharField(max_length=100)
	status=models.CharField(max_length=100)
	offerTitle=models.CharField(max_length=100)
	pageMetaDesc=models.CharField(max_length=300)
	content=models.CharField(max_length=300)
	createdDate=models.DateTimeField(auto_now=True)


class NewCategory(models.Model):
	categoryName=models.CharField(max_length=100)
	translatedCategoryName=models.CharField(max_length=100)
	parentPath=models.CharField(max_length=100)
	status=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	translatedDescription=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	pageTitle=models.CharField(max_length=100)
	metaDescription=models.CharField(max_length=100)
	metaKeyword=models.CharField(max_length=100)
	mpu=models.CharField(max_length=100)
	cssClass=models.CharField(max_length=100)
	categoryIcon=models.ImageField(upload_to="product_image",blank=True)
	createdDate=models.DateTimeField(auto_now=True)

class Offer(models.Model):
	offerReferance=models.CharField(max_length=100)
	offerImage=models.ImageField(upload_to="product_image",blank=True)
	merchant=models.CharField(max_length=100)
	offerType=models.CharField(max_length=100)
	offerSubType=models.CharField(max_length=100)
	voucherCode=models.CharField(max_length=100)
	categoriesCurrent=models.CharField(max_length=100)
	categoriesAdd=models.ForeignKey(NewCategory, on_delete=models.CASCADE)
	status=models.CharField(max_length=100)
	merchantOfferUrl=models.CharField(max_length=100)
	offerClickUrl=models.CharField(max_length=100)
	offerHeadLine=models.CharField(max_length=100)
	offerTitle=models.CharField(max_length=100)
	idealFeedsofferTitle=models.CharField(max_length=100)
	RPofferTitle=models.CharField(max_length=100)
	discountType=models.CharField(max_length=100)
	discountValue=models.CharField(max_length=100)
	description=models.CharField(max_length=300)
	idealfeedsDesc=models.CharField(max_length=300)
	RPDesc=models.CharField(max_length=300)
	termCondition=models.CharField(max_length=300)
	minCartValue=models.CharField(max_length=100)
	BrandRestriction=models.CharField(max_length=100)
	userrestriction=models.CharField(max_length=100)
	startDate=models.DateTimeField()
	endDate=models.DateTimeField()
	displayOrderNo=models.CharField(max_length=100)
	saleEvent=models.CharField(max_length=100)
	blazeText=models.CharField(max_length=100)
	dateCrated=models.DateTimeField(auto_now=True)
	createdBy=models.CharField(max_length=100)
	ownerAgency=models.CharField(max_length=100)

