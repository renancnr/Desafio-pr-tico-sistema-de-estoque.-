# Desafio prático: Sistema de Estoque com Threads

## 1. Objetivo

Simular oito clientes tentando comprar produtos de um estoque inicial de cinco unidades, comparando o comportamento do programa com e sem o uso de `threading.Lock`.

## 2. Arquivos do projeto

- **`estoque.py`**: versão que utiliza `threading.Lock` para proteger o acesso e a atualização do estoque.
- **`estoque_sem_lock.py`**: versão sem mecanismo de sincronização, permitindo observar possíveis condições de corrida.

## 3. Como executar

É necessário ter Python 3 instalado.

Execute cada arquivo separadamente:

```bash
python estoque.py
```

```bash
python estoque_sem_lock.py
```

## 4. Resultados esperados

### Com Lock

O estoque começa com cinco unidades e oito clientes tentam comprar uma unidade cada. O bloqueio protege a verificação e a atualização do estoque.

Resultado esperado:
- Cinco compras realizadas.
- Três clientes sem conseguir comprar.
- Estoque final igual a zero.

A ordem das mensagens pode variar entre as execuções.

### Sem Lock

Sem sincronização, diferentes threads podem verificar o estoque antes que outra thread termine de atualizá-lo. Isso pode provocar uma condição de corrida e resultados inconsistentes.

O resultado depende do escalonamento das threads. Por isso, as saídas devem ser observadas e registradas durante a execução, sem presumir que o estoque necessariamente ficará negativo em todas as tentativas.

## 5. Respostas às perguntas do desafio

### 1. O estoque final ficou coerente com o número de compras?

Com `Lock`, o estoque final esperado é zero, pois existem cinco unidades disponíveis e cada compra retira apenas uma unidade. Assim, cinco clientes compram e três não conseguem comprar.

### 2. O que aconteceu quando o programa foi executado sem proteção?

Sem `Lock`, várias threads podem verificar o estoque simultaneamente antes de sua atualização. Isso cria a possibilidade de inconsistências, como registrar compras além da quantidade disponível.

### 3. O resultado mudou entre as execuções?

O comportamento pode variar conforme o escalonamento das threads. As saídas reais devem ser comparadas após executar o programa várias vezes.

### 4. Qual
