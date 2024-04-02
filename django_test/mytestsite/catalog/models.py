from django.db import models
from django.urls import reverse

# Create your models here.
# class MyModelName(models.Model):
#     """A typical class defining a model, derived from the Model class."""

#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
#     ...

#     # Metadata
#     class Meta:
#         ordering = ['-my_field_name']

#     # Methods
#     def get_absolute_url(self):
#             """Returns the url to access a particular instance of MyModelName."""
#             return reverse('model-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.field_name
class Coffee(models.Model):
    name  = models.CharField(max_length=60, help_text='輸入姓名')
    price = models.IntegerField(help_text='金額')

    # 定义字段数组
    model_fields = ['name', 'price']
    class Meta:
        ordering = ['name', '-price']
    def __str__(self): # 可以控制列表顯示文字
        """String for representing the MyModelName object (in Admin site etc.)."""
        _str = str(self.name)+ ', ' + str(self.price)
        # return self.name
        return _str
    # Methods
    def get_absolute_url(self):
            """Returns the url to access a particular instance of MyModelName."""
            return reverse('test_menu')
    def get_absolute_url2(self, key):
            """Returns the url to access a particular instance of MyModelName."""
            return reverse('test_menu2',args=[key])