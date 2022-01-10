from fastapi import APIRouter
from controllers import FourierResource

router = APIRouter(
    prefix="/fourier"
)

router.add_api_route("",
  FourierResource.post,
  methods=['POST'],
  name="Documentacion",
  tags=['Root']
)
