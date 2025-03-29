from django import forms
from .models import Booking, Table
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[MinValueValidator(timezone.now().date())]
    )
    guests = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'guests', 'special_requests']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_active=True)
        
        # Set initial time to next available slot
        now = timezone.now()
        if now.hour < 11:
            initial_time = '11:00'
        elif now.hour >= 21:
            initial_time = '11:00'
        else:
            initial_time = f"{now.hour + 1}:00"
        
        self.fields['time'].initial = initial_time