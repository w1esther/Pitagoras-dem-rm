# 📐 Demonstração do Teorema de Pitágoras por meio das Relações Métricas no Triângulo Retângulo

Este repositório é dedicado a **scripts em Python**, utilizando a biblioteca **Manim**, para a elaboração de uma animação que demonstra o **Teorema de Pitágoras** por meio das **relações métricas no triângulo retângulo**.

---

## 🎯 Para que serve?

Demonstrar, de forma **visual e dinâmica**, o motivo pelo qual a soma dos quadrados dos catetos de um triângulo retângulo é igual ao quadrado da sua hipotenusa.

---

## 🛠️ Tecnologias utilizadas

* **Python 3.13**
* **Biblioteca Manim (Manim Community)**

---

## 🧠 Por que executar o Manim em um ambiente virtual?

O Manim deve ser executado em um **ambiente virtual** para garantir que todas as dependências necessárias estejam instaladas e isoladas do sistema. Isso evita conflitos de versões, erros de execução e problemas com bibliotecas gráficas e de vídeo, garantindo o funcionamento correto das animações.

---

## 🐍 O que é o Anaconda?

O **Anaconda** é um software que instala o Python e fornece ferramentas para gerenciar **ambientes virtuais** e **bibliotecas**. Ele não é uma IDE, mas facilita a organização de dependências e evita conflitos entre projetos.

---

## 💻 Instalando o Anaconda

1. Acesse o site oficial do Anaconda:

   * [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Baixe a versão correspondente ao **seu sistema operacional** (Windows, macOS ou Linux).
3. Execute o instalador e siga os passos:

   * Clique em **Next**
   * Aceite os termos (**I Agree**)
   * Selecione **Just Me (recommended)**
   * Mantenha o caminho padrão de instalação
4. Ao finalizar, feche o instalador.

⚠️ **Importante:** utilize o **terminal fornecido pelo Anaconda** no seu sistema operacional (Anaconda Prompt no Windows, Terminal no macOS/Linux com o Anaconda ativado).

---

## 🌱 Criando o ambiente virtual

Abra o **Anaconda Prompt** e execute:

```bash
conda create -n manim-env python=3.12
```

Esse comando cria um ambiente virtual chamado `manim-env` utilizando o Python 3.12.

Quando solicitado, confirme digitando `y`.

Ative o ambiente com:

```bash
conda activate manim-env
```

Se aparecer `(manim-env)` no início da linha, o ambiente está ativo.

---

## 📦 Instalando dependências essenciais

Algumas bibliotecas são fundamentais para o funcionamento do Manim:

### 🎨 Cairo

Responsável por desenhar formas, textos e elementos gráficos 2D.

### 🎥 FFmpeg

Responsável por juntar os frames gerados pelo Manim e gerar o vídeo final.

Instale ambas com:

```bash
conda install -c conda-forge cairo ffmpeg
```

---

## 🎬 Instalando o Manim

Com o ambiente ativado, instale o Manim via `pip`:

```bash
pip install manim
```

Verifique se a instalação funcionou:

```bash
manim --version
```

Se a versão do Manim aparecer, a instalação foi concluída com sucesso.

---

## 🔗 Clonando o repositório do GitHub

Escolha uma pasta no seu computador para guardar projetos (exemplo: `Documents/GitHub`) e execute:

```bash
cd C:\Users\seu_usuario\Documents\GitHub
git clone https://github.com/w1esther/Pitagoras-dem-rm.git
```

Entre na pasta do projeto:

```bash
cd Pitagoras-dem-rm
```

---

## ▶️ Executando a animação

Dentro da pasta do projeto, utilize um dos comandos abaixo:

### 🔹 Baixa resolução (mais rápido)

```bash
manim -pql dem_rm.py AlinhaTriangulos
```

### 🔹 Média resolução

```bash
manim -pqm dem_rm.py AlinhaTriangulos
```

### 🔹 Alta resolução

```bash
manim -pqk dem_rm.py AlinhaTriangulos
```

✨ Ambiente configurado e animação pronta para execução.

---

## 🔄 Como acessar um ambiente virtual já criado

Sempre que precisar utilizar novamente o projeto:

1. Abra o **Anaconda Prompt**
2. Ative o ambiente virtual com:

```bash
conda activate manim-env
```

Se o nome `(manim-env)` aparecer no início da linha, o ambiente está ativo.

Para verificar os ambientes disponíveis:

```bash
conda env list
```

Após ativar o ambiente, entre na pasta do projeto e execute normalmente os comandos do Manim.

