def prever_preco(renda, metragem):
    if renda <= 0 or metragem <= 0:
        return 0
    return (renda * 0.3) + (metragem * 1500)
