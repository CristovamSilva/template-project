import pathlib
import sys

import uvicorn
from pydantic.error_wrappers import ValidationError

from .settings import settings


def main():
    uvicorn.run(
        "app:create_app",
        factory=True,
        host=settings.host,
        port=settings.port,
    )


if __name__ == "__main__":
    try:
        main()
    except ValidationError as e:
        directory = pathlib.Path(".").absolute()
        print(
            f"The env file is invalid or could not be "
            f"found on the current directory={directory}.\nValidation: {e}",
            file=sys.stderr,
        )
