from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100, null=False, verbose_name='logradouro')
    cep = models.CharField(max_length=9, null=False, verbose_name='CEP')
    bairro = models.CharField(max_length=100, null=False, verbose_name='bairro')
    complemento = models.CharField(max_length=100, null=True, verbose_name='complemento', blank=True)
    localidade = models.CharField(max_length=100, null=False, verbose_name='localidade')
    uf = models.CharField(max_length=2, null=False, verbose_name='UF')
    ibge = models.CharField(max_length=7, null=False, verbose_name='código do município')
    gia = models.CharField(max_length=10, null=True, verbose_name='GIA', blank=True)
    ddd = models.CharField(max_length=2, null=False, verbose_name='DDD')
    siafi = models.CharField(max_length=10, null=False, verbose_name='SIAFI')
