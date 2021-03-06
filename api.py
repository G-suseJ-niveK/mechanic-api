from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from configs.environment import Config
from utils.responses import ResponseJson


# Import Exceptions
from exceptions.fast_api_validation import ValidationException
from exceptions.fast_api_custom import CustomException
from exceptions.fast_api import http_exception_handler_custom, http_exception_handler,\
                                validation_exception_handler
# routers Ns API
from routers import router as root

# APP Init
app = FastAPI(
  title=Config.PROJECT_NAME,
  version=Config.PROJECT_API_VERSION,
  debug=Config.DEBUG,
  default_response_class=ResponseJson,
  docs_url= None if Config.DOCS_URL == None else Config.DOCS_URL,
  redoc_url= None if Config.REDOC_URL == None else Config.REDOC_URL
)

app.add_middleware(
  CORSMiddleware,
  allow_origins="*",
  # allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.add_exception_handler(CustomException, http_exception_handler_custom)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)


@root.get('/health-check', tags=['Check'])
def health_check():
  """ Root"""
  return {
    'status': 'ok',
    'version': getattr(Config, 'PROJECT_API_VERSION', '0.1.0'),
    'env': getattr(Config, 'ENV', 'null')
  }

#Add Router
app.include_router(root)
handler = Mangum(app)
