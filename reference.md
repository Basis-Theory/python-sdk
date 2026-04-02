# Reference
## Applications
<details><summary><code>client.applications.<a href="src/basis_theory/applications/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.applications.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/basis_theory/applications/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.applications.create(
    name="name",
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.Optional[typing.Sequence[AccessRule]]` 
    
</dd>
</dl>

<dl>
<dd>

**create_key:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/basis_theory/applications/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.applications.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/basis_theory/applications/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.applications.update(
    id="id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.Optional[typing.Sequence[AccessRule]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/basis_theory/applications/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.applications.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/basis_theory/applications/client.py">get_by_key</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.applications.get_by_key()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplicationKeys
<details><summary><code>client.application_keys.<a href="src/basis_theory/application_keys/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.application_keys.list(
    id_="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.application_keys.<a href="src/basis_theory/application_keys/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.application_keys.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.application_keys.<a href="src/basis_theory/application_keys/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.application_keys.get(
    id="id",
    key_id="keyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.application_keys.<a href="src/basis_theory/application_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.application_keys.delete(
    id="id",
    key_id="keyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplicationTemplates
<details><summary><code>client.application_templates.<a href="src/basis_theory/application_templates/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.application_templates.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.application_templates.<a href="src/basis_theory/application_templates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.application_templates.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay
<details><summary><code>client.apple_pay.<a href="src/basis_theory/apple_pay/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**apple_payment_data:** `typing.Optional[ApplePayMethodToken]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_registration_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.<a href="src/basis_theory/apple_pay/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.<a href="src/basis_theory/apple_pay/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GooglePay
<details><summary><code>client.google_pay.<a href="src/basis_theory/google_pay/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_payment_data:** `typing.Optional[GooglePayMethodToken]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_registration_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.google_pay.<a href="src/basis_theory/google_pay/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.google_pay.<a href="src/basis_theory/google_pay/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/basis_theory/documents/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.documents.upload()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CreateDocumentRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/basis_theory/documents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.documents.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/basis_theory/documents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.documents.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tokens
<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">detokenize</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tokens.detokenize(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">tokenize</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tokens.tokenize(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tokens.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tokens.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tokens.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `typing.Optional[UpdatePrivacy]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**search_indexes:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**fingerprint_expression:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mask:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deduplicate_token:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**containers:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tokens.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**encrypted:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `typing.Optional[Privacy]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**search_indexes:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**fingerprint_expression:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mask:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**deduplicate_token:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**containers:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**token_intent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">list_v2</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.tokens.list_v2()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**container:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fingerprint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/basis_theory/tokens/client.py">search_v2</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.tokens.search_v2()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Enrichments
<details><summary><code>client.enrichments.<a href="src/basis_theory/enrichments/client.py">bank_account_verify</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.enrichments.bank_account_verify(
    token_id="token_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.enrichments.<a href="src/basis_theory/enrichments/client.py">getcarddetails</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.enrichments.getcarddetails(
    bin="bin",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bin:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Keys
<details><summary><code>client.keys.<a href="src/basis_theory/keys/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.keys.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/basis_theory/keys/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.keys.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/basis_theory/keys/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.keys.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/basis_theory/keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.keys.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Logs
<details><summary><code>client.logs.<a href="src/basis_theory/logs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.logs.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/basis_theory/logs/client.py">get_entity_types</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.logs.get_entity_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NetworkTokens
<details><summary><code>client.network_tokens.<a href="src/basis_theory/network_tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.network_tokens.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Optional[Card]` 
    
</dd>
</dl>

<dl>
<dd>

**token_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token_intent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cardholder_info:** `typing.Optional[CardholderInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_tokens.<a href="src/basis_theory/network_tokens/client.py">cryptogram</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.network_tokens.cryptogram(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_tokens.<a href="src/basis_theory/network_tokens/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.network_tokens.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_tokens.<a href="src/basis_theory/network_tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.network_tokens.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_tokens.<a href="src/basis_theory/network_tokens/client.py">suspend</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.network_tokens.suspend(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_tokens.<a href="src/basis_theory/network_tokens/client.py">resume</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.network_tokens.resume(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissions
<details><summary><code>client.permissions.<a href="src/basis_theory/permissions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.permissions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Proxies
<details><summary><code>client.proxies.<a href="src/basis_theory/proxies/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.proxies.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/basis_theory/proxies/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.proxies.create(
    name="name",
    destination_url="destination_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**destination_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_reactor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**response_reactor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_transform:** `typing.Optional[ProxyTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**response_transform:** `typing.Optional[ProxyTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**request_transforms:** `typing.Optional[typing.Sequence[ProxyTransform]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_transforms:** `typing.Optional[typing.Sequence[ProxyTransform]]` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[Application]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**require_auth:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_detokenization:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/basis_theory/proxies/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.proxies.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/basis_theory/proxies/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.proxies.update(
    id="id",
    name="name",
    destination_url="destination_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**destination_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_reactor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**response_reactor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_transform:** `typing.Optional[ProxyTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**response_transform:** `typing.Optional[ProxyTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**request_transforms:** `typing.Optional[typing.Sequence[ProxyTransform]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_transforms:** `typing.Optional[typing.Sequence[ProxyTransform]]` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[Application]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**require_auth:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_detokenization:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/basis_theory/proxies/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.proxies.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxies.<a href="src/basis_theory/proxies/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.proxies.patch(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_transform:** `typing.Optional[ProxyTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**response_transform:** `typing.Optional[ProxyTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**request_transforms:** `typing.Optional[typing.Sequence[ProxyTransform]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_transforms:** `typing.Optional[typing.Sequence[ProxyTransform]]` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[Application]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**require_auth:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_detokenization:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reactors
<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.reactors.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.create(
    name="name",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[Application]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**runtime:** `typing.Optional[Runtime]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.update(
    id="id",
    name="name",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[Application]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**runtime:** `typing.Optional[Runtime]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.patch(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[Application]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**runtime:** `typing.Optional[Runtime]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">react</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.react(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reactors.<a href="src/basis_theory/reactors/client.py">react_async</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.react_async(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/basis_theory/roles/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.roles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sessions
<details><summary><code>client.sessions.<a href="src/basis_theory/sessions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.sessions.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/basis_theory/sessions/client.py">authorize</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.sessions.authorize(
    nonce="nonce",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nonce:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.Optional[typing.Sequence[AccessRule]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TokenIntents
<details><summary><code>client.token_intents.<a href="src/basis_theory/token_intents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.token_intents.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token_intents.<a href="src/basis_theory/token_intents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.token_intents.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token_intents.<a href="src/basis_theory/token_intents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.token_intents.create(
    type="x",
    data={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/basis_theory/webhooks/client.py">ping</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simple endpoint that can be utilized to verify the application is running
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.ping()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/basis_theory/webhooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/basis_theory/webhooks/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a new webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.update(
    id="id",
    name="webhook-update",
    url="http://www.example.com",
    events=["token:created"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the webhook
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL to which the webhook will send events
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Sequence[str]` — An array of event types that the webhook will listen for
    
</dd>
</dl>

<dl>
<dd>

**notify_email:** `typing.Optional[str]` — The email address to use for management notification events. Ie: webhook disabled
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/basis_theory/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a new webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/basis_theory/webhooks/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the configured webhooks
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/basis_theory/webhooks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.create(
    name="webhook-create",
    url="http://www.example.com",
    events=["token:created"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the webhook
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL to which the webhook will send events
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Sequence[str]` — An array of event types that the webhook will listen for
    
</dd>
</dl>

<dl>
<dd>

**notify_email:** `typing.Optional[str]` — The email address to use for management notification events. Ie: webhook disabled
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AccountUpdater Jobs
<details><summary><code>client.account_updater.jobs.<a href="src/basis_theory/account_updater/jobs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the account updater batch job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.account_updater.jobs.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_updater.jobs.<a href="src/basis_theory/account_updater/jobs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of account updater batch jobs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.account_updater.jobs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**size:** `typing.Optional[int]` — The maximum number of jobs to return
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_updater.jobs.<a href="src/basis_theory/account_updater/jobs/client.py">create</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the created account updater batch job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.account_updater.jobs.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AccountUpdater RealTime
<details><summary><code>client.account_updater.real_time.<a href="src/basis_theory/account_updater/real_time/client.py">invoke</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the update result
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.account_updater.real_time.invoke(
    token_id="9a420b15-ddfe-4793-9466-48f53520e47c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token_id:** `str` — Card Token identifier
    
</dd>
</dl>

<dl>
<dd>

**expiration_year:** `typing.Optional[int]` — The 4-digit expiration year of the account number. Not required if the card token already stores this value.
    
</dd>
</dl>

<dl>
<dd>

**expiration_month:** `typing.Optional[int]` — The 2-digit expiration month of the account number. Not required if the card token already stores this value.
    
</dd>
</dl>

<dl>
<dd>

**deduplicate_token:** `typing.Optional[bool]` — Whether deduplication should be enabled when creating the new token. Uses the value of the Deduplicate Tokens setting on the tenant if not set.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Tenant merchant identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agentic Agents
<details><summary><code>client.agentic.agents.<a href="src/basis_theory/agentic/agents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enrollment_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**instance_details:** `typing.Optional[InstanceDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.<a href="src/basis_theory/agentic/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.get(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.<a href="src/basis_theory/agentic/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.delete(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.<a href="src/basis_theory/agentic/agents/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.update(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enrollment_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**instance_details:** `typing.Optional[InstanceDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agentic Enrollments
<details><summary><code>client.agentic.enrollments.<a href="src/basis_theory/agentic/enrollments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all enrollments for the current tenant with cursor-based pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from a previous response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.<a href="src/basis_theory/agentic/enrollments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enroll a card token with a card network (Visa or Mastercard).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory, Consumer

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.create(
    token_id="token_id",
    consumer=Consumer(
        email="email",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**consumer:** `Consumer` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Single agent ID (mutually exclusive with agent_ids)
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Sequence[str]]` — Multiple agent IDs (mutually exclusive with agent_id)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.<a href="src/basis_theory/agentic/enrollments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.get(
    enrollment_id="enrollment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.<a href="src/basis_theory/agentic/enrollments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-deletes the enrollment by marking its status as deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.delete(
    enrollment_id="enrollment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.<a href="src/basis_theory/agentic/enrollments/client.py">retry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retry enrolling a card that previously failed. Only failed enrollments can be retried.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.retry(
    enrollment_id="enrollment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agentic Agents Instructions
<details><summary><code>client.agentic.agents.instructions.<a href="src/basis_theory/agentic/agents/instructions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all purchase instructions for an agent with cursor-based pagination and optional enrollment filter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.list(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enrollment_id:** `typing.Optional[str]` — Filter instructions by enrollment ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from a previous response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.instructions.<a href="src/basis_theory/agentic/agents/instructions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new payment instruction for an agent, linked to an enrollment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from basis_theory import Amount, BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.create(
    agent_id="agent_id",
    enrollment_id="enrollment_id",
    amount=Amount(
        value="100.00",
    ),
    description="description",
    expires_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**assurance_data:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**recurring:** `typing.Optional[Recurring]` 
    
</dd>
</dl>

<dl>
<dd>

**instance_details:** `typing.Optional[InstanceDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.instructions.<a href="src/basis_theory/agentic/agents/instructions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.get(
    agent_id="agent_id",
    instruction_id="instruction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instruction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.instructions.<a href="src/basis_theory/agentic/agents/instructions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.delete(
    agent_id="agent_id",
    instruction_id="instruction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instruction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.instructions.<a href="src/basis_theory/agentic/agents/instructions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.update(
    agent_id="agent_id",
    instruction_id="instruction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instruction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[Amount]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agentic Agents Instructions Credentials
<details><summary><code>client.agentic.agents.instructions.credentials.<a href="src/basis_theory/agentic/agents/instructions/credentials/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve payment credentials (card number, expiration, CVC) for a purchase instruction.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory, Merchant

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.credentials.create(
    agent_id="agent_id",
    instruction_id="instruction_id",
    merchant=Merchant(
        name="name",
        url="url",
        country_code="country_code",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instruction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**merchant:** `Merchant` 
    
</dd>
</dl>

<dl>
<dd>

**products:** `typing.Optional[typing.Sequence[Product]]` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[Amount]` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_method:** `typing.Optional[DeliveryMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[ShippingAddress]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agentic Agents Instructions Verify
<details><summary><code>client.agentic.agents.instructions.verify.<a href="src/basis_theory/agentic/agents/instructions/verify/client.py">start</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate cardholder verification for a purchase instruction that requires it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory, DeviceContext

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.verify.start(
    agent_id="agent_id",
    instruction_id="instruction_id",
    device_context=DeviceContext(
        screen_height=1,
        screen_width=1,
        user_agent_string="user_agent_string",
        language_code="language_code",
        time_zone="time_zone",
        java_script_enabled=True,
        client_device_id="client_device_id",
        client_reference_id="client_reference_id",
        platform_type="WEB",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instruction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_context:** `DeviceContext` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.agents.instructions.verify.<a href="src/basis_theory/agentic/agents/instructions/verify/client.py">passkey</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit passkey/FIDO assertion data to complete instruction verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.agents.instructions.verify.passkey(
    agent_id="agent_id",
    instruction_id="instruction_id",
    assurance_data={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instruction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**assurance_data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Visa format (identifier, dfp_session_id, fido_assertion_data) or Mastercard format (flexible object)
    
</dd>
</dl>

<dl>
<dd>

**src_correlation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**flow_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agentic Enrollments Verify
<details><summary><code>client.agentic.enrollments.verify.<a href="src/basis_theory/agentic/enrollments/verify/client.py">start</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates the cardholder verification flow for a pending enrollment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory, DeviceContext

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.verify.start(
    enrollment_id="enrollment_id",
    device_context=DeviceContext(
        screen_height=1,
        screen_width=1,
        user_agent_string="user_agent_string",
        language_code="language_code",
        time_zone="time_zone",
        java_script_enabled=True,
        client_device_id="client_device_id",
        client_reference_id="client_reference_id",
        platform_type="WEB",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_context:** `DeviceContext` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.verify.<a href="src/basis_theory/agentic/enrollments/verify/client.py">method</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Choose the OTP delivery method (SMS, email, etc.) for enrollment verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.verify.method(
    enrollment_id="enrollment_id",
    method_id="method_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.verify.<a href="src/basis_theory/agentic/enrollments/verify/client.py">otp</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit the one-time password received by the cardholder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.verify.otp(
    enrollment_id="enrollment_id",
    otp_code="otp_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**otp_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agentic.enrollments.verify.<a href="src/basis_theory/agentic/enrollments/verify/client.py">complete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete the verification flow (e.g. after passkey creation). Body is optional — Visa sends empty body, Mastercard sends assurance_data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.agentic.enrollments.verify.complete(
    enrollment_id="enrollment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**assurance_data:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**src_correlation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay Merchant
<details><summary><code>client.apple_pay.merchant.<a href="src/basis_theory/apple_pay/merchant/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.merchant.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.merchant.<a href="src/basis_theory/apple_pay/merchant/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.merchant.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.merchant.<a href="src/basis_theory/apple_pay/merchant/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.merchant.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay Domain
<details><summary><code>client.apple_pay.domain.<a href="src/basis_theory/apple_pay/domain/client.py">deregister</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.domain.deregister(
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.domain.<a href="src/basis_theory/apple_pay/domain/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.domain.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.domain.<a href="src/basis_theory/apple_pay/domain/client.py">register</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.domain.register(
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.domain.<a href="src/basis_theory/apple_pay/domain/client.py">register_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.domain.register_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domains:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay Session
<details><summary><code>client.apple_pay.session.<a href="src/basis_theory/apple_pay/session/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.session.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**validation_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_registration_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay Merchant Certificates
<details><summary><code>client.apple_pay.merchant.certificates.<a href="src/basis_theory/apple_pay/merchant/certificates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.merchant.certificates.get(
    merchant_id="merchantId",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.merchant.certificates.<a href="src/basis_theory/apple_pay/merchant/certificates/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.merchant.certificates.delete(
    merchant_id="merchantId",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apple_pay.merchant.certificates.<a href="src/basis_theory/apple_pay/merchant/certificates/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.apple_pay.merchant.certificates.create(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_certificate_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_certificate_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_processor_certificate_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_processor_certificate_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents Data
<details><summary><code>client.documents.data.<a href="src/basis_theory/documents/data/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.documents.data.get(
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GooglePay Merchant
<details><summary><code>client.google_pay.merchant.<a href="src/basis_theory/google_pay/merchant/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.merchant.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.google_pay.merchant.<a href="src/basis_theory/google_pay/merchant/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.merchant.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.google_pay.merchant.<a href="src/basis_theory/google_pay/merchant/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.merchant.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GooglePay Merchant Certificates
<details><summary><code>client.google_pay.merchant.certificates.<a href="src/basis_theory/google_pay/merchant/certificates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.merchant.certificates.get(
    merchant_id="merchantId",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.google_pay.merchant.certificates.<a href="src/basis_theory/google_pay/merchant/certificates/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.merchant.certificates.delete(
    merchant_id="merchantId",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.google_pay.merchant.certificates.<a href="src/basis_theory/google_pay/merchant/certificates/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.google_pay.merchant.certificates.create(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_certificate_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_certificate_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reactors Results
<details><summary><code>client.reactors.results.<a href="src/basis_theory/reactors/results/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.reactors.results.get(
    id="id",
    request_id="requestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants SecurityContact
<details><summary><code>client.tenants.security_contact.<a href="src/basis_theory/tenants/security_contact/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.security_contact.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.security_contact.<a href="src/basis_theory/tenants/security_contact/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.security_contact.update(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants Connections
<details><summary><code>client.tenants.connections.<a href="src/basis_theory/tenants/connections/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory, TenantConnectionOptions

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.connections.create(
    strategy="strategy",
    options=TenantConnectionOptions(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**strategy:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `TenantConnectionOptions` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.connections.<a href="src/basis_theory/tenants/connections/client.py">delete</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.connections.delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants Invitations
<details><summary><code>client.tenants.invitations.<a href="src/basis_theory/tenants/invitations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
response = client.tenants.invitations.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status:** `typing.Optional[TenantInvitationStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.invitations.<a href="src/basis_theory/tenants/invitations/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.invitations.create(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.invitations.<a href="src/basis_theory/tenants/invitations/client.py">resend</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.invitations.resend(
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invitation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.invitations.<a href="src/basis_theory/tenants/invitations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.invitations.get(
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invitation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.invitations.<a href="src/basis_theory/tenants/invitations/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.invitations.delete(
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invitation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants Members
<details><summary><code>client.tenants.members.<a href="src/basis_theory/tenants/members/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.members.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.members.<a href="src/basis_theory/tenants/members/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.members.update(
    member_id="memberId",
    role="role",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.members.<a href="src/basis_theory/tenants/members/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.members.delete(
    member_id="memberId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants Owner
<details><summary><code>client.tenants.owner.<a href="src/basis_theory/tenants/owner/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.owner.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants Self
<details><summary><code>client.tenants.self_.<a href="src/basis_theory/tenants/self_/client.py">get_usage_reports</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.self_.get_usage_reports()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.self_.<a href="src/basis_theory/tenants/self_/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.self_.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.self_.<a href="src/basis_theory/tenants/self_/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.self_.update(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.self_.<a href="src/basis_theory/tenants/self_/client.py">delete</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.tenants.self_.delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Threeds Sessions
<details><summary><code>client.threeds.sessions.<a href="src/basis_theory/threeds/sessions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.threeds.sessions.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pan:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token_intent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**web_challenge_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_info:** `typing.Optional[ThreeDsDeviceInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**authentication_request:** `typing.Optional[AuthenticateThreeDsSessionRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**callback_urls:** `typing.Optional[ThreeDsCallbackUrls]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threeds.sessions.<a href="src/basis_theory/threeds/sessions/client.py">authenticate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.threeds.sessions.authenticate(
    session_id="sessionId",
    authentication_category="authentication_category",
    authentication_type="authentication_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authentication_category:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authentication_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**card_brand:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**challenge_preference:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_decoupled_challenge:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**decoupled_challenge_max_time:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**purchase_info:** `typing.Optional[ThreeDsPurchaseInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_info:** `typing.Optional[ThreeDsMerchantInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**requestor_info:** `typing.Optional[ThreeDsRequestorInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**cardholder_info:** `typing.Optional[ThreeDsCardholderInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**broadcast_info:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**message_extensions:** `typing.Optional[typing.Sequence[ThreeDsMessageExtension]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threeds.sessions.<a href="src/basis_theory/threeds/sessions/client.py">get_challenge_result</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.threeds.sessions.get_challenge_result(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threeds.sessions.<a href="src/basis_theory/threeds/sessions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.threeds.sessions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks Events
<details><summary><code>client.webhooks.events.<a href="src/basis_theory/webhooks/events/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a list of available event types
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from basis_theory import BasisTheory

client = BasisTheory(
    correlation_id="YOUR_CORRELATION_ID",
    api_key="YOUR_API_KEY",
)
client.webhooks.events.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

