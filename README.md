# Documentação do Projeto

## Descrição

Este projeto consiste em um sistema para enviar uma captura de tela de um cliente para um servidor usando Python e a biblioteca Flask. O servidor recebe a captura de tela e a salva como um arquivo PNG. O cliente captura a tela do dispositivo, envia para o servidor e exibe um alerta com a resposta recebida do servidor.

## Configuração

Certifique-se de ter as seguintes dependências instaladas:

- Python 3
- Flask
- requests
- pyautogui
- ctypes (para exibir o alerta no cliente)

## Funcionamento

### server.py

O arquivo `server.py` contém o código para o servidor. Ele utiliza a biblioteca Flask para criar um servidor web. O servidor expõe um endpoint em `/screenshot` que espera receber uma solicitação HTTP POST contendo um arquivo chamado "screenshot". Quando a captura de tela é recebida, o servidor a salva como um arquivo chamado "screenshot.png" no diretório atual. Em seguida, uma resposta de sucesso é retornada para o cliente.

### client.py

O arquivo `client.py` contém o código para o cliente. Primeiro, ele usa a biblioteca pyautogui para capturar a tela do dispositivo e salvar a captura de tela como um arquivo chamado "screenshot.png". Em seguida, o cliente envia a captura de tela para o servidor usando uma solicitação HTTP POST para o endpoint `/screenshot`. O endereço IP do servidor é definido na variável `ip`. Após receber a resposta do servidor, o cliente exibe um alerta com o texto da resposta.

## Execução

1. Certifique-se de ter todas as dependências instaladas corretamente.

2. Execute o arquivo `server.py` para iniciar o servidor. Certifique-se de ter as permissões adequadas para acessar a porta definida (8000).

3. Execute o arquivo `client.py` no cliente para capturar a tela, enviar para o servidor e exibir o alerta com a resposta.

## Observações

- Este projeto é uma implementação hipotética e deve ser adaptado às suas necessidades específicas.
- Lembre-se de considerar questões de segurança ao implantar um servidor e permitir o acesso remoto ao seu dispositivo.

