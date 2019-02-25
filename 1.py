import collections

def main():
    directory = '/home/valerie/University/Статистика/labs/Dopira.csv'

    with open(directory, 'r') as file: #read from file
        file1 = file.readlines()
    print('Данные из файла: ',file1)
    print('Размер выборки: ', len(file1)-1)

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

if __name__ == "__main__":
    main()
