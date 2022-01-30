from starlette.endpoints import HTTPEndpoint
from exceptions.fast_api_custom import CustomException

# Schemas
from validators.root.request import TemplateApiInsertSchema

# Resources
from resources import get_alert, get_fourier

class FourierResource(HTTPEndpoint):
    @staticmethod
    async def post(item: TemplateApiInsertSchema):
        """
            Esta api insertará una interaccion en dynamoDb
        """
        try:
            if len(item.data) <= 0:
                raise CustomException(status_code=410, detail='No se encontro data')

            value = item.data[0]
            value_amp = {}
            for amp in value:
                amp_tranf = amp.lower().strip()
                if amp_tranf == 'valor':
                    value_amp['valor'] = amp

            if value_amp.get('valor') is None:
                raise CustomException(status_code=410, detail='No se encontro data')

            data = list(map(lambda x: x[value_amp['valor']]  , item.data))

            return get_fourier(time= item.time,
                        count=item.count,
                        data= data)

        except Exception as e:
            print('error', e)
            raise CustomException(status_code=e.status_code, detail=e.detail) from e
