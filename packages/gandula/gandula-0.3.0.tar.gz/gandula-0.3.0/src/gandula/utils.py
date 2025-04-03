from contextlib import contextmanager
from time import time


@contextmanager
def performance_logging(description: str, counter: int | None = None, logger=None):
    start = time()
    try:
        yield
    finally:
        took = (time() - start) * 1000
        extra = ''
        if counter is not None:
            extra = f' ({int(counter / took * 1000)}items/sec)'

        unit = 'ms'
        if took < 0.1:
            took *= 1000
            unit = 'us'

        msg = f'{description} took: {took:.2f}{unit} {extra}'
        if logger:
            logger.info(msg)
        else:
            print(msg)
