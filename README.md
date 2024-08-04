# API de Organizador de Viagens

## Descrição

Esta API oferece funcionalidades para gerenciar viagens, incluindo a criação, busca e confirmação de viagens, a gestão de participantes e atividades, e a geração de links de compartilhamento.

## Instalação

Esta API é um aplicativo Flask em Python. Para executá-la, você precisará ter Python e Flask instalados.

Clone este repositório.Navegue até o diretório do projeto.
Instale as dependências:

```
 pip install
```

## Uso

A API utiliza JSON para troca de dados. Você pode utilizar ferramentas como Postman ou curl para interagir com os endpoints da API.

### Exemplos:

Criar uma nova viagem:

```
POST /trips
Content-Type: application/json

{
    "name": "Minhas Férias de Verão",
    "destination": "Havaí",
    "start_date": "2024-10-26",
    "end_date": "2024-11-02",
    "owner_name": "Mirian Quispe",
    "owner_email": "mirian@fake.email.com.br"
    "emails_to_invite": ["qwert@email.com.br", "asdfg@email.com.br"]
}
```

Buscar uma viagem pelo ID:

```
GET /trips/<trip_id>
```

Criar uma atividade para a viagem:

```
POST /trips/<trip_id>/activities
Content-Type: application/json

{
    "title": "Caminhada no Diamond Head",
    "occurs_at": "2024-10-28"
}
```

Confirmar viagem:

```
GET /trips/<trip_id>
```

Criar o link da viagem pelo id da viagem:

```
POST /trips/<tripId>/links
Content-Type: application/json

{
    "title": "Viagem a Bariloche"
}
```

Obter o link da viagem:

```
GET /trips/<tripId>/links
```

Criar o invite para um participante:

```
POST /trips/<tripId>/invites
Content-Type: application/json

{
    "name": "Mirian Quispe",
    "email": "mirian@fake.email.com.br"
}
```

Obter lista de participantes da viagem:

```
GET /trips/<tripId>/participants
```

Confirmar participante na viagem:

```
GET /participants/<participantId>/confirm
```

Criar uma atividade para a viagem:

```
POST /trips/<trip_id>/activities
Content-Type: application/json

{
    "title": "Caminhada no Diamond Head",
    "occurs_at": "2024-10-28"
}
```

Obter lista de atividades da viagem:

```
GET /trips/<tripId>/participants
```

## Dependências:

Esta API depende das seguintes bibliotecas externas:

- Flask
- Pytest
