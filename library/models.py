from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100,  null=False)
    synopsis = models.TextField( null=False)
    category = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title;

class Client(models.Model):
    name = models.CharField(max_length=50, null=False)
    birth = models.DateField( null=False)
    tel = models.CharField(max_length=15, null=False)

    def __str__(self) -> str:
        return self.name


class Withdraw(models.Model):
    withdraw_at = models.DateTimeField(auto_now_add=True, null=False)
    devolution_at = models.DateTimeField(null=True, blank=True)
    client_id = models.ForeignKey(Client, null=False, on_delete=models.DO_NOTHING)
    book_taken = models.ForeignKey(Book,null=False,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.book_taken.title + " | " + self.client_id.name