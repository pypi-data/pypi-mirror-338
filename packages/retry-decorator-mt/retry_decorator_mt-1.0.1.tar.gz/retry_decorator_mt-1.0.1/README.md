# retry-decorator
A retry python decorator to handle a given set of errors and to retry the decorated function n times if error is in set of errors 

## Installation
`pip install retry-decorator`

## how to use
Here is an exemple on how to use the decorator
``` 
from RetryDecorator import retry

@retry(n_retry=2, tts=0.1)
def func_to_retry(raise_error: bool = True):
    if raise_error:
        print("error is raised")
        
        raise Exception("test exception")
    
    print("error not raised")

    return True

def exemple():
    try:
        func_to_retry()

    except Exception as e:
        print(e)

    func_to_retry(False)

    return

exemple()
``` 
