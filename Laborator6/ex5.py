"""
Write a function that receives as a parameter the path to an xml
document and an attrs dictionary and returns those elements that
have as attributes all the keys in the dictionary and values
the corresponding values. For example, if
attrs={"class": "url", "name": "url-form", "data-id": "item"}
the items selected will be those tags whose attributes are
class="url" si name="url-form" si data-id="item".
"""
# C:\Users\Laura\Desktop\pythonProject\example.xml
import re


def find_reg(dict, path):
    with open(path, "r") as fd_xml:
        xml_file = str(fd_xml.read())
        elements = re.findall(".*<.*>.*", xml_file)
        for element in elements:
            ok = False
            for attribute in dict.keys():
                string = attribute + "=\"" + dict[attribute] + "\""
                if string in element:
                    ok = True
            if ok:
                # print this element -> incomplete
                print(re.findall("<.*\\s", element)[0].split("<")[1])
                tag = re.findall("<.*\\s", element)[0].split("<")[1]
                pattern = "(?:<{}.*?>)(.*?)(?:<\\/{}>)".format(tag, tag)
                pattern = "".join(pattern.split())
                print(pattern)
                print(re.findall(pattern, xml_file))


input_path = "C:\\Users\\Laura\\Desktop\\pythonProject\\example.xml"
dictionary = {"id": "501"}
find_reg(dictionary, input_path)
