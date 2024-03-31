from django.test import TestCase
from .models import Veterinario, Servicos, Cliente, Vacina, Vermifugos, Animais, Agendamento
from datetime import date, time

class VeterinarioTest(TestCase):
    def test_str_method(self):
        veterinario = Veterinario.objects.create(nome="Joana", crmv="SP-1234")
        self.assertEqual(str(veterinario), "Joana (CRMV: SP-1234)")

class ServicosTest(TestCase):
    def test_str_method(self):
        servico = Servicos.objects.create(servicos="Banho e Tosa", servicos_personalizados="Personalizado", veterinario=Veterinario.objects.create())
        self.assertEqual(str(servico), "Banho e Tosa")

class ClienteTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(nome="Cliente Teste", telefone="00 00000-0000", cep="00000-000", logradouro="Rua Teste", numero="123", bairro="Bairro Teste", cidade="Cidade Teste", estado="TE")

    def test_cliente_nome(self):
        cliente = Cliente.objects.get(nome="Cliente Teste")
        self.assertEqual(cliente.nome, "Cliente Teste")

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

class AgendamentoTest(TestCase):
    def test_str_method(self):
        cliente = Cliente.objects.create(nome="João Pereira")
        animal = Animais.objects.create(nome="Rex", cliente=cliente)
        veterinario = Veterinario.objects.create(nome="Dr. Smith")
        servico = Servicos.objects.create(servicos="Banho e Tosa", veterinario=veterinario)
        agendamento = Agendamento.objects.create(animal=animal, procedimento=servico, data=date(2024, 3, 30), horario=time(10, 0, 0))
        self.assertEqual(str(agendamento), "Agendamento para Rex - Banho e Tosa em 2024-03-30 às 10:00:00")
