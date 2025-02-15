import logging

log = logging.getLogger("Rahul")

def Hello_Mellow():
    print("Hello from Mellow Hi")
    log.info("Logged from Mellow.py")


if __name__ == "__main__":
    Hello_Mellow()