from project_gen.utils.download import download
from project_gen.utils.generate import generate_api, move_files, replace_import_in_files

service_name = "register_service"
swagger_url = "http://185.185.143.231:8085/register/openapi.json"

download()
generate_api(package_name=service_name, swagger_url=swagger_url)
move_files(package_name=service_name)
replace_import_in_files(directory="clients/http", package_name=service_name)
