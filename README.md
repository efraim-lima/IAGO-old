# IAGO
Projeto do Robô que tenho trabalhado


# Para iniciar a usar os arquivos do IAGO precisamos, as vezes, instalar coisas e alterar coisas.

## Para tal criei este guia pra eu mesmo não me perder rsrrs

# Alguns apontamentos e comandos simples para que eu não esqueça

## Criar uma chave SSH na maquina

### Primeiro é legal ver as ja existentes:

ls -al ~/.ssh

### Depois criamos o par de chaves:

ssh-keygen -t ed25519 -C "efraim.alima@gmail.com"

### Este abaixo deu MAIS CERTO

ssh-keygen -t rsa -C efraim.alima@gmail.com

ssh-keygen -t rsa -b 4096 -C "efraim.alima@gmail.com"

### aparentemente a chave ficará salva no caminho: /home/efraim/.ssh/id_rsa

eval $(ssh-agent -s)

ssh-add ~/.ssh/id_ed25519

### Agora copiaremos a chave pública, basta copiar o texto que será gerado após

### o comando abaixo:

cat ~/.ssh/id_ed25519.pub

### testar a conexão:

ssh -T git@github.com

### Após todas as configurações basta fazer o clone.

git clone <URL do projeto>

## Os comandos que serão mais utilizados:
  
git add <path>
  
### para adicionar tudo dos arquivos
  
git add * 
  
### para salvar um determinado ponto de alteração
  
git commit -m "sua mensagem"
  
### sobe o repositório local para o online
  
git push 

## Configurar o git
  
git config --global user.email "efraim.alima@gmail.com"

git config --global user.name "Efraim"

git add .

git remote add origin https://github.com/efraim-lima/IAGO.git

git push -u origin master

git init

### para ver os repositórios remotos

git remote -v 

dir

dir <pasta>
  
###  para criar um arquivo
  
touch <file.extensão> 
  
git add <path>
  
### para salvar um determinado ponto de alteração
  
git commit -m "sua mensagem" 
  
### sobe o repositório local para o online
  
git push 
  
### para mostrar o historico de produção
  
git log 
  
### mostra como está o projeto agora
  
git status 
  
### para mostrar as alterações
  
git show <codigo do git log> 
  
### para criar projetos paralelos
  
git branch <nome da funcionalidade nova> 
  
### muda para a branch
  
git checkout <nome da funcionalidade nova> 
  
### para unir as branches
  
git merge <nome da funcionalidade nova> 
  
git branch -D <nome da funcionalidade nova>

## Confgurando o ambiente Python pra o crowler

sudo apt-get install pyhton3
  
sudo apt install python3-virtualenv
  
virtualenv iago
  
source iago/bin/activate
  
sudo pip install
  
sudo apt-get install python3-tk
  
### BeautifulSoup
### webdriver-manager
### PySimpleGUI
### lxml


### PARA TRABALHAR COM WEBGJ E THREE.JS

### criar uma pasta para receber os arquivos do clone
  
git clone https://github.com/designcourse/threejs-webpack-starter.git
  
cd ./<pasta onde criamos o clone>
  
npm i
  
### abre o servidor onde está a imagem ja criada
  
npm run dev 

### cancelei esse caminho abaixo

### Instalando o npm
  
sudo apt-get install npm
  
npm install --save three
  
npm init
  
npm install time-stamp

### depois basta ir no site direcionado pelo link a seguir:
  
https://www.npmjs.com/package/gltf-webpack-loader

### instalar o webpack
  
sudo apt install cmdtest
  
yarn add gltf-webpack-loader -D
  
npm install --save-dev webpack

### para a API
  
pip install flask

////////////////////////////////////////////////////

### creditos do criador da lua do site:
  
"Moon" (https://skfb.ly/6TwGU) by Akshat is licensed under Creative Commons Attribution (http:// creativecommons.org/licenses/by/4.0/).
