# story-children-gemma3

**Descrição breve:** Prompt programável para geração de histórias infantis pensado para videos no youtube de 1 minuto.

## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
  - [Pré-requisitos](#pré-requisitos)
  - [Configuração de path_history](#configuração-de-path_history)
  - [Instalando Dependências](#instalando-dependências)
- [Notas das versões](#notas_das_versões)

## Introdução

[Em construlçai]

## Instalação

Primeiro instale o servidor local do Ollama disponível em [Link](https://ollama.com/).

Inicie o Ollama conforme documentação.

Garanta o endereço host http://127.0.0.1:11434/


### Instale story-children-gemma3


```shell
pip install story-children-gemma3

```

### Configuração de path_history

Pelo menos uma vez é necessário implementar a função **utils.setup.config()** para definir o caminho.


```python
from story_chilren_gemma3.utils import setup

utils.setup.config()

```
### Pré-requisitos


- Python = "3.8+"

## Notas das versões

### Versão 0.1.7
- Fix-Bug: Execuções scripts como programs, utils e textToHistory!
