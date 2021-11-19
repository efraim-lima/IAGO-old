# IAGO
Projeto do Robô que tenho trabalhado


//Para iniciar a usar os arquivos do IAGO precisamos, as vezes, instalar coisas e alterar coisas.
Para tal criei este guia pra eu mesmo não me perder rsrrs

//Segue alguns apontamentos e comandos simples para que eu não esqueça

//Criar uma chave SSH na maquina
//Primeiro é legal ver as ja existentes:
ls -al ~/.ssh
//Depois criamos o par de chaves:
ssh-keygen -t ed25519 -C "efraim.alima@gmail.com"
ssh-keygen -t rsa -b 4096 -C "efraim.alima@gmail.com"
//aparentemente a chave ficará salva no caminho: /home/efraim/.ssh/id_rsa
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
//Agora copiaremos a chave pública, basta copiar o texto que será gerado após
//o comando abaixo:
cat ~/.ssh/id_ed25519.pub
//testar a conexão:
ssh -T git@github.com
//Após todas as configurações basta fazer o clone.
git clone <URL do projeto>

//os comandos que serão mais utilizados:
//git add <path>
//git add * //para adicionar tudo dos arquivos
//git commit -m "sua mensagem" //para salvar um determinado ponto de alteração
//git push //sobe o repositório local para o online

//configurar o git
//git config --global user.email "efraim.alima@gmail.com"
//git config --global user.name "Efraim"
//git add .
//git remote add origin https://github.com/efraim-lima/IAGO.git
//git push -u origin master
//git init
//git remote -v //para ver os repositórios remotos
//dir
//dir <pasta>
//touch <file.extensão> // para criar um arquivo
//git add <path>
//git commit -m "sua mensagem" //para salvar um determinado ponto de alteração
//git push //sobe o repositório local para o online
//git log //para mostrar o historico de produção
//git status //mostra como está o projeto agora
//git show <codigo do git log> //para mostrar as alterações
//git branch <nome da funcionalidade nova> //para criar projetos paralelos
//git checkout <nome da funcionalidade nova> //muda para a branch
//git merge <nome da funcionalidade nova> //para unir as branches
//git branch -D <nome da funcionalidade nova>

//Confgurando o ambiente Python pra o crowler

//sudo apt-get install pyhton3
//sudo apt install python3-virtualenv
//virtualenv iago
//source iago/bin/activate
//sudo pip install
//sudo apt-get install python3-tk
//BeautifulSoup
//webdriver-manager
//PySimpleGUI
//lxml


//PARA TRABALHAR COM WEBGJ E THREE.JS

//criar uma pasta para receber os arquivos do clone
git clone https://github.com/designcourse/threejs-webpack-starter.git
cd ./<pasta onde criamos o clone>
npm i
npm run dev //abre o servidor onde está a imagem ja criada








//cancelei esse caminho abaixo

//Instalando o npm
//sudo apt-get install npm
//npm install --save three
//npm init
//npm install time-stamp

//depois basta ir no site direcionado pelo link a seguir:
https://www.npmjs.com/package/gltf-webpack-loader

//instalar o webpack
sudo apt install cmdtest
yarn add gltf-webpack-loader -D
npm install --save-dev webpack