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
    h = int(( x_max - x_min ) / K) + 1
    print('Шаг интервала:', h)

    x = [x_min, x_min + h, x_min + 2*h, x_min + 3*h, x_min + 4*h, x_min + 5*h, x_min + 6*h, x_min + 7*h]
    n_1 = list()
    nn_1 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        nn1 = variationSequence[i][1]
        if j < x[1]:
            n_1.append(j)
            nn_1.append(nn1)
    print('Первый интервал ', n_1)
    nn__1 = 0
    for i in range(len(nn_1)):
        nn__1 =   nn_1[i] + nn__1
    print(nn__1)

    n_2 = list()
    nn_2 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        if j >= x[1]:
            if j < x[2]:
                n_2.append(j)
                nn_2.append(nn1)
    print('Второй интервал ', n_2)
    nn__2 = 0
    for i in range(len(nn_2)):
        nn__2 =   nn_2[i] + nn__2
    print(nn__2)

    n_3 = list()
    nn_3 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        if j >= x[1]:
            if j >= x[2]:
                if j < x[3]:
                    n_3.append(j)
                    nn_3.append(nn1)
    print('Третий интервал ', n_3)
    nn__3 = 0
    for i in range(len(nn_3)):
        nn__3 =   nn_3[i] + nn__3
    print(nn__3)

    n_4 = list()
    nn_4 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        if j >= x[1]:
            if j >= x[2]:
                if j >= x[3]:
                    if j < x[4]:
                        n_4.append(j)
                        nn_4.append(nn1)
    print('Четвертый интервал ', n_4)
    nn__4 = 0
    for i in range(len(nn_4)):
        nn__4 =   nn_4[i] + nn__4
    print(nn__4)

    n_5 = list()
    nn_5 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        if j >= x[1]:
            if j >= x[2]:
                if j >= x[3]:
                    if j >= x[4]:
                        if j < x[5]:
                            n_5.append(j)
                            nn_5.append(nn1)
    print('Пятый интервал ', n_5)
    nn__5 = 0
    for i in range(len(nn_5)):
        nn__5 =   nn_5[i] + nn__5
    print(nn__5)

    n_6 = list()
    nn_6 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        if j >= x[1]:
            if j >= x[2]:
                if j >= x[3]:
                    if j >= x[4]:
                        if j >= x[5]:
                            if j < x[6]:
                                n_6.append(j)
                                nn_6.append(nn1)
    print('Шестой интервал ', n_6)
    nn__6 = 0
    for i in range(len(nn_6)):
        nn__6 =   nn_6[i] + nn__6
    print(nn__6)

    n_7 = list()
    nn_7 = list()
    for i in range(len(variationSequence)):
        j = variationSequence[i][0]
        if j >= x[1]:
            if j >= x[2]:
                if j >= x[3]:
                    if j >= x[4]:
                        if j >= x[5]:
                            if j >= x[6]:
                                if j <= x[7]:
                                    n_7.append(j)
                                    nn_7.append(nn1)
    print('Седьмой интервал ', n_7)
    nn__7 = 0
    for i in range(len(nn_7)):
        nn__7 =   nn_7[i] + nn__7
    print(nn__7)


    with open('interval.csv', 'w') as intervalFile:
        intervalFile.write(str(x[0]) + ';' + str(x[1]) + ';' + str(nn__1) + ';' + str(nn__1 / n) + '\n')
        intervalFile.write(str(x[1]) + ';' + str(x[2]) + ';' + str(nn__2) + ';' + str(nn__2 / n) + '\n')
        intervalFile.write(str(x[2]) + ';' + str(x[3]) + ';' + str(nn__3) + ';' + str(nn__3 / n) + '\n')
        intervalFile.write(str(x[3]) + ';' + str(x[4]) + ';' + str(nn__4) + ';' + str(nn__4 / n) + '\n')
        intervalFile.write(str(x[4]) + ';' + str(x[5]) + ';' + str(nn__5) + ';' + str(nn__5 / n) + '\n')
        intervalFile.write(str(x[5]) + ';' + str(x[6]) + ';' + str(nn__6) + ';' + str(nn__6 / n) + '\n')
        intervalFile.write(str(x[6]) + ';' + str(x[7]) + ';' + str(nn__7) + ';' + str(nn__7 / n) + '\n')




if __name__ == "__main__":
    main()
