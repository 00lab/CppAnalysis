# coding:utf-8


class Node:
    def __init__(self, id, name_str, label_str='', in_edge_list=None, out_edge_list=None):
        self.id = id  # 每个节点的id序号
        self.name = name_str  # 每个节点显示的文本字符串
        self.label = label_str  # 节点的注释和附加信息
        if in_edge_list is None:
            in_edge_list = []
        self.in_edge_list = in_edge_list  # 所有的入边集合[]类型，Edge对象
        if out_edge_list is None:
            out_edge_list = []
        self.out_edge_list = out_edge_list  # 出边集合[]类型，Edge对象

    def set_name_str(self, name_str):
        self.name = name_str

    def get_name_str(self):
        return self.name

    def set_label_str(self, label_str):
        self.label = label_str

    def get_label_str(self):
        return self.label

    def add_in_edge(self, edge_obj):
        self.in_edge_list.append(edge_obj)

    def get_in_edge_list(self, edge_obj):
        return self.in_edge_list

    def add_out_edge(self, edge_obj):
        self.out_edge_list.append(edge_obj)

    def get_out_edge_list(self, edge_obj):
        return self.out_edge_list


class Edge:
    def __init__(self, id, src_node, dst_node, name_str=''):
        self.id = id
        self.src_node = src_node
        self.dst_node = dst_node
        self.name = name_str

    def set_name_str(self, name_str):
        self.name = name_str

    def get_name_str(self):
        return self.name
