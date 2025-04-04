from typing import Iterable, Callable, Type
from time import sleep

import logging

def retry(
    n_retry: int = 1,
    exceptions: Iterable[Type[(Exception,)]]=(Exception,),
    tts: float = 0
):
    def retry_decorator(func: Callable[[any], any]):
        def retry_wrapper(*args, **kwargs):
            retry_logger = logging.getLogger(__name__)
            exceptions_set = {e for e in exceptions}

            for i in range(n_retry + 1):
                if i > 0:
                    retry_logger.debug("retry {i}")

                try:
                    result = func(*args, **kwargs)

                    return result

                except tuple(exceptions_set) as e:
                    retry_logger.debug(e)

                    if i < n_retry:
                        pass

                    else:
                        raise e

                sleep(tts)

        return retry_wrapper

    return retry_decorator

