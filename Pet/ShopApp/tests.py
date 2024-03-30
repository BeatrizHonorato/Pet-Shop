from django.test import TestCase
from .models import Veterinario, Servicos, Cliente, Vacina, Vermifugos, Animais
from datetime import date

class VeterinarioTest(TestCase):
    def test_str_method(self):
        veterinario = Veterinario.objects.create(nome="Joana", crmv="SP-1234")
        self.assertEqual(str(veterinario), "Joana (CRMV: SP-1234)")

class ServicosTest(TestCase):
    def test_str_method(self):
        servico = Servicos.objects.create(servicos="Banho e Tosa", servicos_personalizados="Personalizado", veterinario=Veterinario.objects.create())
        self.assertEqual(str(servico), "Banho e Tosa")

class ClienteTest(TestCase):
    def test_str_method(self):
        cliente = Cliente.objects.create(nome="João Pereira")
        self.assertEqual(str(cliente), "João Pereira")

class VacinaTest(TestCase):
    def test_str_method(self):
        veterinario = Veterinario.objects.create(nome="Joana", crmv="SP-1234")
        cliente = Cliente.objects.create(nome="João Pereira")
        animal = Animais.objects.create(nome="Rex", cliente=cliente)
        vacina = Vacina.objects.create(nome="Vacina A", data_aplicacao=date.today(), veterinario=veterinario, animal=animal)
        self.assertEqual(str(vacina), "Vacina A")

class VermifugosTest(TestCase):
    def test_str_method(self):
        veterinario = Veterinario.objects.create(nome="Joana", crmv="SP-1234")
        cliente = Cliente.objects.create(nome="João Pereira")
        animal = Animais.objects.create(nome="Rex", cliente=cliente)
        vermifugo = Vermifugos.objects.create(produto="Vermífugo A", data=date.today(), dose=1, peso=10.5, animal=animal)
        self.assertEqual(str(vermifugo), "Vermífugo A")

class AnimaisTest(TestCase):
    def test_str_method(self):
        cliente = Cliente.objects.create(nome="João Pereira")
        animal = Animais.objects.create(nome="Rex", cliente=cliente)
        self.assertEqual(str(animal), "Rex")
