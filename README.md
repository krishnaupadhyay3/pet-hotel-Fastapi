---
title: PetStore v0.1.0
language_tabs:
  - python: Python
  - shell: Shell
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->
# an application for managing a pet hotel

The app support 3 roles: customer, staff and manager accessible through a login page.

When logged in a customer can see a list of his pets and, if they are checked in, see in which room they are staying. Also, he should be able to create pets but only edit or delete pets that are *not* checked in.

Staff and managers should be able to invite a customer to the application by email address; the system should then send an invitation message automatically, prompting the user to complete the registration. You're free to choose whatever transactional email provider you prefer.

The staff should be able to search, create and edit pets as well as check them in and out. The staff should also be able to see if a pet has an owner.

A manager should be able to do all the operations the staff can, plus move pets to other rooms as well as delete them.

When a customer fails to log in three times in a row, his or her account should be blocked automatically, and only staff and managers should be able to unblock it.


# Installation 
  change the .env values in pethotel directory or can change value in docker-compose.yml file
  Run in the Default folder

```sh 
  docker-compose up -d
```

<h1 id="fastapi">PetStore</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

- oAuth2 authentication. 

    - Flow: password

    - Token URL = [/v1/token](/v1/token)

|Scope|Scope Description|
|---|---|

<h1 id="fastapi-default">Default</h1>

## login_for_access_token_v1_token_post

<a id="opIdlogin_for_access_token_v1_token_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

