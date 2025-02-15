import logging
from Hello import Hello_Hi
from Mellow import Hello_Mellow

log_name = "Rahul.log"

def testfunc():
    print("Hello fron Test Func")
    print(__name__)

if __name__ == "__main__":
    testfunc()
    log = logging.getLogger("Rahul")
    log.setLevel(level=logging.DEBUG)

    handler = logging.FileHandler(log_name)
    handler.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)

    log.info("Running Hello Hi")

    try:
        Hello_Hi()
        Hello_Mellow()
    except:
        log.debug()
    else:
        log.info("Function Hello_Hi called")
