from django.forms import ModelForm
from .models import Product, Review

class ProductForm(ModelForm):
    class Meta:
      model = Product
      fields =['title', 'featured_image', 'description','price']

     

    def __init__(self, *args, **kwargs):
       super(ProductForm, self).__init__(*args, **kwargs)

       for name, field in self.fields.items():
          field.widget.attrs.update({'class':'input'})


       #self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder':'Add Name'})
       #self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder':'Add Name'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            "value": 'Place your vote',
            "body": 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
   

