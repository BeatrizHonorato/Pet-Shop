from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class VeterinarioManager(BaseUserManager):
    def create_user_vet(self, email, nome, endereco, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido.')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, endereco=endereco, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nome, password, **extra_fields)

class Veterinario(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=250, default="joana.silva@gmail.com")
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    nome = models.CharField(max_length=100, default="Joana da Silva")
    crmv = models.CharField(max_length=7, default="SP-0000")
    telefone = models.CharField(max_length=13, default="00 00000-0000")
    telefone2 = models.CharField(max_length=13, default="00 00000-0000")
    cep = models.CharField(max_length=8, default="00000-000")
    logradouro = models.CharField(max_length=200, default="Rua 1")
    numero = models.CharField(max_length=5, default="00000")
    complemento = models.CharField(max_length=200, default="")
    bairro = models.CharField(max_length=100, default="São José")
    cidade = models.CharField(max_length=100, default="Araras")
    estado = models.CharField(max_length=2, default="SP")
    servicos_oferecidos = models.ManyToManyField('Servicos', related_name='veterinarios')

    objects = VeterinarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return f"{self.nome} (CRMV: {self.crmv})"
    
class Servicos(models.Model):
    SERVICOS = (
        ('BANHO_E_TOSA', 'Banho e Tosa'),
        ('TOSA_HIGIENICA', 'Tosa Higiênica'),
        ('HIDRATACAO', 'Hidratação'),
        ('VACINACAO', 'Vacinação'),
        ('EXAMES_LABORATORIAIS', 'Exames Laboratórias'),
        ('MICROCHIPAGEM', 'Microchipagem'),
        ('CONSULTA_CLINICA', 'Consulta Clínica'),
        ('ATENDIMENTO_DOMICILIAR', 'Atendimento Domiciliar'),
        ('ATENDIMENTO_24_HORAS', 'Atendimento 24 horas'),
        ('HOSPEDAGEM', 'Hospedagem'),
        ('TRANSPORTE', 'Transporte'),
        ('ADESTRAMENTO', 'Adestramento'),
    )

    servicos = models.CharField(max_length=150, choices=SERVICOS)
    servicos_personalizados = models.CharField(max_length=150)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE, related_name='servicos')

    def __str__(self):
        return self.servicos
    
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=13, default="00 00000-0000")
    cep = models.CharField(max_length=8, default="00000-000")
    logradouro = models.CharField(max_length=200, default="Rua 10")
    numero = models.CharField(max_length=5, default="00000")
    complemento = models.CharField(max_length=200, default="")
    bairro = models.CharField(max_length=100, default="Goiás")
    cidade = models.CharField(max_length=100, default="Araras")
    estado = models.CharField(max_length=2, default="SP")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
      
class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    data_aplicacao = models.DateField()
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE, related_name='vacinas_aplicadas')
    proxima_dose = models.DateField(null=True, blank=True)
    animal = models.ForeignKey('Animais', on_delete=models.CASCADE, related_name='vacinas_aplicadas')

    def __str__(self):
        return self.nome

class Vermifugos(models.Model):
    produto = models.CharField(max_length=100)
    data = models.DateField()
    dose = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    animal = models.ForeignKey('Animais', on_delete=models.CASCADE, related_name='vermifugos_administrados')

    def __str__(self):
        return self.produto

class Animais(models.Model):
    PORTES = (
        ('PEQUENO', 'Pequeno'),
        ('MEDIO', 'Medio'),
        ('GRANDE', 'Grande'),
    )
    SEXO = (
        ('FEMININO', 'Feminino'),
        ('MASCULINO', 'Masculino'),
    )

    nome = models.CharField(max_length=100, default="Bus")
    especie = models.CharField(max_length=100, default="Canino")
    porte = models.CharField(max_length=20, choices=PORTES)
    raca = models.CharField(max_length=150, default="Pastor Alemão")
    cor = models.CharField(max_length=100, default="Preto")
    sexo = models.CharField(max_length=10, choices=SEXO)
    nascimento = models.DateField(null=True, blank=True)
    vacinas = models.ManyToManyField('Vacina', related_name='animais_vacinados')
    vermifugos = models.ManyToManyField('Vermifugos', related_name='animais_vermifugados')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='animais')

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    animal = models.ForeignKey('Animais', on_delete=models.CASCADE)
    procedimento = models.ForeignKey('Servicos', on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"Agendamento para {self.animal} - {self.procedimento} em {self.data} às {self.horario}"
