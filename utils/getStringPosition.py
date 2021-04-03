from pytesseract import image_to_data

minConf = 80  # 识别时最小有效置信度
lang = 'chi_sim'  # 识别时使用的文字语言


def get_string_position(img):
    img_data = image_to_data(img, lang=lang).split('\n')
    data_cache = {}
    output = []
    img_data.pop(0)
    for line in img_data:
        row = line.split('\t')
        if len(row) < 12 or int(row[10]) < minConf:
            continue
        key = row[2] + ':' + row[4]
        value = row[11]
        left = int(row[6])
        top = int(row[7])
        right = left + int(row[8])
        bottom = top + int(row[9])
        conf = int(row[10])
        if key in data_cache:
            data_cache[key][0] = data_cache[key][0] + value
            data_cache[key][1] = (min(data_cache[key][1][0], left), max(data_cache[key][1][1], right))
            data_cache[key][2] = (min(data_cache[key][2][0], top), max(data_cache[key][2][1], bottom))
            data_cache[key][3] = (min(data_cache[key][3][0], conf), max(data_cache[key][3][1], conf))
        else:
            data_cache[key] = [value, (left, right), (top, bottom), (conf, conf)]
    for line in data_cache:
        output.append(data_cache[line])
    return output


def get_special_string_position(data, string, log=False):
    for row in data:
        if log:
            print(row)
        if row[0].find(string) > -1:
            print((row[2][0] + row[2][1]) / 2)
            return (row[1][0] + row[1][1]) / 2, (row[2][0] + row[2][1]) / 2
    return None


def find_string_in_img(img, string, log=False):
    return get_special_string_position(get_string_position(img), string, log)
