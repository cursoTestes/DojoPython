def sacar(valor):
    notas = {'10':0,'20':0,'50':0, '100':0}

    notas['100'] = int(valor / 100)
    valor -= notas['100'] * 100
    notas['50'] = int(valor / 50)
    valor -= notas['50'] * 50
    notas['20'] = int(valor / 20)
    valor -= notas['20'] * 20
    notas['10'] = int(valor / 10)

    return notas
    #return sum(notas.values())
