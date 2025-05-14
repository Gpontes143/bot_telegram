
# 🤖 Fluxo de Bot de Atendimento Simples

## 1. Início do fluxo
**Comando:** `/start`

**Resposta do bot:**
```
Olá! 👋 Eu sou o Bot de Atendimento. Como posso te ajudar hoje?

Escolha uma opção:
1️⃣ Informações  
2️⃣ Suporte técnico  
3️⃣ Falar com um atendente
```

---

## 2. Usuário escolhe uma opção

### ➤ Opção 1: Informações
**Resposta do bot:**
```
Aqui estão algumas informações úteis:
- Horário de atendimento: 9h às 18h
- Site: https://example.com
- Contato: suporte@example.com

Deseja algo mais? (Digite /start para voltar ao menu)
```

---

### ➤ Opção 2: Suporte técnico
**Resposta do bot:**
```
Por favor, descreva seu problema técnico. 🛠️
Nossa equipe analisará e responderá o quanto antes.
```

---

### ➤ Opção 3: Falar com um atendente
**Resposta do bot:**
```
Ok! 👨‍💻 Um atendente será acionado.
Por favor, aguarde um momento.
```

---

## 🔄 Fluxo Lógico Simplificado (Diagrama)

```
[ /start ]
   ↓
[ Menu Principal ]
   ├──> [1] Informações      → Mensagem com links e dados úteis
   ├──> [2] Suporte técnico  → Solicita descrição do problema
   └──> [3] Falar com alguém → Informa que irá acionar atendente
```
