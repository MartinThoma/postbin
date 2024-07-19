[![PyPI version](https://badge.fury.io/py/postbin.svg)](https://badge.fury.io/py/postbin)
[![Python Support](https://img.shields.io/pypi/pyversions/postbin.svg)](https://pypi.org/project/postbin/)
[![GitHub last commit](https://img.shields.io/github/last-commit/MartinThoma/postbin)](https://github.com/MartinThoma/postbin)

# postbin

A simple Flask webserver to log all incoming requests with their headers and payloads.

## Installation

Install postbin using pip:

```
pip install postbin
```

## Usage

Start the server with

```
$ postbin
```

Then make requests, e.g. with curl:

```
curl -X POST http://127.0.0.1:5000 \
     -H "Content-Type: application/json" \
     -H "Custom-Header: CustomValue" \
     -d '{"key1":"value1","key2":"value2"}'
```

The postbin prints:

```
           Request Headers
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃         Header ┃ Value            ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│           Host │ 127.0.0.1:5000   │
│     User-Agent │ curl/7.68.0      │
│         Accept │ */*              │
│   Content-Type │ application/json │
│  Custom-Header │ CustomValue      │
│ Content-Length │ 33               │
└────────────────┴──────────────────┘
           JSON Payload: {'key1': 'value1', 'key2': 'value2'}
```

## Examples

### A simple GET request

```
curl -i -H "some-header: some-value" localhost:5000/foo/bar?somequery=somevalue
```

Output:

```
[06:31:34] Received Request: GET /foo/bar
        Request Headers
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃      Header ┃ Value          ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│        Host │ localhost:5000 │
│  User-Agent │ curl/7.68.0    │
│      Accept │ */*            │
│ Some-Header │ some-value     │
└─────────────┴────────────────┘
           Data Payload: b''
```

### Multi-dict support of form data

Input:

```
curl -X PUT "http://127.0.0.1:5000/" \
        -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
        -H "X-Test-Header: foo bar" \
        -H "Accept: application/json" \
        --data-raw "key1"="value1" \
        --data-raw "array1[]"="value1" \
        --data-raw "array1[]"="value2" \
        --data-raw "key2"="value1"
```

Output:

```
[06:48:08] Received Request: PUT /
                           Request Headers
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Header ┃ Value                                            ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│           Host │ localhost:5000                                   │
│     User-Agent │ curl/7.68.0                                      │
│   Content-Type │ application/x-www-form-urlencoded; charset=utf-8 │
│  X-Test-Header │ foo bar                                          │
│         Accept │ application/json                                 │
│ Content-Length │ 55                                               │
└────────────────┴──────────────────────────────────────────────────┘
           Form Data:
             key1: value1
             array1[]: value1
             array1[]: value2
             key2: value1
```
