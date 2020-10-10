from fastapi import FastAPI
from src.client.mongo_db_client import MongoDBClient
from src.bean.product_details import Product

MDClient = MongoDBClient()
app = FastAPI()


@app.get('/')
def index():
    return {'key': 'value'}


@app.post('/new_product')
def new_product(prod: Product):
    MDClient.Collection.insert_one(prod.dict())
    return prod.dict()


@app.get('/products')
def get_product():
    product=MDClient.Collection.find({},{'_id':0,'name':1,'image':1,'price':1,'description':1})
    result = [i for i in product]
    return result


