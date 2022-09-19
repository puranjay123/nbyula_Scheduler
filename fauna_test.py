from faunadb import query as q  
from faunadb.objects import Ref   
from faunadb.client import FaunaClient  

client = FaunaClient(secret="fnAEwyz9miACS-JIP4ljPrO0D506SLYVf_iIOrVW")  

indexes = client.query(q.paginate(q.indexes()))  

print(indexes)