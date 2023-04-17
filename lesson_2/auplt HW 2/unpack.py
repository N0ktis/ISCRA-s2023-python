import sys
import math


# Функция отбрасывает весб путь к файлу, обрабатывает имя, затем снова добавляет путь

def path_creator(in_name):
    if in_name.count('\\') == 0:
        return file_name_creator(in_name)
    else:
        paths = in_name.split('\\')
        return '\\'.join(paths[:-1]) + '\\' + file_name_creator(paths[-1])


# Функция изменения имени файла
# Если файл расширения .lzw, оно отьрасывается, если при этом нет расширения, устанавливается расширение .dec
# Если файл не имеет расширения, расширение устанавливается .dec
# К имени каждого файла добавляется _dec

def file_name_creator(in_name):
    if in_name.count('.') >= 2:
        name = in_name.split('.')
        new_name = '.'.join(name[:-2]) + "_dec." + name[-2]
        if name[-1] == 'lzw':
            return new_name
        else:
            new_name = '.'.join(name[:-1]) + "_dec." + name[-1]
            return new_name
    elif in_name.count('.') == 1:
        name = in_name.split('.')
        if name[-1] == 'lzw':
            return name[0] + "_dec" + '.dec'
        else:
            return name[0] + "_dec." + name[-1]
    else:
        return in_name + "_dec.dec"


if not (2 <= len(sys.argv) <= 3):
    print('Usage: python', sys.argv[0], 'input_file (output_file)')
    exit(-1)

out_path = sys.argv[2] if len(sys.argv) == 3 else path_creator(sys.argv[1])

dictionary = {i: (i,) for i in range(256)}
sequence = []
i = 0

with open(sys.argv[1], 'rb') as input_file:
    data = input_file.read()
    print("Your file:", out_path)
    with open(out_path, 'wb') as output_file:
        while i < len(data):
            if not sequence:
                n = len(dictionary)

            else:
                n = len(dictionary) + 1
            bits = math.ceil(math.log2(n))
            bytes = bits // 8
            if bits % 8 != 0:
                bytes += 1
            index: int = int.from_bytes(data[i:i + bytes], 'little')
            if index == len(dictionary):
                ch = len(sequence) - 1 if len(sequence) > 1 else 1
                new_sequence = sequence + sequence[:ch]
            else:
                new_sequence = list(dictionary[index])

            if dictionary.get(index) is not None:
                if (i > 0):
                    dictionary[len(dictionary)] = tuple(sequence + new_sequence[0:1])
                output_file.write(bytearray(new_sequence))
                sequence = new_sequence
            else:
                sequence.append(sequence[0])
                output_file.write(bytearray(sequence))
                dictionary[len(dictionary)] = tuple(sequence)

            i += bytes

print("DONE!!!")
