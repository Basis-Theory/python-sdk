import os
import re
import uuid
from datetime import datetime, timedelta, timezone

from basis_theory import BasisTheory, NotFoundError


def new_private_test_tenant_client():
    return BasisTheory(
        api_key=os.getenv('BT_PVT_TEST_API_KEY'),
        base_url=os.getenv('BT_API_URL')
    )


def create_card_token(client, card_number):
    token = client.tokens.create(
        type="card",
        data={
            "number": card_number,
            "expiration_month": 12,
            "expiration_year": 2030,
            "cvc": 123,
        },
    )
    return token.id


def device_context():
    return {
        "screen_height": 1080,
        "screen_width": 1920,
        "user_agent_string": "python-sdk-test",
        "language_code": "en-US",
        "time_zone": "America/New_York",
        "java_script_enabled": True,
        "client_device_id": str(uuid.uuid4()),
        "client_reference_id": str(uuid.uuid4()),
        "platform_type": "WEB",
    }


def create_and_verify_enrollment(client, card_number, email, agent_ids=None):
    token_id = create_card_token(client, card_number)
    create_kwargs = {
        "token_id": token_id,
        "consumer": {"email": email},
    }
    if agent_ids:
        create_kwargs["agent_ids"] = agent_ids

    enrollment = client.agentic.enrollments.create(**create_kwargs)

    # Start verification
    verify_response = client.agentic.enrollments.verify.start(
        enrollment.id, device_context=device_context()
    )

    # Auto-approved cards are already verified after verify.start
    if verify_response.status != "approved":
        # OTP flow: select method, submit OTP, complete
        if verify_response.methods and len(verify_response.methods) > 0:
            client.agentic.enrollments.verify.method(
                enrollment.id, method_id=verify_response.methods[0].id
            )

        client.agentic.enrollments.verify.otp(enrollment.id, otp_code="123456")
        client.agentic.enrollments.verify.complete(enrollment.id, assurance_data={})

    return client.agentic.enrollments.get(enrollment.id)


def find_enrollment(client, enrollment_id):
    for enrollment in client.agentic.enrollments.list():
        if enrollment.id == enrollment_id:
            return enrollment
    return None


def find_instruction(client, agent_id, instruction_id, enrollment_id=None):
    kwargs = {}
    if enrollment_id:
        kwargs["enrollment_id"] = enrollment_id
    for instruction in client.agentic.agents.instructions.list(agent_id, **kwargs):
        if instruction.id == instruction_id:
            return instruction
    return None


# ── Agents ───────────────────────────────────────────────────────────────────


def test_agents_lifecycle() -> None:
    client = new_private_test_tenant_client()
    # Create
    agent_name = "(Deletable) python-SDK-agent-" + str(uuid.uuid4())
    agent = client.agentic.agents.create(name=agent_name)
    assert agent.id is not None
    assert agent.name == agent_name
    assert agent.status == "active"
    assert agent.enrollment_ids is not None
    assert agent.created_at is not None

    # Get and verify all fields match
    retrieved = client.agentic.agents.get(agent.id)
    assert retrieved.id == agent.id
    assert retrieved.name == agent.name
    assert retrieved.status == "active"
    assert retrieved.enrollment_ids == agent.enrollment_ids
    assert retrieved.created_at == agent.created_at

    # Update
    updated_name = "(Deletable) python-SDK-agent-updated-" + str(uuid.uuid4())
    updated = client.agentic.agents.update(agent.id, name=updated_name)
    assert updated.id == agent.id
    assert updated.name == updated_name
    assert updated.status == "active"
    assert updated.created_at == agent.created_at

    # Delete
    client.agentic.agents.delete(agent.id)

    # Verify deleted
    try:
        client.agentic.agents.get(agent.id)
        assert False, "Should have raised a 404 for agent not found"
    except NotFoundError:
        pass


# ── Enrollments ──────────────────────────────────────────────────────────────


