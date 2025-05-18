class texto:
    def texto_inicial():
        home = """
Olá! 👋 Eu sou o Bot de Atendimento. Como posso te ajudar hoje?
Escolha uma opção:
1️⃣ Informações  
2️⃣ Suporte técnico  
3️⃣ Falar com um atendente
        """
        return home
    
    def info_menu():
        return """
📚 Menu de Informações:
1️⃣ Horário de funcionamento
2️⃣ Endereços
3️⃣ Produtos e serviços
4️⃣ Voltar ao menu principal
        """
    
    def suporte_menu():
        return """
🛠️ Suporte Técnico:
1️⃣ Problemas com produto
2️⃣ Dúvidas técnicas
3️⃣ Reportar bug
4️⃣ Voltar ao menu principal
        """
    
    def atendente_menu():
        return """
👨‍💼 Você será conectado com um de nossos atendentes em breve.
Por favor, descreva brevemente seu problema enquanto aguarda:
        """
    
    def horario_funcionamento():
        return """
⏰ Nosso horário de funcionamento:
Segunda a Sexta: 08:00 - 18:00
Sábado: 09:00 - 13:00
Domingo: Fechado

4️⃣ Voltar ao menu anterior
        """
    
    def enderecos():
        return """
📍 Nossos endereços:
Matriz: Rua Principal, 123
Filial 1: Av. Secundária, 456
Filial 2: Praça Central, 789

4️⃣ Voltar ao menu anterior
        """
    
    def produtos_servicos():
        return """
🏷️ Nossos produtos e serviços:
- Consultoria
- Desenvolvimento
- Suporte técnico
- Treinamentos

4️⃣ Voltar ao menu anterior
        """
    
    
    