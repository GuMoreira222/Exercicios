def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos aluno (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    aluno = {}
    aluno['Total'] = len(nota)
    aluno['Maior'] = max(nota)
    aluno['Menor'] = min(nota)
    aluno['Média'] = sum(nota)/len(nota)
    if sit == True:
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'BOA'
        elif aluno['Média'] >= 5:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'RUIM'
    return aluno

r = notas(4,8,9,7, sit=True)
print(r)

