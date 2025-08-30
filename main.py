import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# ----------------------
# Configuração do prompt
# ----------------------
template = """
Você é um Scrum Master virtual chamado ScrumBOT AI. 
Seu papel é ajudar equipes a aplicar métodos ágeis. 
Siga estas diretrizes:

- Transformar descrições de funcionalidades em User Stories no formato:
  "Como [persona], quero [funcionalidade], para [benefício]".
- Sempre sugerir critérios de aceitação.
- Manter o tom de um Scrum Master ajudando o time.
- Auxiliar em priorização, estimativas, detecção de impedimentos, retrospectiva e geração de Kanban.
- Responda sempre em português do Brasil.

Histórico da conversa: {context}

Pergunta do usuário: {question}

Resposta:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# ----------------------
# Backlog
# ----------------------
backlog = []

def salvar_backlog():
    with open("backlog.json", "w", encoding="utf-8") as f:
        json.dump(backlog, f, ensure_ascii=False, indent=4)

def carregar_backlog():
    global backlog
    try:
        with open("backlog.json", "r", encoding="utf-8") as f:
            backlog = json.load(f)
    except FileNotFoundError:
        backlog = []

# ----------------------
# Funções especiais
# ----------------------
def priorizar_backlog(metodo="MoSCoW"):
    if not backlog:
        print("⚠️ Nenhuma User Story no backlog ainda.")
        return
    backlog_texto = "\n".join([f"- {item}" for item in backlog])
    prompt_priorizacao = f"""
Você é um Scrum Master. Organize o seguinte backlog aplicando a técnica {metodo}.

Backlog:
{backlog_texto}

Explique rapidamente como foi feita a priorização.
"""
    result = model.invoke(prompt_priorizacao)
    print("\n📊 Backlog Prioritizado:\n")
    print(result)

def estimar_backlog():
    if not backlog:
        print("⚠️ Nenhuma User Story no backlog ainda.")
        return
    backlog_texto = "\n".join([f"- {item}" for item in backlog])
    prompt_estimativa = f"""
Você é um facilitador de Sprint Planning. 
Sugira estimativas de pontos de história (1,2,3,5,8,13,21) para as seguintes User Stories. Justifique brevemente cada estimativa.

Backlog:
{backlog_texto}

Formato:
- User Story
  Estimativa: X pontos
  Justificativa: ...
  Responda sempre em português do Brasil.
"""
    result = model.invoke(prompt_estimativa)
    print("\n🎯 Estimativas sugeridas:\n")
    print(result)

def detectar_impedimentos():
    print("\nDigite os registros do Daily Stand-up (ou 'fim' para encerrar):")
    registros = []
    while True:
        linha = input("Registro: ")
        if linha.lower() == "fim":
            break
        registros.append(linha)
    if not registros:
        print("⚠️ Nenhum registro fornecido.")
        return
    registros_texto = "\n".join([f"- {r}" for r in registros])
    prompt_impedimentos = f"""
Você é um Scrum Master virtual. Analise os seguintes registros de Daily Stand-up 
e identifique impedimentos ou problemas recorrentes (dependências, gargalos, sobrecarga).

Registros:
{registros_texto}
"""
    result = model.invoke(prompt_impedimentos)
    print("\n🚨 Impedimentos detectados:\n")
    print(result)

def retrospecitiva_agil():
    print("\nDigite os feedbacks da Sprint (ou 'fim' para encerrar):")
    feedbacks = []
    while True:
        linha = input("Feedback: ")
        if linha.lower() == "fim":
            break
        feedbacks.append(linha)
    if not feedbacks:
        print("⚠️ Nenhum feedback fornecido.")
        return
    feedbacks_texto = "\n".join([f"- {f}" for f in feedbacks])
    prompt_retro = f"""
Você é um Scrum Master virtual. Organize os feedbacks em Start, Stop, Continue
e sugira planos de ação práticos para cada categoria.

