# Avantio Accommodation Scraper

Este projeto realiza **web scraping** na **página de reservas da Avantio (PMS)** para coletar informações relevantes sobre as propriedades cadastradas. O sistema automatiza o acesso e a extrai os dados de cada acomodação contida no banco de dados.

---

## Funcionalidades

- Login automático na plataforma **Avantio PMS** com resolução de autenticação de dois fatores.
- Navegação para a página de cada propriedade.
- Coleta de dados diretamente da página de avaliações.
- Exportação dos dados coletados para uma planilha **Excel**.

As informações obtidas incluem:

- **Nome da acomodação**
- **Avaliação no Portal desejado**
- **Link da acomodação**  
- **Perfil da acomodação**  
- **Status (ativo ou não)**  

---

##  Estrutura do Projeto

```
src/
├── crawler/
│   ├── driver.py              # Instancia o driver Selenium
│   ├── login/
│   │   ├── frontpage.py       # Realiza o login no site Avantio
│   │   └── twoFA.py           # Verifica a necessidade e fornece autenticação de 2 fatores
│   └── review_page/
│       └── airbnb.py          # Acessa e coleta informações da página de avaliações no Airbnb
├── database/
│   ├── connect.py             # Cria coneção com banco de dados
│   └── query.py               # Realiza queries no banco de dados e retorna os IDs das acomodações
├── logs/
│   └── log.py                 # Instancia os logs de Erro caso ocorra
├── execute_crawler.py         # Cria o processo de execução do Crawler
└── main.py                    # Ponto de entrada da aplicação
```

---

##  Como Funciona

1. O script realiza **login automático** e realizando a **Autenticação de 2 Fatores** no site **Avantio PMS** usando **Selenium**.
2. Consulta o banco de dados para obter a lista de **IDs de acomodações** a serem verificadas.
3. Para cada ID:
   - Acessa a página da acomodação.
   - Redireciona para a página de avaliações no **Airbnb**.
   - Coleta as informações detalhadas de cada acomodação.
4. Os dados são armazenados e exportados em um arquivo **accommodations.xlsx**.

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **Poetry** (para gerenciamento de dependências e ambientes virtuais)
- **Selenium**  
- **Pandas**  
- **SqlAlchemy**
- **PostgreSQL**
- **Pyotp**
- **Loguru**
---

## Pré-requisitos

- Python 3.10 ou superior
- Google Chrome (ou navegador compatível com Selenium WebDriver)
- ChromeDriver compatível com a versão do navegador
- Acesso ao banco de dados com as informações das acomodações

---

## Instalação e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/AngeloGagno/Avantio_Crawler.git
cd Avantio_Crawler
```

### 2. Instale as dependências com o Poetry
```bash
poetry install
```

### 3. Execute a aplicação
```bash
poetry run python src/main.py
```

### 4. Resultado
O arquivo `accommodations.xlsx` será gerado no diretório raiz com as informações das acomodações.

---

## Estrutura do Código

### `main.py`

Faz o login, coleta as informações de cada acomodação e gera a planilha Excel.

### `execute_crawler.py`

Cria todo o padrão de execução do **Crawler**

### `crawler/driver.py`

Instancia e configura o **Selenium WebDriver**.

### `crawler/login/frontpage.py`

Fornece o código de **dois fatores** e realiza a inserção caso necessario.

### `crawler/login/twoFA.py`

Automatiza o **login no site da Avantio**.

### `crawler/review_page/airbnb.py`

Navega até a página de avaliações da **Avantio** e coleta as informações necessárias.

### `database/query.py`

Faz a **consulta no banco de dados** para buscar os IDs das acomodações a serem verificadas.

### `logs/log.py`

Cria **logs de Erro** caso não encontre a propriedade, caso haja qualquer problema de conexão com o banco ou alteração na interface do sistema.
---
## Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- 📧 Email: angelogagno@gmail.com
- 🔗 LinkedIn: [Angelo Gagno](https://www.linkedin.com/in/angelogagno)
- 🐙 GitHub: [Angelo Gagno](https://github.com/angelogagno)

---

Desenvolvido por [Angelo Gagno](https://github.com/angelogagno).