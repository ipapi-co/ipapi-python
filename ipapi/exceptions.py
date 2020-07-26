
''' exception classes used by ipapi package '''

class RateLimited(Exception):
    ''' Request was rate limited : HTTP 429 '''
    pass


class AuthorizationFailed(Exception):
    ''' Invalid authorization credentials : HTTP 403 '''
    pass

class PageNotFound(Exception):
    ''' Page not found error : HTTP 404 '''
    pass
