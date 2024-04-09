from django.db import models

class Usuarioss(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    endereco = models.TextField(max_length=255)
    numero = models.IntegerField()
    bairro = models.TextField(max_length=255)
    cidade = models.TextField(max_length=255)
    estado = models.TextField(max_length=255)
    telefone = models.TextField(max_length=255)
    crmv = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    confirmar_senha = models.TextField(max_length=255)

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data_nascimento = models.DateField()
    telefone = models.IntegerField()
    cep = models.IntegerField()
    endereco = models.TextField(max_length=255)
    numero = models.IntegerField()
    bairro = models.TextField(max_length=255)
    cidade = models.TextField(max_length=255)
    estado = models.TextField(max_length=255)

class Pets(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    especie = models.TextField(max_length=255)
    porte = models.TextField(max_length=255)
    raca = models.TextField(max_length=255)
    cor = models.TextField(max_length=255)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()