r = requests.post('/v1/token', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X POST /v1/token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json'

```

`POST /v1/token`

*Login For Access Token*

> Body parameter

```yaml
grant_type: string
username: string
password: string
scope: ""
client_id: string
client_secret: string

```

<h3 id="login_for_access_token_v1_token_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_login_for_access_token_v1_token_post](#schemabody_login_for_access_token_v1_token_post)|true|none|

> Example responses

> 200 Response

```json
{
  "access_token": "string",
  "token_type": "string"
}
```

<h3 id="login_for_access_token_v1_token_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Token](#schematoken)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## create_common_user_v1_register_post

<a id="opIdcreate_common_user_v1_register_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/v1/register', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X POST /v1/register \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /v1/register`

*Create Common User*

> Body parameter

```json
{
  "username": "string",
  "email": "string",
  "full_name": "string",
  "password": "string"
}
```

<h3 id="create_common_user_v1_register_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserCommon](#schemausercommon)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="create_common_user_v1_register_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="create_common_user_v1_register_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## list_pet_v1_pet_get

<a id="opIdlist_pet_v1_pet_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v1/pet', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X GET /v1/pet \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`GET /v1/pet`

*List Pet*

<h3 id="list_pet_v1_pet_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|skip|query|integer|false|none|
|limit|query|integer|false|none|

> Example responses

> 200 Response

```json
[
  {
    "pet_name": "string",
    "checked_in": "string",
    "room": "string"
  }
]
```

<h3 id="list_pet_v1_pet_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="list_pet_v1_pet_get-responseschema">Response Schema</h3>

Status Code **200**

*Response List Pet V1 Pet Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response List Pet V1 Pet Get|[[PetList](#schemapetlist)]|false|none|none|
|» PetList|[PetList](#schemapetlist)|false|none|none|
|»» pet_name|string|true|none|none|
|»» checked_in|string|true|none|none|
|»» room|string|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## pet_create_v1_pet_post

<a id="opIdpet_create_v1_pet_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v1/pet', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X POST /v1/pet \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`POST /v1/pet`

*Pet Create*

> Body parameter

```json
{
  "pet_name": "string"
}
```

<h3 id="pet_create_v1_pet_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PetClass](#schemapetclass)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="pet_create_v1_pet_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="pet_create_v1_pet_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## pet_info_v1_pet__pet_id__get

<a id="opIdpet_info_v1_pet__pet_id__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v1/pet/{pet_id}', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X GET /v1/pet/{pet_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`GET /v1/pet/{pet_id}`

*Pet Info*

<h3 id="pet_info_v1_pet__pet_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pet_id|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="pet_info_v1_pet__pet_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="pet_info_v1_pet__pet_id__get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## pet_update_v1_pet__pet_id__put

<a id="opIdpet_update_v1_pet__pet_id__put"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.put('/v1/pet/{pet_id}', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X PUT /v1/pet/{pet_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`PUT /v1/pet/{pet_id}`

*Pet Update*

> Body parameter

```json
{
  "pet_name": "string",
  "checked_in": false,
  "room": "string",
  "deleted": false,
  "owner": "string"
}
```

<h3 id="pet_update_v1_pet__pet_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pet_id|path|string|true|none|
|body|body|[PetInDB](#schemapetindb)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="pet_update_v1_pet__pet_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="pet_update_v1_pet__pet_id__put-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## pet_delete_v1_pet__pet_id__delete

<a id="opIdpet_delete_v1_pet__pet_id__delete"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v1/pet/{pet_id}', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X DELETE /v1/pet/{pet_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`DELETE /v1/pet/{pet_id}`

*Pet Delete*

<h3 id="pet_delete_v1_pet__pet_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pet_id|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="pet_delete_v1_pet__pet_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="pet_delete_v1_pet__pet_id__delete-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## user_invite_v1_invite_post

<a id="opIduser_invite_v1_invite_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v1/invite', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X POST /v1/invite \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`POST /v1/invite`

*User Invite*

> Body parameter

```json
{
  "email": "user@example.com"
}
```

<h3 id="user_invite_v1_invite_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[InviteEmail](#schemainviteemail)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="user_invite_v1_invite_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="user_invite_v1_invite_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## unblock_user_v1_unblock__post

<a id="opIdunblock_user_v1_unblock__post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v1/unblock/', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X POST /v1/unblock/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`POST /v1/unblock/`

*Unblock User*

> Body parameter

```json
{
  "email": "user@example.com"
}
```

<h3 id="unblock_user_v1_unblock__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[InviteEmail](#schemainviteemail)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="unblock_user_v1_unblock__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="unblock_user_v1_unblock__post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## create_user_v1_rootuser_post

<a id="opIdcreate_user_v1_rootuser_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v1/rootuser', headers = headers)

print(r.json())

```

```shell
# You can also use wget
curl -X POST /v1/rootuser \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

`POST /v1/rootuser`

*Create User*

> Body parameter

```json
{
  "username": "string",
  "email": "string",
  "full_name": "string",
  "password": "string",
  "roles": "customer"
}
```

<h3 id="create_user_v1_rootuser_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserInput](#schemauserinput)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="create_user_v1_rootuser_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="create_user_v1_rootuser_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

# Schemas

<h2 id="tocS_Body_login_for_access_token_v1_token_post">Body_login_for_access_token_v1_token_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_login_for_access_token_v1_token_post"></a>
<a id="schema_Body_login_for_access_token_v1_token_post"></a>
<a id="tocSbody_login_for_access_token_v1_token_post"></a>
<a id="tocsbody_login_for_access_token_v1_token_post"></a>

```json
{
  "grant_type": "string",
  "username": "string",
  "password": "string",
  "scope": "",
  "client_id": "string",
  "client_secret": "string"
}

```

Body_login_for_access_token_v1_token_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|grant_type|string|false|none|none|
|username|string|true|none|none|
|password|string|true|none|none|
|scope|string|false|none|none|
|client_id|string|false|none|none|
|client_secret|string|false|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_InviteEmail">InviteEmail</h2>
<!-- backwards compatibility -->
<a id="schemainviteemail"></a>
<a id="schema_InviteEmail"></a>
<a id="tocSinviteemail"></a>
<a id="tocsinviteemail"></a>

```json
{
  "email": "user@example.com"
}

```

InviteEmail

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string(email)|true|none|none|

<h2 id="tocS_PetClass">PetClass</h2>
<!-- backwards compatibility -->
<a id="schemapetclass"></a>
<a id="schema_PetClass"></a>
<a id="tocSpetclass"></a>
<a id="tocspetclass"></a>

```json
{
  "pet_name": "string"
}

```

PetClass

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pet_name|string|true|none|none|

<h2 id="tocS_PetInDB">PetInDB</h2>
<!-- backwards compatibility -->
<a id="schemapetindb"></a>
<a id="schema_PetInDB"></a>
<a id="tocSpetindb"></a>
<a id="tocspetindb"></a>

```json
{
  "pet_name": "string",
  "checked_in": false,
  "room": "string",
  "deleted": false,
  "owner": "string"
}

```

PetInDB

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pet_name|string|true|none|none|
|checked_in|boolean|false|none|none|
|room|string|false|none|none|
|deleted|boolean|false|none|none|
|owner|string|true|none|none|

<h2 id="tocS_PetList">PetList</h2>
<!-- backwards compatibility -->
<a id="schemapetlist"></a>
<a id="schema_PetList"></a>
<a id="tocSpetlist"></a>
<a id="tocspetlist"></a>

```json
{
  "pet_name": "string",
  "checked_in": "string",
  "room": "string"
}

```

PetList

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pet_name|string|true|none|none|
|checked_in|string|true|none|none|
|room|string|false|none|none|

<h2 id="tocS_Token">Token</h2>
<!-- backwards compatibility -->
<a id="schematoken"></a>
<a id="schema_Token"></a>
<a id="tocStoken"></a>
<a id="tocstoken"></a>

```json
{
  "access_token": "string",
  "token_type": "string"
}

```

Token

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_token|string|true|none|none|
|token_type|string|true|none|none|

<h2 id="tocS_UserCommon">UserCommon</h2>
<!-- backwards compatibility -->
<a id="schemausercommon"></a>
<a id="schema_UserCommon"></a>
<a id="tocSusercommon"></a>
<a id="tocsusercommon"></a>

```json
{
  "username": "string",
  "email": "string",
  "full_name": "string",
  "password": "string"
}

```

UserCommon

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|none|none|
|email|string|true|none|none|
|full_name|string|false|none|none|
|password|string|true|none|none|

<h2 id="tocS_UserInput">UserInput</h2>
<!-- backwards compatibility -->
<a id="schemauserinput"></a>
<a id="schema_UserInput"></a>
<a id="tocSuserinput"></a>
<a id="tocsuserinput"></a>

```json
{
  "username": "string",
  "email": "string",
  "full_name": "string",
  "password": "string",
  "roles": "customer"
}

```

UserInput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|none|none|
|email|string|true|none|none|
|full_name|string|false|none|none|
|password|string|true|none|none|
|roles|string|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[string]|true|none|none|
|msg|string|true|none|none|
|type|string|true|none|none|
