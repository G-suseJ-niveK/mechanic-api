from fastapi import APIRouter
from controllers import LogApiResource

router = APIRouter(
    prefix="/api"
)

router.add_api_route("",
  LogApiResource.post,
  methods=['POST'],
  name="Documentacion",
  response_model=str,
  tags=['Root']
)
