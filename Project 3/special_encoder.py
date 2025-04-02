def encode_integer(n):
    powers = [81, 27, 9, 3, 1]
    coeffs = []

    for p in powers:
        q, r = divmod(n, p)
        if r > p // 2:
            q += 1
        elif r < -p // 2:
            q -= 1
        coeff = q
        if coeff > 1:
            coeff = 1
        elif coeff < -1:
            coeff = -1
        coeffs.append(coeff)
        n -= coeff * p

    return tuple(coeffs)
