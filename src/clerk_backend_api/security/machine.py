from clerk_backend_api.security.types import TokenType, TokenPrefix

MACHINE_TOKEN_PREFIXES = [TokenPrefix.MACHINE_TOKEN_PREFIX, TokenPrefix.OAUTH_TOKEN_PREFIX, TokenPrefix.API_KEY_PREFIX]

def is_machine_token(token: str) -> bool:
    return any(token.startswith(prefix.value) for prefix in MACHINE_TOKEN_PREFIXES)

def get_token_type(token: str) -> TokenType:
    if token.startswith(TokenPrefix.MACHINE_TOKEN_PREFIX.value):
        return TokenType.MACHINE_TOKEN
    elif token.startswith(TokenPrefix.API_KEY_PREFIX.value):
        return TokenType.API_KEY
    elif token.startswith(TokenPrefix.OAUTH_TOKEN_PREFIX.value):
        return TokenType.OAUTH_TOKEN
    else:
        return TokenType.SESSION_TOKEN
