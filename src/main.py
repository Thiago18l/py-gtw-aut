from config.log.logger import logger
from infrastructure.application.factory import GatewayFactory
import os

conf = "metadados"


def main():
    gateway = GatewayFactory(
        os.environ["GATEWAY_TYPE"],
        conf,
        log,
    )
    instance = gateway.new()
    instance.connect()
    instance.send(
        f"{list(map(lambda n: n ** 2,
                    filter(
                        lambda n: not n % 2, range(10)
                        )))}"
    )


if __name__ == "__main__":
    log = logger(os.environ["LOG_LEVEL"])
    main()
