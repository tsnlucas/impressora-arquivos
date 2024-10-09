# Impressora de Arquivos

Um aplicativo simples em Python para selecionar, imprimir e gerenciar arquivos (PDF, Word e texto) de forma eficiente.

## Funcionalidades

- **Selecionar Arquivos**: Permite ao usuário selecionar múltiplos arquivos (PDF, DOCX, TXT).
- **Imprimir Arquivos**: Envia os arquivos selecionados diretamente para a impressora.
- **Limpar Lista**: Remove todos os arquivos da lista selecionada.
- **Exportar Lista**: Salva a lista de arquivos selecionados em um arquivo de texto.
- **Histórico de Impressão**: Mantém um registro dos arquivos impressos em um arquivo `historico_impressao.txt`.

## Motivação

Este projeto foi desenvolvido como parte de um estudo utilizando inteligência artificial. A motivação para sua criação surgiu da limitação de ter que selecionar arquivos de 10 em 10 ou 15 em 15 no Windows, o que torna o processo de impressão menos eficiente. O objetivo é facilitar a seleção e impressão de múltiplos arquivos de uma só vez.

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `pywin32`: Para manipulação de impressoras no Windows.
  
  Para instalar as dependências, use:
  ```bash
  pip install pywin32
