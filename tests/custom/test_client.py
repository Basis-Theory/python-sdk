import os
import uuid
from unittest.result import failfast

from basis_theory import BasisTheory, BasisTheoryEnvironment, NotFoundError


def test_should_get_self() -> None:
    client = new_management_client()
    actual = client.tenants.self_.get()
    assert actual.name == 'SDK Integration Tests'


def test_should_support_token_lifecycle() -> None:
    client = new_private_client()
    management_client = new_management_client()

    cardNumber = '6011000990139424'
    token_id = create_token(cardNumber, client)
    get_and_validate_card_number(cardNumber, client, token_id)

    # PATCH does not currently support correct `content-header`
    # updatedCardNumber = '4242424242424242'
    # update_token(client, token_id, updatedCardNumber)
    # get_and_validate_card_number(updatedCardNumber, client, token_id)

    application_id = create_application(management_client)

    # Proxies
    proxy_id = create_proxy(application_id, management_client)
    management_client.proxies.delete(id=proxy_id)

    # Reactors
    reactor_id = create_reactor(application_id, management_client)
    # REACT Doesn't work right now...? Returns a 403 requiring `token:use`.
    # However, the application has `token:use` and the reactor appears to be setup correctly in the Portal 🤷
    # react(management_client, reactor_id)
    management_client.reactors.delete(id=reactor_id)

    management_client.applications.delete(id=application_id)

    client.tokens.delete(id=token_id)
    try:
        client.tokens.get(id=token_id)
        assert False, "Token should no longer be retrievable"
    except NotFoundError:
        pass

def test_should_support_idempotency_header() -> None:
    client = new_private_client()
    idempotency_key = str(uuid.uuid4())

    firstTokenId = create_token('6011000990139424', client, idempotency_key)
    secondTokenId = create_token('4242424242424242', client, idempotency_key)

    assert firstTokenId == secondTokenId

def test_should_paginate_on_list_v1() -> None:
    client = new_private_client()
    page_size = 3
    page_number = 1

    tokens = client.tokens.list(size=page_size, page=page_number)

    for count, token in enumerate(tokens, start=1):
        if count > page_size:
            break

    assert count > page_size

def test_should_paginate_on_list_v2() -> None:
    client = new_private_client()
    page_size = 3

    tokens = client.tokens.list_v2(size=page_size)

    for count, token in enumerate(tokens, start=1):
        if count > page_size:
            break

    assert count > page_size

def react(management_client, reactor_id):
    expected = {
        'key1': 'Key1-' + str(uuid.uuid4()),
        'key2': 'Key2-' + str(uuid.uuid4()),
    }
    x = management_client.reactors.react(
        id=reactor_id,
        args=expected)
    assert x.raw['key1'] == expected['key1']
    assert x.raw['key2'] == expected['key2']


def create_reactor(application_id, management_client):
    reactor = management_client.reactors.create(
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        code='module.exports = function (req) {return {raw: req.args}}',
        application={
            "id": application_id
        }
    )
    reactor_id = reactor.id
    return reactor_id


def create_proxy(application_id, management_client):
    proxy = management_client.proxies.create(
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        destination_url='https://echo.basistheory.com/' + str(uuid.uuid4()),
        application={
            "id": application_id
        }
    )
    proxy_id = proxy.id
    return proxy_id


def create_application(management_client):
    application = management_client.applications.create(
        type='private',
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        permissions=['token:use']
    )
    application_id = application.id
    return application_id


def update_token(client, token_id, updatedCardNumber):
    client.tokens.update(id=token_id, data={"number": updatedCardNumber})


def get_and_validate_card_number(cardNumber, client, token_id):
    token = client.tokens.get(token_id)
    assert token.data['number'] == cardNumber


def create_token(cardNumber, client, idempotency_key=None):
    token = client.tokens.create(
        type="card",
        data={
            "number": cardNumber,
            "expiration_month": 4,
            "expiration_year": 2025,
            "cvc": 123,
        },
        metadata={
            "customer_id": "3181"
        },
        search_indexes=["{{ data.expiration_month }}", "{{ data.number | last4 }}"],
        fingerprint_expression="{{ data.number }}",
        mask={
            "number": "{{ data.number, reveal_last: 4 }}",
            "cvc": "{{ data.cvc }}",
        },
        deduplicate_token=False,
        containers=["/pci/high/"],
        idempotency_key=idempotency_key
    )
    token_id = token.id
    assert token_id is not None
    return token_id


def new_management_client():
    return BasisTheory(
        api_key=os.getenv('BT_MGT_API_KEY'),
        base_url=os.getenv('BT_API_URL')
    )


def new_private_client():
    return BasisTheory(
        api_key=os.getenv('BT_PVT_API_KEY'),
        base_url=os.getenv('BT_API_URL')
    )