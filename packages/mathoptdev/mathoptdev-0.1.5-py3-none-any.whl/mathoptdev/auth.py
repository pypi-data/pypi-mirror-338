from .token import get_stored_token

MATHOPT_HEADER = 'x-mathopt-api-token';

def get_auth_headers() -> dict[str, str]:
    token = get_stored_token()
    return {MATHOPT_HEADER: token}
