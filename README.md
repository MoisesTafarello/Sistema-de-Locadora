# Trabalho-Sistema-de-Locadora

1️⃣ Introdução

O Sistema de Locadora de Filmes e Jogos é uma aplicação em Python que permite gerenciar clientes, filmes e jogos de forma prática e organizada. Com ele, é possível:

Cadastrar clientes;

Registrar itens para locação;

Controlar empréstimos e devoluções;

Acompanhar a disponibilidade de cada item.

O projeto foi desenvolvido utilizando conceitos de Programação Orientada a Objetos (POO), como herança e encapsulamento, servindo como exemplo para estudos de POO e oferecendo uma experiência completa de como uma locadora funciona de forma estruturada e eficiente.

2️⃣ Estrutura do Projeto 👨‍💻

O sistema está organizado em arquivos específicos para manter o código modular, claro e fácil de manter:

2.1 - itens.py 🎬🎮

Define as classes Item, Filme e Jogo, com todos os atributos e métodos necessários para locação, devolução e controle de disponibilidade.

2.2 - cliente.py 👤

Contém a classe Cliente, permitindo alugar, devolver e listar os itens que cada cliente possui.

2.3 - locadora.py 🏢

Classe Locadora, responsável por gerenciar listas de clientes e itens, oferecendo métodos para cadastrar, listar e controlar locações.

2.4 - main.py 🚀

Arquivo principal com o menu interativo, integrando todas as funcionalidades do sistema e permitindo que o usuário:

Cadastre clientes;

Cadastre filmes ou jogos;

Liste clientes e itens disponíveis;

Realize locações e devoluções;

Encerre o sistema.

2.5 - README.md 📃

Documentação completa do projeto, explicando cada classe, método e funcionalidade implementada.

3️⃣ Programação do Projeto 💻

O sistema foi desenvolvido utilizando POO em Python, garantindo modularidade e clareza no código.

3.1 Arquivos e Funções Principais 📂

main.py

Menu interativo para integrar todas as funcionalidades.

Loop contínuo até que o usuário escolha sair, com tratamento de exceções.

funcoes.py
Funções auxiliares que conectam o menu às operações das classes:

cadastrar_cliente(locadora) → adiciona um cliente;

cadastrar_item(locadora) → adiciona um Filme ou Jogo com todos os atributos;

locar_item(locadora) → permite alugar um item disponível;

devolver_item(locadora) → permite devolver um item locado.

3.2 Classes e Estrutura de Dados 🏢🎬🎮

Item (classe base)

Atributos: codigo, titulo, disponivel

Métodos: alugar() e devolver()

Filme (herda de Item)

Atributos adicionais: genero, duracao

Jogo (herda de Item)

Atributos adicionais: plataforma, faixa_etaria

Cliente

Atributos: nome, cpf, itens_locados

Métodos:

locar(item) → adiciona item à lista se disponível

devolver(item) → remove item da lista e atualiza disponibilidade

listar_itens() → exibe itens locados

Locadora

Atributos: clientes, itens

Métodos:

cadastrar_cliente(cliente)

cadastrar_item(item)

listar_clientes()

listar_itens() (exibe status: Disponível / Alugado)

3.3 Funcionamento do Sistema ⚙️

Cadastro: Clientes e itens são registrados no sistema;

Listagem: Visualização de clientes e itens disponíveis;

Locação: Cliente seleciona item disponível, que é adicionado à sua lista e marcado como alugado;

Devolução: Cliente devolve item, que é removido da lista e marcado como disponível;

Menu interativo: Todas as ações são realizadas através do menu, tornando o uso intuitivo e controlado.

4️⃣ Conclusão ✅

O Sistema de Locadora de Filmes e Jogos demonstra a aplicação prática de POO em Python, utilizando conceitos como herança, encapsulamento e modularidade.

Com ele, é possível:

Gerenciar clientes, filmes e jogos;

Controlar empréstimos e devoluções;

Filtrar itens por diferentes critérios;

Ter uma visão completa de como uma locadora funciona.

O projeto serve como um excelente recurso educacional, permitindo compreender a interação entre objetos e a importância de organizar código de forma clara.

Ele pode ser expandido facilmente, adicionando persistência em banco de dados, interface gráfica ou novas funcionalidades, tornando-o uma base sólida para aprendizado e desenvolvimento de sistemas mais complexos.
