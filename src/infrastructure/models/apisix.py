from infrastructure.models import Gateway


class ApisixGateway(Gateway):

    def __init__(self, conf, log) -> None:
        self.conf = conf
        self.log = log

    def connect(self):
        self.log.info("iniciando conexão apisix")

    def send(self, data):
        self.log.info(f"enviado dados {data}")

    def receive(self):
        self.log.info("recebido dados")