def test_auto_approved_enrollment_lifecycle() -> None:
    client = new_private_test_tenant_client()

    # Create and verify enrollment (passkey bypass card)
    enrollment = create_and_verify_enrollment(
        client, "4000056655665556", "sdk-test@example.com"
    )
    assert enrollment.id is not None
    assert enrollment.status == "active"
    assert enrollment.provider is not None
    assert enrollment.created_at is not None

    # Verify card object fields
    assert enrollment.card is not None
    assert enrollment.card.brand == "visa"
    assert enrollment.card.bin is not None
    assert enrollment.card.last4 == "5556"
    assert enrollment.card.expiration_month is not None
    assert enrollment.card.expiration_year is not None

    # Get enrollment and verify all fields match
    retrieved = client.agentic.enrollments.get(enrollment.id)
    assert retrieved.id == enrollment.id
    assert retrieved.status == "active"
    assert retrieved.provider == enrollment.provider
    assert retrieved.card.brand == enrollment.card.brand
    assert retrieved.card.bin == enrollment.card.bin
    assert retrieved.card.last4 == enrollment.card.last4
    assert retrieved.card.expiration_month == enrollment.card.expiration_month
    assert retrieved.card.expiration_year == enrollment.card.expiration_year
    assert retrieved.created_at == enrollment.created_at

    # List enrollments (paginated) and verify structure
    listed = find_enrollment(client, enrollment.id)
    assert listed is not None
    assert listed.status == "active"
    assert listed.card.last4 == "5556"

    # Delete enrollment
    client.agentic.enrollments.delete(enrollment.id)


def test_otp_verification_flow() -> None:
    client = new_private_test_tenant_client()

    # Create a card token (OTP challenge Visa test card)
    token_id = create_card_token(client, "4000000000000002")

    # Create enrollment (will be pending_verification)
    enrollment = client.agentic.enrollments.create(
        token_id=token_id,
        consumer={"email": "sdk-test-otp@example.com"},
    )
    assert enrollment.id is not None
    assert enrollment.status == "pending_verification"
    assert enrollment.provider is not None
    assert enrollment.created_at is not None

    # Verify card object on initial create response
    assert enrollment.card is not None
    assert enrollment.card.brand == "visa"
    assert enrollment.card.bin is not None
    assert enrollment.card.last4 == "0002"
    assert enrollment.card.expiration_month is not None
    assert enrollment.card.expiration_year is not None

    # Start verification — expect challenge with OTP methods
    verify_response = client.agentic.enrollments.verify.start(
        enrollment.id, device_context=device_context()
    )
    assert verify_response.status == "challenge"
    assert verify_response.methods is not None
    assert len(verify_response.methods) > 0
    assert verify_response.methods[0].id is not None
    assert verify_response.methods[0].type is not None

    # Select verification method
    if verify_response.methods and len(verify_response.methods) > 0:
        client.agentic.enrollments.verify.method(
            enrollment.id, method_id=verify_response.methods[0].id
        )

    # Submit OTP (mock accepts any code)
    otp_response = client.agentic.enrollments.verify.otp(
        enrollment.id, otp_code="123456"
    )
    assert otp_response.status == "device_bound"

    # Complete verification
    complete_response = client.agentic.enrollments.verify.complete(enrollment.id, assurance_data={})
    assert complete_response.status == "verified"

    # Verify enrollment is now active with all fields
    completed = client.agentic.enrollments.get(enrollment.id)
    assert completed.id == enrollment.id
    assert completed.status == "active"
    assert completed.provider == enrollment.provider
    assert completed.card.brand == "visa"
    assert completed.card.last4 == "0002"
    assert completed.created_at == enrollment.created_at

    # Cleanup
    client.agentic.enrollments.delete(enrollment.id)


# ── Instructions ─────────────────────────────────────────────────────────────


