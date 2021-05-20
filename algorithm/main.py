import clustering as clustering
import numpy as numpy

def printPartition(path, cluster):
    file = open(path, 'w')
    for each in cluster:
        file.write(str(each.nome) + ' ' + str(each.cluster)+'\n')


def main():
    auxiliar = input(
        "Qual o arquivo que deseja inserir?\n 1 = c2ds1-2sp\n 2 = c2ds3-2g\n 3 = monkey\n")
    if auxiliar == "1":
        p = "c2ds1-2sp"
    elif auxiliar == '2':
        p = "c2ds3-2g"
    elif auxiliar == '3':
        p = "monkey"

    path = "bases/" + p + ".txt"
    # file = pandas.read_csv(path, sep='\t')
    # data = file.iloc[:, :].values
    data = readDataSet(path)
        
    nClusters = int(input("Quantos clusters voce deseja utilizar?\n"))
    
    nIterations = int(input("Quantas iteracoes voce deseja realizar?\n"))
    # incializa o kmeans
    
    result = clustering.kMeans(nClusters, nIterations, data, p)
    # itera o kmeans
    
    result.fit()

    #plots.kMeansPlot(result)
    pat = "generated/" + p + "kMeans" + \
        "C" + str(nClusters) + "_" + "I" + str(nIterations) + '.clu'

    if(auxiliar == '3'):
        for aaa in result.data:
            aaa.cluster += 1
    printPartition(pat, result.data)


def readDataSet(name):
    path = name
    print(path)
    file = open(path)
    element = []
    dataSet = []
    nome = 'nada'
    c = 0
    for line in file:
        for word in line.split():
            if(word == 'sample_label'):  # ignore the first line
                break
            else:
                if(line.split().index(word) == 0):
                    nome = word
                else:
                    element.append(float(word))  # capting the data
        if(element):
            novoObjeto = clustering.objects(nome, element, c)
            dataSet.append(novoObjeto)
            c += 1
        element = []
    file.close()
    return dataSet


main()
