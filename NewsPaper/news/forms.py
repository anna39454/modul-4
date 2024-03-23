from django import forms
from .models import Post
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       #fields = '__all__'
#собственный класс формы, наследуя ModelForm.
# Данный стандартный класс Django позволяет быстро и удобно создавать формы на основе моделей.
#Саму модель мы должны прописать в Meta классе в поле model= Product.
#В fields мы указали особенное значение ’__all__’,
# которое означает, что Django сам должен пойти в модель и взять все поля, кроме первичного ключа
# могли сами перечислить все поля
       fields = [
           'tile',
           'text',
           'categoryTape',
           'author',
       ]
