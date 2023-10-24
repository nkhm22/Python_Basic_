import zipfile
import collections

def unzip(archive):
    zfile=zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()
def collect_stats(file):
    result={}
    if file.endswith('.zip'):
        unzip(file)
        file= ''.join((file[:-3], 'txt'))
    text_file=open(file, 'r', encoding= 'utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char]=0
                result[j_char] += 1
    text_file.close()
    return result

def print_stats(stats):
    o = open("statistics.txt", "w", encoding='utf-8')
    print("+{:-^19}+".format('+'), file=o)
    print("|{: ^9}|{: ^9}|".format('буква','частота'), file=o)
    print("+{:-^19}+".format('+'), file=o)
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count), file=o)
    print("+{:-^19}+".format('+'), file=o)
    o.close()

def sort_frequency(stats_dict):
    sorted_values=sorted(stats_dict.values())
    sorted_dict=collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key]==i_value:
                sorted_dict[j_key]=stats_dict[j_key]
    return sorted_dict
file_name='voyna-i-mir.zip'
stats=collect_stats(file_name)
stats=sort_frequency(stats)
print_stats(stats)