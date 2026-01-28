# 📐 Demonstração do Teorema de Pitágoras por meio das Relações Métricas no Triângulo Retângulo

Este repositório é dedicado a scripts em **Python**, utilizando a biblioteca **Manim**, para a elaboração de uma animação que demonstra o **Teorema de Pitágoras** por meio das **relações métricas no triângulo retângulo**.

---

## 🎯 Para que serve?

Demonstrar, de forma **visual e dinâmica**, o motivo pelo qual a soma dos quadrados dos catetos de um triângulo retângulo é igual ao quadrado da sua hipotenusa.

---

## 🛠️ Tecnologias utilizadas

- Python 3.13
- Biblioteca Manim

---

## ▶️ Como executar o projeto

⚠️ **Antes de executar o projeto, é necessário instalar a biblioteca Manim.**  
As instruções oficiais de instalação estão disponíveis em:

👉 https://github.com/ManimCommunity/manim

Após a instalação, copie e execute os comandos abaixo no terminal:

```bash
# Clone o repositório
git clone https://github.com/w1esther/Pitagoras-dem-rm.git

# Acesse a pasta do projeto
cd Pitagoras-dem-rm

# Execute a animação com o Manim

# Baixa resolução
manim -pql dem_rm.py AlinhaTriangulos

# Média resolução
manim -pqm dem_rm.py AlinhaTriangulos

# Alta resolução
manim -pqk dem_rm.py AlinhaTriangulos
