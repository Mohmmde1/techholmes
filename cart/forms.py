from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Hidden

class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, label='Quantity')
    slug = forms.CharField(widget=forms.HiddenInput())
    def __init__(self, product_slug=None, *args, **kwargs):
        super(AddCartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'add_cart_form'
        self.helper.layout = Layout(
            Field('quantity'),
            Hidden('slug', value=product_slug),
            Submit('submit', 'Add to Cart')
        )
        self.helper.form_method = 'post'
        self.helper.form_action = f'/cart/'
