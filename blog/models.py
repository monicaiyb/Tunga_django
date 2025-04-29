from django.db.models import Model
from django.db.models import CharField, DateTimeField,BooleanField, ForeignKey,CASCADE
# Create your models here.
class Author(Model):
    first_name=CharField(max_length=100)
    last_name=CharField(max_length=100)
    created_at=DateTimeField(auto_now_add=True)
    is_published=BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Blog (Model):
    title=CharField(max_length=200)
    description=CharField(max_length=500)
    created_at=DateTimeField(auto_now_add=True)
    completed=BooleanField(default=False)
    artist = ForeignKey(Author, on_delete=CASCADE)