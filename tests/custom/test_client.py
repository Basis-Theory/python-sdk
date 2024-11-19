import os
import time
import uuid

import pytest

from basis_theory import BasisTheory, NotFoundError

def test_should_get_self() -> None:
    client = new_management_client()
    actual = client.tenants.self_.get()
    assert actual.name == 'SDK Integration Tests'

def test_should_create_update_patch_reactors() -> None:
    management_client = new_management_client()
    application_id = create_application(management_client)
    reactor = management_client.reactors.create(
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        code="""module.exports = async function (req) {
            // Do something with req.configuration.SERVICE_API_KEY
            return {
                raw: {
                    foo: "bar"
                }
            };
        };""",
        configuration={
            "SERVICE_API_KEY": "key_abcd1234"
        },
        application={
            "id": application_id
        }
    )
    reactor_id = reactor.id
    assert reactor_id is not None

    reactor_update = management_client.reactors.update(
        id = reactor_id,
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        code="""module.exports = async function (req) {
          // Do something with req.configuration.SERVICE_API_KEY
        
          return {
            raw: {
              foo: "bar",
              update: "updated"
            }
          };
        };""",
        configuration={
            "SERVICE_API_KEY": "key_abcd1234",
            "NEW_API_KEY": "key_new"
        },
        application={
            "id": application_id
        }
    )
    update_reactor_id = reactor_update.id
    assert update_reactor_id == reactor_id

    # client.reactors.patch(
    #     id = reactor_id,
    #     name='(Deletable) python-SDK-' + str(uuid.uuid4()),
    #     configuration={
    #         "SERVICE_API_KEY": "key_abcd1234"
    #     }
    # )

    client = new_private_client()
    react_response = client.reactors.react(
        id=reactor_id,
        args={
            "foo": "bar"
        }
    )
    assert react_response.raw['foo'] == "bar"

    react_async_response = client.reactors.react_async(
        id=reactor_id,
        args={
            "foo": "bar"
        }
    )
    assert react_async_response.async_reactor_request_id is not None

def test_tokenize_basic() -> None:
    client = new_private_client()
    response = client.tokens.tokenize(
        request={
            "first_name": "John",
            "last_name": "Doe"
        }
    )
    assert is_guid(response["first_name"])
    assert is_guid(response["last_name"])

def test_tokenize_token() -> None:
    client = new_private_client()
    response = client.tokens.tokenize(
        request={
            "type": "token",
            "data": "Sensitive Value",
            "metadata": {
                "nonSensitive": "Non-Sensitive Value"
            },
            "search_indexes": [
                "{{ data }}"
            ],
            "fingerprint_expression": "{{ data }}"
        }
    )
    assert is_guid(response["id"])

def test_tokenize_card() -> None:
    client = new_private_client()
    response = client.tokens.tokenize(
        request={
            "type": "card",
            "data": {
                "number": "4242424242424242",
                "expiration_month": 12,
                "expiration_year": 2025,
                "cvc": "123"
            },
            "metadata": {
                "nonSensitive": "Non-Sensitive Value"
            }
        }
    )
    assert is_guid(response["id"])

def test_tokenize_array() -> None:
    client = new_private_client()
    response = client.tokens.tokenize(
        request=[
            "John",
            "Doe",
            {
                "type": "card",
                "data": {
                    "number": "4242424242424242",
                    "expiration_month": 12,
                    "expiration_year": 2025,
                    "cvc": "123"
                },
                "metadata": {
                    "nonSensitive": "Non-Sensitive Value"
                }
            },
            {
                "type": "token",
                "data": "Sensitive Value"
            }
        ]
    )
    assert is_guid(response[0])
    assert is_guid(response[1])
    assert is_guid(response[2]["id"])
    assert is_guid(response[3]["id"])

def test_tokenize_composite() -> None:
    client = new_private_client()
    response = client.tokens.tokenize(
        request={
            "first_name": "John",
            "last_name": "Doe",
            "primary_card": {
                "type": "card",
                "data": {
                    "number": "4242424242424242",
                    "expiration_month": 12,
                    "expiration_year": 2025,
                    "cvc": "123"
                }
            },
            "sensitive_tags": [
                "preferred",
                {
                    "type": "token",
                    "data": "vip"
                }
            ]
        }
    )
    assert is_guid(response["first_name"])
    assert is_guid(response["last_name"])
    assert is_guid(response["primary_card"]["id"])
    assert is_guid(response["sensitive_tags"][0])
    assert is_guid(response["sensitive_tags"][1]["id"])

def test_detokenize_single() -> None:
    client = new_private_client()
    token_id = create_token('4242424242424242', client)
    actual = client.tokens.detokenize(
        request={
            "card_number": "{{ " + token_id+ " | json: '$.number' }}"
        }
    )
    assert actual["card_number"] == "4242424242424242"

def test_detokenize_list() -> None:
    client = new_private_client()
    token_id_1 = create_token('4242424242424242', client)
    token_id_2 = create_token('4111111111111111', client)
    actual = client.tokens.detokenize(
        request={
            "tokens": [
                "{{ " + token_id_1 + "  }}",
                "{{ " + token_id_2 + "  }}",
            ]
        }
    )
    assert actual["tokens"][0]["number"] == '4242424242424242'
    assert actual["tokens"][1]["number"] == '4111111111111111'

def test_bank_account_verify() -> None:
    client = new_private_client()
    token = client.tokens.create(
        type="bank",
        data={
            "routing_number": "021000021",
            "account_number": "00001"
        }
    )
    actual = client.enrichments.bankaccountverify(
        token_id=token.id
    )
    assert actual.status == "enabled"

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
    react(client, reactor_id)
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

pytest.mark.skip
def test_should_support_correlation_id_header() -> None:
    client = new_private_client()
    correlation_id = str(uuid.uuid4())

    client.tenants.self_(correlation_id=correlation_id).get()

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

def test_should_manage_webhooks_lifecycle() -> None:
    client = new_management_client()

    url = 'https://echo.basistheory.com/' + str(uuid.uuid4())
    webhook_id = create_webhook(client, url)
    get_and_validate_webhook_url(client, webhook_id, url)

    time.sleep(2) # Required to avoid error `The webhook subscription is undergoing another concurrent operation. Please wait a few seconds, then try again.`

    updated_url = 'https://echo.basistheory.com/' + str(uuid.uuid4())
    update_webhook(client, webhook_id, updated_url)
    get_and_validate_webhook_url(client, webhook_id, updated_url)

    time.sleep(2)  # Required to avoid error `The webhook subscription is undergoing another concurrent operation. Please wait a few seconds, then try again.`

    client.webhooks.delete(id=webhook_id)

    # Does not currently work due to empty body on 404
    # Issue eng-7345
    # ensure_webhook_removed(client, webhook_id)


def ensure_webhook_removed(client, webhook_id):
    try:
        client.webhooks.get(id=webhook_id)
        assert False, "Webhook should no longer be retrievable"
    except NotFoundError:
        pass


def update_webhook(client, webhook_id, updated_url):
    client.webhooks.update(
        id=webhook_id,
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        url=updated_url,
        events=['token.created', 'token.updated']
   )


def get_and_validate_webhook_url(client, webhook_id, url):
    webhook = client.webhooks.get(id=webhook_id)
    assert webhook.url == url


def create_webhook(client, url):
    webhook = client.webhooks.create(
        name='(Deletable) python-SDK-' + str(uuid.uuid4()),
        url=url,
        events=['token.created']
    )
    webhook_id = webhook.id
    return webhook_id


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

def is_guid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False