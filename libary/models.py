from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название книги')
    description = models.TextField(blank=True, null = True, verbose_name='Описание книги')
    count_pages = models.PositiveIntegerField(null=False, verbose_name='Количество страниц')
    price = models.FloatField(verbose_name='Цена')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата издания книги')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата написания книги')
    update_date = models.DateField(auto_now_add=True, verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null = True, blank=True, verbose_name='Фотография обложки')
    exists = models.BooleanField(default=True, verbose_name='Издана?')
    publisher = models.ForeignKey('Publishing_house', on_delete=models.CASCADE, null=True, verbose_name='Издательство')
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null = True, verbose_name='Автор книги')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name', '-price']

class Publishing_house(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название издательства')
    agent_name = models.CharField(max_length=255, verbose_name='Фамилия представителя')
    agent_secondname = models.CharField(max_length=255, verbose_name='Имя представителя')
    agent_surname = models.CharField(max_length=255, null = True, blank=True, verbose_name='Отчество представителя')
    telephone = models.CharField(max_length=255, verbose_name='Телефон') 

    def __str__(self):
        return self.title + " " + self.agent_name + " | " + self.telephone
    
    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        permissions = [
            ('change_only_telephone', 'Можно изменять только телефон')
        ]

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    books = models.ManyToManyField(Books)

    def __str__(self):
        return  self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class Pasport_book(models.Model):
    article = models.IntegerField(verbose_name='Артикул')
    features = models.CharField(max_length=255, verbose_name='Дополнения к книге')
    book = models.OneToOneField(Books, on_delete=models.PROTECT, primary_key=True, verbose_name='Книга')

    def __str__(self):
        return str(self.article) + '|' + str(self.book)
    
    class Meta:
        verbose_name = 'Паспорт книги'
        verbose_name_plural = 'Паспорта книг'

class Author(models.Model):
    name_author = models.CharField(verbose_name='Имя автора', max_length=255)
    second_name = models.CharField(verbose_name='Фамилия автора', max_length=255)
    author_surname = models.CharField(verbose_name='Отчество автора', max_length=255)

    def __str__(self):
        return self.name_author + "|" + " " + self.second_name
    
    class Meta:
        verbose_name = 'Имя автора'
        verbose_name_plural = 'Имена авторов'
