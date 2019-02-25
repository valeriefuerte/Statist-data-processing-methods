import collections
import math

def main():
    directory = '/home/valerie/University/Статистика/labs/Dopira.csv'

    with open(directory, 'r') as file: #read from file
        file1 = file.readlines()
    print('Данные из файла: ',file1)
    #print('Размер выборки: ', len(file1)-1)

    sequence = list()
    for i in range(1, len(file1)): #make up the initial sequence
        sequence.insert(i, float(file1[i].split(',')[0]))
    print('Изначальный ряд: ', sequence)

    rangeSequence = sorted(sequence)
    print('Ранжированный ряд: ', rangeSequence)

    variation = list()
    count = collections.Counter()
    for i in rangeSequence:
        count[i] += 1

    for key, value in count.items():
        variation.insert(0, [key,value])
    variationSequence = sorted(variation)
    print('Вариационный ряд: ',variationSequence)

    with open('variation.csv', 'w') as variationFile:
            for i in range(len(variationSequence)):
                variationFile.write(str(variationSequence[i][0]) + ';' + str(variationSequence[i][1]) + '\n')

    n = 0
    for i in range(len(variationSequence)):
        n = variationSequence[i][1] + n
    print('Объем выборки:', n)

    K = int(1 + 3.322 * math.log(n, 10))
    print('Количество интервалов:', K)

    max = len(variationSequence)
    x_min = variationSequence[0][0]
    x_max = variationSequence[max-1][0]
    h = ( x_max - x_min ) / n
    print('Шаг интервала:', h)


if __name__ == "__main__":
    main()
