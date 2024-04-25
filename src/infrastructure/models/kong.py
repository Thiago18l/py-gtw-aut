from infrastructure.models import Gateway


class KongGateway(Gateway):

    def __init__(self, conf, log) -> None:
        self.conf = conf
        self.log = log

    def connect(self):
        self.log.info("iniciando conexão Kong")

    def send(self, data):
        self.log.info(f"enviado dados {data}")

    def receive(self):
        self.log.info("recebido dados")
