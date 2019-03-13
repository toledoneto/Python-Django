from django.db import models
from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'User pode deletar clientes'),
        )

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)

        data = {'cliente': self.first_name}
        plain_text = render_to_string('clientes/emails/novo_cliente.txt', data)
        html_email = render_to_string('clientes/emails/novo_cliente.html', data)
        # send_mail(
        #     'Novo cliente cadastrado',
        #     plain_text,
        #     'seuemail_FROM@provedor.com',
        #     ['seuemail_TO@provedor.com'],
        #     html_message=html_email,
        #     fail_silently=False,
        # )
        #
        # mail_admins(
        #     'Novo cliente cadastrado',
        #     plain_text,
        #     html_message=html_email,
        #     fail_silently=False,
        # )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
