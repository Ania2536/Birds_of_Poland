from django import forms

from birds_app.models import Birds, Family, Comments, Wishlist, Quiz


class AddBirdForm(forms.ModelForm):
    family = forms.CharField()
    class Meta:
        model = Birds
        exclude = ['family', 'approve', 'author']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

class WishListForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        birds = Wishlist.objects.filter(user=user).values_list('birds', flat=True)
        birds = Birds.objects.exclude(id__in=birds)
        self.fields['birds'].queryset = birds
    class Meta:
        model = Wishlist
        fields = ['birds']

