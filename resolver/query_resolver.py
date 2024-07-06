from ariadne import QueryType
from flask import Response

query = QueryType()

@query.field('')
def resolver_hello_world():
    return 'Hello World !'