Feedbacks:
{feedbacks_texto}
"""
    result = model.invoke(prompt_retro)
    print("\n📋 Retrospectiva Ágil:\n")
    print(result)

def cliente_virtual():
    print("\nInteragindo com o Cliente Virtual (Product Owner). Digite 'fim' para encerrar.\n")
    contexto = "Você é o Product Owner do projeto, responsável por esclarecer dúvidas, negociar requisitos e validar entregas com o time."
    while True:
        pergunta = input("Time: ")
        if pergunta.lower() == "fim":
            print("Encerrando interação com o Cliente Virtual ✅\n")
            break
        prompt_cliente = f"""
{contexto}

O time perguntou: {pergunta}

Responda como um Product Owner profissional.
"""
        resposta = model.invoke(prompt_cliente)
        print("Cliente Virtual:", resposta)

def gerar_kanban():
    if not backlog:
        print("⚠️ Nenhuma User Story no backlog ainda.")
        return
    backlog_texto = "\n".join([f"- {item}" for item in backlog])
    prompt_kanban = f"""
Você é um Scrum Master virtual. 
Organize o backlog em um quadro Kanban com colunas: To Do, Doing, Done.
Backlog:
{backlog_texto}

Responda no formato:
To Do:
- ...
Doing:
- ...
Done:
- ...
"""
    result = model.invoke(prompt_kanban)
    print("\n📋 Quadro Kanban sugerido pela IA:\n")
    print(result)

# ----------------------
# Loop principal
# ----------------------
def handle_conversation():
    carregar_backlog()
    context = ""
    print(
            "Bem-vindo ao *ScrumBOT AI*!\n"
            "Este é o seu assistente para Métodos Ágeis.\n"
            "Eu posso ajudar você e sua equipe a:\n"
            "✅ Criar User Stories a partir das suas ideias\n"
            "✅ Priorizar o backlog automaticamente (MoSCoW, WSJF...)\n"
            "✅ Sugerir estimativas de esforço (Planning Poker virtual)\n"
            "✅ Detectar impedimentos nas Dailies\n"
            "✅ Conduzir retrospectivas ágeis com insights\n"
            "✅ Simular o papel de um Product Owner (cliente)\n"
            "✅ Gerar um quadro Kanban automaticamente\n\n"
            "Dica: comece me dizendo uma funcionalidade que gostaria de implementar no sistema\n"
            "Ou digite 'ajuda' para verificar comandos especiais (IMPORTANTE!)"
        )
      
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input == 'exit':
            print("Encerrando... backlog salvo em backlog.json ✅")
            salvar_backlog()
            break
        elif user_input == 'priorizar':
            priorizar_backlog("MoSCoW")
            continue
        elif user_input == 'estimar':
            estimar_backlog()
            continue
        elif user_input == 'impedimentos':
            detectar_impedimentos()
            continue
        elif user_input == 'retrospectiva':
            retrospecitiva_agil()
            continue
        elif user_input == 'cliente':
            cliente_virtual()
            continue
        elif user_input == 'kanban':
            gerar_kanban()
            continue
        elif user_input == 'ajuda':
            print(
            "Comandos disponíveis:\n"
            "- exit → sair\n"
            "- priorizar → priorização do backlog\n"
            "- estimar → Sprint Planning\n"
            "- impedimentos → detectar problemas\n"
            "- retrospectiva → Retrospectiva Ágil\n"
            "- cliente → simular Product Owner\n"
            "- kanban → gerar quadro Kanban\n"
            )
            continue


        # Conversa normal para gerar User Stories
        result = chain.invoke({"context": context, "question": user_input})
        print("ScrumBOT:", result)

        context += f"\nUser: {user_input}\nAI: {result}" 

        # Captura User Story
        if "Como " in result:
            backlog.append(result.strip())
            salvar_backlog()
            print("📌 User Story adicionada ao backlog!")


# ----------------------
# Executar
# ----------------------
if __name__ == "__main__":
    handle_conversation()
