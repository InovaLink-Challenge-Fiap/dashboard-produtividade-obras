# Status do Projeto Dashboard de Produtividade

## O que já foi feito

- Dashboard rodando no Streamlit
- Leitura da planilha df_diarios.xlsx
- Filtro automático para mão de obra
- Filtros interativos na sidebar: obra, caderno e grupo
- Proteção contra erros e filtros que não retornam dados
- **Aba Dados:** tabela com todos os registros filtrados
- **Aba Estatísticas:** média, mediana, moda, desvio-padrão, variância, amplitude e CV
- **Aba Gráficos:** histograma, curva de densidade, boxplot por obra e barras por grupo
- **Aba Comparações:** tabela e gráfico comparando todas as obras
- **Aba Perguntas:** perguntas A, B, C e D com gráfico e texto

---

## O que ainda falta

### 1. Tabela de colunas da planilha (Aba Dados)
O professor pede que a gente explique o que cada coluna da planilha significa e qual o tipo de variável. No código, procurar por `# TODO: FALTA ADICIONAR a tabela classificando`.

### 2. Texto explicando média, mediana e moda (Aba Estatísticas)
Os números já estão calculados, mas o professor quer que a gente explique quando usar cada medida. No código, procurar por `# TODO: FALTA ADICIONAR texto explicando quando usar`.

### 3. Texto explicando desvio, variância, amplitude e CV (Aba Estatísticas)
Mesma lógica os valores estão lá mas precisam de explicação prática. No código, procurar por `# TODO: FALTA ADICIONAR texto explicando o que desvio`.

### 4. Lista de perguntas de um gestor (Aba Dados)
O professor quer que a gente escreva perguntas que um gestor de obras faria olhando esses dados, com nossas próprias palavras. No código, procurar por `# TODO: FALTA ADICIONAR a lista de perguntas`.

### 5. Reescrever as respostas das perguntas A, B, C e D IMPORTANTE
As respostas que aparecem embaixo dos gráficos nas perguntas A, B, C e D **foram geradas por IA**. O professor pediu que as respostas sejam escritas com as palavras do grupo.

No código, procurar por `# TODO: reescrever este texto com outras palavras palavras`.

### 6. Aba da questão extra vídeo do YouTube
Registre no dashboard as anotações do grupo e dúvidas sobre o video do youtube, pontos principais e explicação do coeficiente mencionado. No código, procurar por `# TODO: FALTA ADICIONAR a aba da questão extra`.

---

## Como rodar o projeto
cd ~/Downloads/dashboard_produtividade
streamlit run app.py




