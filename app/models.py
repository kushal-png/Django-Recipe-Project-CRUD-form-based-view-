from django.db import models

# Create your models here.
class recipeModel(models.Model):
    title=models.CharField(max_length=100, unique=True, null=False)
    description=models.TextField(null=False)
    image=models.ImageField(upload_to="app")
    
    class Meta:
        app_label="app"
        db_table="recipe"
        ordering=["id"]
    
    def __str__(self) -> str:
        return f"recipe {self.id} with {self.title}"