def missing_char(str, n):
    if 0 <= n < len(str):
        return str[:n] + str[n+1:]
    return "requete invalide"
