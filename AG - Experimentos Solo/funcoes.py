# Funções dos Experimentos A.01 e A.02 (Dia 09/03/2023)
# preciso de uma lista para representar meu individuo
# quantidade de elementos na lista é o número de genes
# cada gene pode ser 0 ou 1, vou gerar esse números aleatoriamente
# funções

import random
import itertools

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def individuo_cb(n):
    """Gera um individuo para o problema das caixas binárias.
    
    Args:
      n: número de genes do indivíduo.
    
    Return:
       Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individiuo: lista contendo os genes das caixas binárias
    
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)

# Funções dos Experimentos A.03 e A.04 (Dia 16/03/2023)