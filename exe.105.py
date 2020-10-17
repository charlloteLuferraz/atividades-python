def notas(*n, sit=False):
    """
    → Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return: dicionário com vários informaões sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['total'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5, 2.5, 9, 8.5)
#print(resp)
help(notas)
