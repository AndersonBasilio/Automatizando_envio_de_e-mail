# Automatizando Envio de E-mail 📧

## 🔎 Visão Geral  
Este projeto tem como objetivo automatizar o envio de e-mails (por exemplo, para recrutadores) usando Python e automação do teclado/mouse com a biblioteca `pyautogui`.  
A ideia é facilitar o envio de mensagens com anexos, nome e destinatário pré-configurados, agilizando processos repetitivos de envio de e-mail.

## ✅ Funcionalidades  
- Permite definir o e-mail de destino, nome do destinatário e o arquivo a ser enviado.  
- Simulação de interação com interface (teclado/mouse) para automatizar o processo de envio — sem necessidade de intervenção manual a cada envio.  
- Código em Python, utilizando bibliotecas padrão e `pyautogui`, para máxima portabilidade.

## 🛠️ Tecnologias / Dependências  
- Python (versão compatível)  
- `pyautogui` — biblioteca usada para automação de entradas de teclado/mouse  

## 🚀 Como usar / Instalação  

### Pré-requisitos  
- Ter Python instalado na máquina.  
- Instalar a biblioteca `pyautogui`.  

```bash
pip install pyautogui
Executando o script
Clone este repositório:

bash
Copiar código
git clone https://github.com/AndersonBasilio/Automatizando_envio_de_e-mail.git
Acesse a pasta do projeto:

bash
Copiar código
cd Automatizando_envio_de_e-mail
Execute o script principal:

bash
Copiar código
python automatizando_envio_de_email.py
Siga as instruções do script para inserir e-mail de destino, nome, definir o arquivo a ser enviado etc.

🧪 Exemplo de uso
Por exemplo, enviar um currículo ou documento para recrutador, definindo e-mail, anexando o arquivo e disparando automaticamente, sem abrir manualmente o gerenciador de e-mail.

(Você pode adicionar aqui um exemplo real ou um print do resultado, se quiser — isso ajuda quem for usar o projeto a entender rapidamente.)

📄 Licença
Este projeto está licenciado sob a licença MIT.

🙋 Autor / Contato
Desenvolvedor: AndersonBasilio
Use as Issues do GitHub ou envie mensagem para contato caso queira sugerir melhorias ou relatar bugs.

💡 Possíveis melhorias / Versões futuras
Adicionar suporte a diferentes provedores de e-mail sem depender de automação via GUI (usando SMTP ou APIs).

Permitir envio de e-mail em lote: múltiplos destinatários a partir de um CSV ou base de dados.

Incluir configuração externa (arquivo JSON/YAML) para definir destinatários, assunto, corpo, anexos — facilitando reuso.

Tratar erros ou falhas (ex: caso o e-mail não seja enviado, ou automação falhe).

Implementar logs ou confirmação de envio para controle.


 
