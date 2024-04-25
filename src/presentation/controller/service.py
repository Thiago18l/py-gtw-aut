def post_service(payload: dict, header: dict, gtw_url: str, log) -> None:
    log.info("Iniciando request")
    log.debug(f"paylod: {payload}, header: {header}")
    log.debug(f"gateway_url: {gtw_url}")
