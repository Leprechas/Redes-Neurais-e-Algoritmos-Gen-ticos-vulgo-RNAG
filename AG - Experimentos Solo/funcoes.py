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


def populacao_cb(tamanho, n):
    """cria uma pop no problema do experimento A.03

    Arg: Número genes e tamanho da pop

    return: uma lista com individuos (cada item é um)
    e cada individuo é uma lista com n genes
    """
    populacao = []
    for _ in range(tamanho):  # O "_" armazena o último comando feito
        populacao.append(individuo_cb(n))
    return populacao


def selecao_roleta_max(populacao, fitness):
    """Seleciona os indi. de uma pop. usando o método da roleta

    OBS: só funciona para prob. de maximização

    Arg;
        pop: lista com os indivi.
        fitness: lista com os valores da funcao objetivo dos indivi. da pop

    Returns;
        Pop dos indivíduos selecionados

    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


def funcao_obj_pop_cb(populacao):
    """Calcula a func objetivo para todos os indivi. de uma pop

    Arg;
        pop: lista com todos os seres da pop

    return: lista de valores representando a pontuação fitness de cada indivi.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    Arg;
        pai: uma lista
        mae: uma lista

    Returns:
        2 listas, cada lista um filho
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = pai[ponto_de_corte:] + mae[:ponto_de_corte]

    return filho1, filho2

def mutacao_cb(individuo):
    """ Garantir mutação de um gene de um individuo
    
    Arg;
        individuo: uma lista
        
    Returns: 1 individuo sofre uma mutação em 1 gene
    """
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo
