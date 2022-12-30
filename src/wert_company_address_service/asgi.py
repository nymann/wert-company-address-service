from wert_company_address_service.api import Api
from wert_company_address_service.core.config import Config
from wert_company_address_service.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
