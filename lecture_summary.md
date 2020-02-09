### db정보로 models.py생성

-   python manage.py inspectdb > fastadmin/models.py
-   settings.py의 db정보를 기반으로 연결하여 fastadmin app에 models.py 생성

```console
python manage.py inspectdb > fastadmin/models.py
python manage.py makemigrations
python manage.py migrate
```

### django-admin-rangefilter 설치

-   pip install django-admin-rangefilter
-   참조 사이트 - https://pypi.org/project/django-admin-rangefilter/

### django package

-   django-grappelli
-   django-suit
ªª
### django-grappelli : ui plugin

-   설치
    -   pipenv install django-grappelli
-   설정

```python


```

-   참조사이트 : https://django-grappelli.readthedocs.io/en/latest/quickstart.html#installation

### Pillow 
- 이미지 처리할때 사용하는 라이브러리
- pipenv install Pillow
```python
# settings.py
# MEDIA - 관련설정
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

---

# urls.py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    ...
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
                          
---

# models.py
class Cat(models.Model):
    name = models.CharField(max_length=30, verbose_name="이름")
    age = models.IntegerField()
    photo = models.ImageField(null=True, blank=True, upload_to='cats_photo/')

    def __str__(self):
        return 'Name: %s' % self.name

# admin.py
class DisplayCat(admin.ModelAdmin):
	fields = ('name', 'age', 'photo')
	list_display = ('name', 'age', 'photo', 'get_image')

	@staticmethod
	def get_image(obj):
		return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
			url=obj.photo.url, width=obj.photo.width, height=obj.photo.height)
		)

admin.site.register(Cat, DisplayCat)
```

### env-notice
- pipenv install django-admin-env-notice 
- front 단에  서버별로 식별하기위해 사용
- 참조사이트 - https://github.com/dizballanze/django-admin-env-notice

### django-admin-honeypot - 보안관련
- pipenv install django-admin-honeypot  
- 참조사이트 - https://github.com/dmpayton/django-admin-honeypot
https://django-admin-honeypot.readthedocs.io/en/latest/#