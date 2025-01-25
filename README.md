<h1><strong>Primeira Aplicação em Python: Sistema para Restaurantes</strong></h1>

<h2>📜 Sobre o Projeto</h2>
<p>
  Este repositório contém um projeto inicial desenvolvido em Python como parte do curso da Alura: 
  <a href="https://cursos.alura.com.br/course/python-crie-sua-primeira-aplicacao" target="_blank">
    Python: Crie sua Primeira Aplicação.
  </a>
</p>
<p>
  O objetivo do sistema é gerenciar restaurantes por meio de funcionalidades como cadastro, listagem e alteração de status (ativo/inativo).
</p>

<h2>🛠️ Funcionalidades</h2>
<ul>
  <li><strong>Cadastro de Restaurantes:</strong> Permite adicionar novos restaurantes à lista, informando nome, categoria, contato e CNPJ.</li>
  <li><strong>Listagem de Restaurantes:</strong> Exibe todos os restaurantes cadastrados de forma organizada.</li>
  <li><strong>Alteração de Status:</strong> Habilita a alternância do status (ativo/inativo) de um restaurante específico.</li>
  <li><strong>Menu Interativo:</strong> Oferece um menu para navegação entre as opções disponíveis.</li>
</ul>

<h2>🏗️ Estrutura do Projeto</h2>
<ul>
  <li><strong>Arquivo Principal:</strong> Contém a lógica do programa e funções principais como cadastro, listagem, alteração de status e controle do menu interativo.</li>
  <li><strong>Estrutura de Dados:</strong> Restaurantes são armazenados em uma lista de dicionários, com informações como nome, categoria, contato, CNPJ e status.</li>
</ul>

<h2>🚀 Como Executar o Projeto</h2>
<ol>
  <li>Certifique-se de ter o Python 3.10+ instalado em sua máquina.</li>
  <li>Clone o repositório para o seu computador:
    <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git</code></pre>
  </li>
  <li>Navegue até o diretório do projeto:
    <pre><code>cd seu-repositorio</code></pre>
  </li>
  <li>Execute o programa:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

<h2>🖼️ Exemplo de Saída</h2>
<p>Ao listar os restaurantes, o programa exibe algo como:</p>
<pre>
***************************
Você selecionou a listagem de restaurante, segue abaixo:
***************************

Nome do restaurante     | Categoria              | Contato             | CNPJ                   | Status
Padaria                | Comercio               | 11 977155199        | 045627/0001-91         | ativo
Sushi                  | Japones                | 21 9876555199       | 076543/0001-12         | desativado
Pizzaria               | pizza                  | 44 409763129        | 3427/0001-89           | desativado
</pre>

<h2>📂 Estrutura do Código</h2>
<ul>
  <li><strong>Funções:</strong> 
    <ul>
      <li><code>mensagem_inicial()</code>: Exibe a mensagem inicial do sistema.</li>
      <li><code>opcoes_de_uso()</code>: Mostra o menu de opções para o usuário.</li>
      <li><code>cadastrar_novo_restaurante()</code>: Cadastra um novo restaurante na lista.</li>
      <li><code>listar_restaurantes()</code>: Lista os restaurantes cadastrados.</li>
      <li><code>alternar_status_restaurante()</code>: Altera o status (ativo/inativo) de um restaurante.</li>
      <li><code>opcoes_escolhidas()</code>: Gerencia a navegação do menu principal.</li>
      <li><code>encerrar_app()</code>: Encerra o programa.</li>
    </ul>
  </li>
  <li><strong>Lista de Restaurantes:</strong> Armazena os dados dos restaurantes em formato de lista de dicionários.</li>
</ul>
