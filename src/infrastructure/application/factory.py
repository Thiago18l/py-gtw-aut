from infrastructure.models.kong import KongGateway
from infrastructure.models.apisix import ApisixGateway


class GatewayFactory:
    def __init__(self, type: object, conf: dict, log) -> None:
        self.type = type
        self.conf = conf
        self.log = log

    def new(self) -> object:
        if self.type == "APISIX":
            return ApisixGateway(self.conf, self.log)
        elif self.type == "KONG":
            return KongGateway(self.conf, self.log)
        else:
            self.log.error(f"Gateway type: {type}")
            raise ValueError(f"Tipo de gateway inválido: {type}")
