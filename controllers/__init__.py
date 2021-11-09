from starlette.endpoints import HTTPEndpoint

# Schemas
from validators.root.request import TemplateApiInsertSchema

# Resources
from resources import full_name

class LogApiResource(HTTPEndpoint):
    @staticmethod
    async def post(item : TemplateApiInsertSchema):
        """
            Esta api insertará una interaccion en dynamoDb
        """
        item = dict(item)
        result = full_name(name2, name3)
        # Envio el item
        print('item', item)

        return result
