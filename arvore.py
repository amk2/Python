import json
import simplejson


def test_parse_json():
    f_path = 'dbMeta-20180809_1013.json'
    with open(f_path) as f:
        # j_data = json.load(f)      # ValueError: No JSON object could be decoded
        j_data = simplejson.load(f)  # right
    print j_data


if __name__ == '__main__':
    test_parse_json()