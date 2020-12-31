# -*- coding: UTF-8 -*-

import sys
import os
import base64

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: img_to_base64.py img_file_path')
        exit(-1)
    else:
        img_file_path = sys.argv[1]
        with open(img_file_path, 'rb') as f:
            img_data = f.read()
            base64_output = base64.b64encode(img_data)
            file_name = os.path.basename(img_file_path)
            print('!['+file_name + ']['+file_name+']\n')
            print('['+file_name + ']:data:image/png;base64,' +
                  base64_output.decode())