def test_instructions_lifecycle_with_credentials() -> None:
    client = new_private_test_tenant_client()

    # Setup: create agent and auto-approved enrollment
    agent = client.agentic.agents.create(
        name="(Deletable) python-SDK-instruction-agent-" + str(uuid.uuid4())
    )

    enrollment = create_and_verify_enrollment(
        client,
        "4000056655665556",
        "sdk-test-instructions@example.com",
        agent_ids=[agent.id],
    )
    assert enrollment.status == "active"

    # Create instruction
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)

    instruction = client.agentic.agents.instructions.create(
        agent.id,
        enrollment_id=enrollment.id,
        amount={"value": "25.00", "currency": "USD"},
        description="(Deletable) python-SDK test purchase",
        expires_at=expires_at,
    )
    assert instruction.id is not None
    assert instruction.enrollment_id == enrollment.id
    assert instruction.status == "pending_verification"
    assert instruction.amount is not None
    assert instruction.amount.value == "25.00"
    assert instruction.amount.currency == "USD"
    assert instruction.expires_at is not None
    assert instruction.created_at is not None

    # Get instruction and verify all fields match
    retrieved = client.agentic.agents.instructions.get(agent.id, instruction.id)
    assert retrieved.id == instruction.id
    assert retrieved.enrollment_id == instruction.enrollment_id
    assert retrieved.status == instruction.status
    assert retrieved.amount.value == instruction.amount.value
    assert retrieved.amount.currency == instruction.amount.currency
    assert retrieved.created_at == instruction.created_at

    # Update instruction
    updated = client.agentic.agents.instructions.update(
        agent.id,
        instruction.id,
        amount={"value": "50.00", "currency": "USD"},
    )
    assert updated.id == instruction.id
    assert updated.amount.value == "50.00"
    assert updated.amount.currency == "USD"
    assert updated.enrollment_id == enrollment.id
    assert updated.created_at == instruction.created_at

    # List instructions (paginated) and verify structure
    listed = find_instruction(client, agent.id, instruction.id)
    assert listed is not None
    assert listed.enrollment_id == enrollment.id
    assert listed.amount.value == "50.00"

    # Verify instruction (required before credentials can be retrieved)
    instr_verify_response = client.agentic.agents.instructions.verify.start(
        agent.id, instruction.id, device_context=device_context()
    )
    # Passkey bypass card returns verified immediately
    assert instr_verify_response.status == "verified"

    # Confirm instruction is now approved
    approved = client.agentic.agents.instructions.get(agent.id, instruction.id)
    assert approved.status == "approved"
    assert approved.id == instruction.id
    assert approved.enrollment_id == enrollment.id

    # Get credentials
    credentials = client.agentic.agents.instructions.credentials.create(
        agent.id,
        instruction.id,
        merchant={
            "name": "(Deletable) Test Merchant",
            "url": "https://example.com",
            "country_code": "US",
        },
    )
    assert credentials.card.number is not None
    assert credentials.card.expiration_month is not None
    assert credentials.card.expiration_year is not None
    assert credentials.card.cvc is not None

    # Verify mock virtual card number format: 400000100000 + last 4
    assert re.match(r"^400000100000\d{4}$", credentials.card.number)

    # Delete instruction
    client.agentic.agents.instructions.delete(agent.id, instruction.id)

    # Cleanup
    client.agentic.enrollments.delete(enrollment.id)
    client.agentic.agents.delete(agent.id)


def test_instructions_list_filtered_by_enrollment() -> None:
    client = new_private_test_tenant_client()

    # Setup
    agent = client.agentic.agents.create(
        name="(Deletable) python-SDK-filter-agent-" + str(uuid.uuid4())
    )

    enrollment = create_and_verify_enrollment(
        client,
        "4000056655665556",
        "sdk-test-filter@example.com",
        agent_ids=[agent.id],
    )

    expires_at = datetime.now(timezone.utc) + timedelta(days=7)

    instruction = client.agentic.agents.instructions.create(
        agent.id,
        enrollment_id=enrollment.id,
        amount={"value": "10.00", "currency": "USD"},
        description="(Deletable) python-SDK filter test",
        expires_at=expires_at,
    )

    # Verify created instruction fields
    assert instruction.id is not None
    assert instruction.enrollment_id == enrollment.id
    assert instruction.status == "pending_verification"
    assert instruction.amount.value == "10.00"
    assert instruction.amount.currency == "USD"
    assert instruction.expires_at is not None
    assert instruction.created_at is not None

    # List with enrollment filter (paginated)
    listed = find_instruction(
        client, agent.id, instruction.id, enrollment_id=enrollment.id
    )
    assert listed is not None
    assert listed.enrollment_id == enrollment.id
    assert listed.amount.value == "10.00"

    # Cleanup
    client.agentic.agents.instructions.delete(agent.id, instruction.id)
    client.agentic.enrollments.delete(enrollment.id)
    client.agentic.agents.delete(agent.id)
