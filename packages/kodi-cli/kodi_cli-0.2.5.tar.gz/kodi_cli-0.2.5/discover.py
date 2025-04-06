import requests
from kodi_interface import KodiObj
import cfg
from loguru import logger as LOGGER

def main():

    cfg.configure_logger(log_format=cfg.DEFAULT_CONSOLE_LOGFMT, log_level="INFO")
    for node in range(2,255):
        kodi_host = f'192.168.1.{node}'
        kodi = KodiObj(kodi_host, cfg.port, cfg.kodi_user, cfg.kodi_pw, cfg._json_rpc_loc)
        kodi.check_command("JSONRPC", "Ping")
        print(f'Checking {kodi_host} ', end='',flush=True)
        success = kodi.send_request("JSONRPC", "Ping", None)
        print(success)

if __name__ == "__main__":
    main()
