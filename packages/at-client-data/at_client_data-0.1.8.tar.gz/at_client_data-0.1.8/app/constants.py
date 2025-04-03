from enum import Enum

class ErrorCode(str, Enum):
    # Success
    SUCCESS = "SUCCESS"
    
    ## Server Errors (SRV)
    SRV_UNKNOWN_ERROR = "SRV_UNKNOWN_ERROR"
    
    ## Resource Errors (RSC)
    RSC_NOT_FOUND = "RSC_NOT_FOUND"
    RSC_EMPTY_RESULT = "RSC_EMPTY_RESULT"
    
    ## Input Errors (INP)
    INP_INVALID_REQUEST = "INP_INVALID_REQUEST"
    
    ## External Service Errors (EXT)
    EXT_SERVICE_UNAVAILABLE = "EXT_SERVICE_UNAVAILABLE"