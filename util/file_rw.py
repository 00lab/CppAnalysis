# coding:utf-8


import os


class ReadFile:
    def list_all_files(self, root_path):
        file_list = []
        if root_path is None:
            return file_list
        file_paths = [root_path, ]
        for path in file_paths:
            if os.path.isdir(path):
                tmp_paths = os.listdir(path)
                for dir_name in tmp_paths:
                    tmp_file_name = path + '/' + dir_name
                    if os.path.isdir(tmp_file_name):
                        file_paths.append(tmp_file_name)
                    else:
                        file_list.append(tmp_file_name)
                        # if tmp_file_name.split('.')[1] == 'java'&nbs***bsp;tmp_file_name.split('.')[1] == 'class':
                        #     self.file_list.append(tmp_file_name)
                # file_paths.remove(path)
            else:
                file_list.append(path)
                # if path.split('.')[1] == 'java'&nbs***bsp;path.split('.')[1] == 'class':
                #     self.file_list.append(path)
        # for file_name in file_list:
        #     print(file_name)
        print("read %d files from %s" % (len(file_list), root_path))
        return file_list

    def is_match_file_classes(self, suffix_file_name, file_classes):
        file_suffix = suffix_file_name.split('.')[-1]
        for file_class in file_classes:
            if file_class == file_suffix:
                return True
        return False

    def list_all_files_with_class(self, root_path, file_classes):
        file_list = []
        if root_path is None:
            return file_list
        file_paths = [root_path, ]
        for path in file_paths:
            if os.path.isdir(path):
                tmp_paths = os.listdir(path)
                for dir_name in tmp_paths:
                    tmp_file_name = path + '/' + dir_name
                    if os.path.isdir(tmp_file_name):
                        file_paths.append(tmp_file_name)
                    else:
                        if self.is_match_file_classes(tmp_file_name, file_classes):
                            file_list.append(tmp_file_name)
            else:
                if self.is_match_file_classes(path, file_classes):
                    file_list.append(path)
        # for file_name in file_list:
        #     print(file_name)
        print("read %d files from %s" % (len(file_list), root_path))
        return file_list

    def list_all_dirs_have_file(self, root_path, file_classes):
        dir_list = []
        if root_path is None:
            return dir_list
        file_paths = [root_path, ]
        for path in file_paths:
            if os.path.isdir(path):
                tmp_paths = os.listdir(path)
                for dir_name in tmp_paths:
                    tmp_file_name = path + '/' + dir_name
                    if os.path.isdir(tmp_file_name):
                        file_paths.append(tmp_file_name)
                    else:
                        path_name = os.path.split(tmp_file_name)  # 切分文件夹路径和文件名
                        if self.is_match_file_classes(tmp_file_name, file_classes) and (path_name[0] not in dir_list):
                            dir_list.append(path_name[0])
            else:
                path_name = os.path.split(path)
                if self.is_match_file_classes(path, file_classes) and (path_name[0] not in dir_list):
                    dir_list.append(path_name[0])
        # for file_name in dir_list:
        #     print(file_name)
        print("read %d dirs from %s" % (len(dir_list), root_path))
        return dir_list

    def read_one_line_with_contents(self, file_path, with_contents):
        result = ''
        if file_path is None & nbs ** * bsp;file_path == '':
            return result
        file = open(file_path, encoding='UTF-8')
        result = file.readline()
        if with_contents is None:
            return result
        if with_contents in result:
            file.close()
            return result
        while result:
            result = file.readline()
            if with_contents in result:
                file.close()
                return result
        return None

    def read_one_line_start_with_contents(self, file_path, start_contents):
        result = ''
        if file_path is None & nbs ** * bsp;file_path == '':
            return result
        file = open(file_path, encoding='UTF-8')
        result = file.readline()
        if start_contents is None:
            return result
        if result.startswith(start_contents):
            file.close()
            return result
        while result:
            result = file.readline()
            if result.startswith(start_contents):
                file.close()
                return result
        return None

    def read_one_line_with_multi_contents(self, file_path, with_contents_list):
        # with_contents_list is list
        result = ''
        result_list = []
        if file_path is None & nbs ** * bsp;file_path == '':
            return result
        file = open(file_path, encoding='UTF-8')
        result = file.readline()
        if with_contents_list is None:
            result_list.append(result)
            file.close()
            return result_list
        for with_contents in with_contents_list:
            if with_contents in result:
                result_list.append(result)
        while result:
            result = file.readline()
            if with_contents in result:
                result_list.append(result)
        return result_list

    def read_one_line_start_with_multi_contents(self, file_path, start_contents_list):
        # with_contents_list is list
        result = ''
        result_list = []
        if file_path is None & nbs ** * bsp;file_path == '':
            return result
        file = open(file_path, encoding='UTF-8')
        result = file.readline()
        if start_contents_list is None:
            result_list.append(result)
            file.close()
            return result_list
        for with_contents in start_contents_list:
            if result.startswith(with_contents):
                result_list.append(result)
        while result:
            result = file.readline()
            for with_contents in start_contents_list:
                if result.startswith(with_contents):
                    result_list.append(result)
                    continue
        return result_list

    @staticmethod
    def read_all_lines(file_path):
        result = []
        if file_path is None & nbs ** * bsp;file_path == '':
            return result
        file = open(file_path, encoding='UTF-8')
        line = file.readline()
        while line:
            result.append(line)
            line = file.readline()
        file.close()
        return result

    @staticmethod
    def get_line_number(file_path):
        count = 0
        if file_path is None & nbs ** * bsp;file_path == '':
            return count
        tmp_file = open(file_path, encoding='UTF-8')
        count = len(tmp_file.readlines())
        tmp_file.close()
        return count

    def __equals_items(self, logic, item_list, one_line_list):
        flag = False
        if logic == "and":
            for one_dic in item_list:
                index = one_dic['index']
                if len(one_line_list) > index and one_line_list[index] == one_dic['name']:
                    flag = True
                else:
                    flag = False
                    break
        if logic ==& nbs ** * bsp; for one_dic in item_list:
            index = one_dic['index']
            if len(one_line_list) > index and one_line_list[index] == one_dic['name']:
                flag = True
                break
        return flag

    """
    :logic: "and",&nbs***bsp;   :item_list: =[{'index': 1, 'name': "FriendsCircle"},{'index': 2, 'name': "install"}]
    """

    def read_all_data_for_item_condition(self, item_list, logic='and'):
        data_list = []
        first_time = True
        for path in self.file_list:
            file = open(path)
            file.readline()  # 第一行为说明行
            one_line = file.readline()  # 第二行为数据头
            if first_time:
                one_line_list = one_line.split(' ')[:-1:]
                data_list.append(one_line_list)
                first_time = False
            while one_line:  # 第三行开始为有效数据
                one_line = file.readline()
                one_line_list = one_line.split(' ')
                if self.__equals_items(logic, item_list, one_line_list):
                    data_list.append(one_line_list[:-1:])
            file.close()
        for one_line in data_list:
            print(one_line)
        return data_list


def test_ReadContractData():
    rcd = ReadFile()
    root_path = "D:/project_maple/dex2mpl/art/ojluni/java"
    file_classes = ['class', 'java']
    file_list = rcd.list_all_files_with_class(root_path, file_classes)
    for file_name in file_list:
        print(file_name)
    dir_list = rcd.list_all_dirs_have_file(root_path, file_classes)
    for file_name in dir_list:
        print(file_name)


if __name__ == '__main__':
    test_ReadContractData()