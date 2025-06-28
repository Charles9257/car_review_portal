 
 # reviews/models.py

from django.db import models
from users.models import CustomUser
from dealership.models import Dealership
from textblob import TextBlob

class Review(models.Model):
    SENTIMENT_CHOICES = (
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f'Review by {self.user.username} for {self.dealership.name}'
    
    def analyze_sentiment(self):
        analysis = TextBlob(self.review_text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.1:
            return 'positive'
        elif polarity < -0.1:
            return 'negative'
        else:
            return 'neutral'

    def save(self, *args, **kwargs):
        self.sentiment = self.analyze_sentiment()
        super().save(*args, **kwargs)
