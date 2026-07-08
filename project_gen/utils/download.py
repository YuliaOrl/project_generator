import os
import platform
import requests
import shutil
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

OPENAPI_GENERATOR = "openapi-generator-cli-7.23.0.jar"


def download() -> None:
    url = "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.23.0/openapi-generator-cli-7.23.0.jar"
    target_dir = ".venv/Scripts" if platform.system() == "Windows" else ".venv/bin"

    with requests.get(url, stream=True, timeout=100, verify=False) as response:
        response.raise_for_status()
        file_name = OPENAPI_GENERATOR
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        if platform.system() != "Windows":
            os.chmod(file_name, 0o755)

    shutil.move(file_name, f"{target_dir}/{file_name}")


def init() -> None:
    target_dir = ".venv/Scripts" if platform.system() == "Windows" else ".venv/bin"
    if not os.path.exists(f"{target_dir}/{OPENAPI_GENERATOR}"):
        download()

    print(f"Downloaded {OPENAPI_GENERATOR}")

