import glob
import hashlib
import os


def md5(file_path):
    with open(file_path, 'rb') as f:
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        return hash_code


def scan(glob_path):
    MD5List = {}
    for fileName in glob.glob(glob_path, recursive=True):
        if os.path.isfile(fileName):
            key = md5(fileName)
            if key in MD5List:
                print('已经存在文件:%s\n重复文件:%s\n删除文件:%s' %
                      (MD5List.get(key), fileName, fileName))
                try:
                    os.remove(fileName)
                except Exception as e:
                    print('删除失败:%s\n如果提示权限不足,请右键属性关闭文件夹FileStorage的只读属性' % e)
            else:
                MD5List[key] = fileName


if __name__ == '__main__':
    scan(r"C:\Users\**\Documents\WeChat Files\**\FileStorage\**\*")
