# ScrumBOT AI - Assistente Virtual para Métodos Ágeis

## Descrição
ScrumBOT AI é um chatbot que atua como Scrum Master virtual, auxiliando equipes a aplicar métodos ágeis.  
Ele ajuda a transformar funcionalidades em User Stories, sugere critérios de aceitação, prioriza backlog, estima pontos de história, detecta impedimentos, conduz retrospectivas e gera quadros Kanban automaticamente.

## Funcionalidades
- Criar User Stories a partir de descrições de funcionalidades.
- Sugerir critérios de aceitação.
- Priorizar backlog utilizando técnicas como **MoSCoW**.
- Estimativas automáticas de pontos de história (Planning Poker virtual).
- Detecção de impedimentos a partir de registros de Daily Stand-up.
- Retrospectiva Ágil com insights organizados em **Start, Stop, Continue**.
- Simulação de interação com um **Product Owner virtual**.
- Geração automática de **Quadro Kanban**.

## Tecnologias Usadas
- [Python](https://www.python.org/)  
- [Ollama](https://ollama.com/) (para rodar modelos LLaMA 3 localmente)  
- [LangChain](https://www.langchain.com/) (para encadeamento de prompts)  
- [Git](https://git-scm.com/)  

## Como utilizar a aplicação

1. **Instale o Python**  
   [Download do Python](https://www.python.org/downloads/)

2. **Instale o Ollama**  
   [Guia de instalação do Ollama](https://ollama.com/download)

3. **Execute no terminal para baixar o modelo LLaMA 3**  
   ```bash
   ollama run llama3
    ```

4. **Clone o repositório do GitHub**

   ```bash
   git clone https://github.com/JoaoVCoutinho/ScrumBOT.git
   cd ScrumBOT
   ```

5. **Crie um ambiente virtual**

   ```bash
   python -m venv chatbot
   source chatbot/bin/activate   # Linux/macOS
   chatbot\Scripts\activate      # Windows
   ```

5. **Erros comuns no Windows**

   Ao ativar o ambiente virtual, você pode receber o seguinte erro:
   chatbot\Scripts\activate.ps1 : O arquivo ... não pode ser carregado porque a execução de scripts foi desabilitada neste sistema. Para permitir execução de scripts apenas nesta sessão do PowerShell, rode:
   
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   chatbot\Scripts\Activate.ps1
   ```

6. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

7. **Execute a aplicação (Atenção, deixe o Ollama aberto)**

   ```bash
   python main.py
   ```

Agora você já pode interagir com o **ScrumBOT AI** no terminal! 🚀
