def encode_integer(n):
    powers = [81, 27, 9, 3, 1]
    coeffs = []
    steps = []  # List to store the steps

    for p in powers:
        q, r = divmod(n, p)
        step = f"Dividing {n} by {p}: quotient = {q}, remainder = {r}"
        steps.append(step)

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

        # Showing the updated n after the coefficient adjustment
        n -= coeff * p
        steps.append(f"Updated n after coefficient adjustment: {n}")

    # Creating the final result without multiplying by 1, and showing the coefficients
    result_terms = [f'{coeff}*{p}' for coeff, p in zip(coeffs, powers) if coeff != 0]

    # Now create the equation string, e.g. "121 = 81 + 27 + 9 + 3 + 1"
    result = ' + '.join([str(p) for coeff, p in zip(coeffs, powers) if coeff == 1]) \
           + ' ' + ' '.join([f"- {abs(p)}" for coeff, p in zip(coeffs, powers) if coeff == -1])

    # Returning the result in a human-readable format without 1* and -1* in the output
    final_output = f"{sum(coeff * p for coeff, p in zip(coeffs, powers))} = {result}"

    return final_output
