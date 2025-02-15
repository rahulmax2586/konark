import logging

log_name = "Hello.log"

log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)

handler = logging.FileHandler(log_name)
handler.setLevel(level=logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

log.addHandler(handler)

def Hello_Hi():
    print("Hello from Hello Hi")
    log.info("Logged from Hello.py")


if __name__ == "__main__":
    Hello_Hi()