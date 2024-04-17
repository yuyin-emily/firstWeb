from django.db import models

from django.utils.text import slugify #name 網址縮寫？ 回復原址用
from django.urls import reverse

# 定義分類名稱欄位
class Category(models.Model):
    title = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.title
    
# 定義標籤名稱欄位
class Tag(models.Model):
    title = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.title

# 定義商品資料欄位
class Flower(models.Model):
    title = models.CharField(max_length=255, default="") #單行文字方塊
    description = models.TextField(default="") #多行文字方塊
    slug = models.SlugField(blank=True, default="") #短網址說明
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(default="",blank=True,upload_to="images")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs): #自動帶入title
        self.slug = slugify(self.title)
        super(Flower, self).save()
        
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.slug)])