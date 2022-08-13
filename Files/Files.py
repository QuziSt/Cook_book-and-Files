def creating_result():
    all_texts = [len(list(open(f'{i}.txt', encoding='utf-8').readlines())) for i in range(1, 4)]
    texts_dict = {'1.txt': all_texts[0], '2.txt': all_texts[1], '3.txt': all_texts[2]}
    key_list = list(texts_dict.keys())
    value_list = list(texts_dict.values())
    print(key_list)
    print(value_list)
    with open('result.txt','a', encoding='utf-8')as result:
        pos = value_list.index(sorted(all_texts)[0])
        result.write(key_list[pos]+'\n')
        result.write(str(sorted(all_texts)[0])+'\n')
        result.write(''.join(line for line in open(key_list[pos], encoding='utf-8'))+'\n')

        pos = value_list.index(sorted(all_texts)[1])
        result.write(key_list[pos] + '\n')
        result.write(str(sorted(all_texts)[1]) + '\n')
        result.write(''.join(line for line in open(key_list[pos], encoding='utf-8'))+'\n')

        pos = value_list.index(sorted(all_texts)[2])
        result.write(key_list[pos] + '\n')
        result.write(str(sorted(all_texts)[2]) + '\n')
        result.write(''.join(line for line in open(key_list[pos], encoding='utf-8'))+'\n')


creating_result()
