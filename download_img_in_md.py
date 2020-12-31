# -*- coding: UTF-8 -*-

import re
import requests
import codecs
import sys
import imghdr
import os
import uuid


def get_md_str(file_name):
    f = codecs.open(file_name, 'r', 'utf-8')
    return f.read()


def get_urls_in_md(md_str):
    pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    iters = pattern.finditer(md_str)
    return iters


def get_img(url):
    resp = requests.get(url)
    if resp.ok:
        return resp.content
    else:
        return None


def write_to_file(img, file_name):
    with open(file_name, 'wb') as f:
        f.write(img)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage: download_img_in_md.py input_md_file_path output_img_dir_path')
        exit(-1)
    else:
        input_md_file_path = sys.argv[1]
        output_img_dir_path = sys.argv[2]
        print("input md file: "+input_md_file_path)
        md_str = get_md_str(input_md_file_path)
        url_iters = get_urls_in_md(md_str)
        for url_iter in url_iters:
            print("\tfound: "+url_iter.group(0))
            img_name = url_iter.group(1).strip()
            img_url = url_iter.group(2).split(' ')[0].strip()
            img_data = get_img(img_url)
            img_format = imghdr.what('', h=img_data)
            img_file_path = os.path.join(
                output_img_dir_path, img_name+'.'+img_format)
            if len(img_name) == 0 or os.path.exists(img_file_path):
                img_file_path = os.path.join(
                    output_img_dir_path, img_name+'('+str(uuid.uuid1())+')'+'.'+img_format)
            write_to_file(img_data, img_file_path)
            print("\t\twrote to: "+img_file_path)
