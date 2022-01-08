class AbstractItem(object):
    def __init__(self, item_name):
        self.item_name = item_name

    def is_dir(self):
        return NotImplemented


class Directory(AbstractItem):
    def __init__(self, item_name):
        self.item_list = []
        AbstractItem.__init__(self, item_name)

    def is_dir(self):
        return True


class StrFile(AbstractItem):
    def __init__(self, item_name):
        self.content = ""
        AbstractItem.__init__(self, item_name)

    def is_dir(self):
        return False


class FileSystem(object):

    def __init__(self):
        self.root = Directory("")

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        path_list = path[1:].split("/")
        pwd = self.root
        for dir_name in path_list:
            for item in pwd.item_list:
                if item.item_name == dir_name:
                    pwd = item
                    break
        if not pwd.is_dir():
            return [pwd.item_name]
        ret = []
        for item in pwd.item_list:
            ret.append(item.item_name)
        return sorted(ret)

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        path_list = path[1:].split("/")
        pwd = self.root
        for dir_name in path_list:
            found = False
            for item in pwd.item_list:
                if item.is_dir() and item.item_name == dir_name:
                    pwd = item
                    found = True
                    break
            if not found:
                new_dir = Directory(dir_name)
                pwd.item_list.append(new_dir)
                pwd = new_dir

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        path_list = filePath[1:].split("/")
        file_name = path_list[-1]
        path_list.pop()
        pwd = self.root
        for dir_name in path_list:
            for item in pwd.item_list:
                if item.item_name == dir_name:
                    pwd = item
                    break
        file_exist = False
        for item in pwd.item_list:
            if (not item.is_dir()) and item.item_name == file_name:
                file_exist = True
                pwd = item
                break
        if file_exist:
            pwd.content += content
        else:
            new_file = StrFile(file_name)
            new_file.content += content
            pwd.item_list.append(new_file)

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        path_list = filePath[1:].split("/")
        file_name = path_list[-1]
        path_list.pop()
        pwd = self.root
        for dir_name in path_list:
            for item in pwd.item_list:
                if item.item_name == dir_name:
                    pwd = item
                    break
        for item in pwd.item_list:
            if (not item.is_dir()) and item.item_name == file_name:
                return item.content
        return ""

# The FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
