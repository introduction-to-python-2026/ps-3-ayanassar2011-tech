def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        tmp = ((-1)**i)   *   (1/(2*i+1))
        leibniz_series.append(tmp)
    pi_aproximation = 4 * sum(leibniz_series)

    return pi_aproximation
