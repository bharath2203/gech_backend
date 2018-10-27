from django.contrib import admin
from .models import Student, Notification, Department, Faculty
from django.core.files.images import get_image_dimensions
from django import forms
from image_cropping import ImageCroppingMixin

class myForm(forms.ModelForm):
   class Meta:
       model = Student
       fields = '__all__'
   def clean_image(self):
       picture = self.cleaned_data.get("image")
       if not picture:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(picture)
           print(w)
           print(h)
           if w > 400 or w < 100:
               raise forms.ValidationError("The image is %i pixel wide. It's supposed to be between 100 to 200" % w)
           if h > 400 or h < 100:
               raise forms.ValidationError("The image is %i pixel high. It's supposed to be between 100 to 200" % h)
           #if w != h: 
               #raise forms.ValidationError("Crop picture to same height and width")
       return picture

class MyAdmin( admin.ModelAdmin):
    form = myForm

admin.site.register(Student, MyAdmin)
admin.site.register(Notification)
admin.site.register(Department)
admin.site.register(Faculty)