from django.db import models

class Dealership(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='dealerships')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

  