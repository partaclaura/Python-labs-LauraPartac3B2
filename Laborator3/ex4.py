#  The build_xml_element function receives the following
#  parameters: tag, content, and key-value elements given as name-parameters.
#  Build and return a string that represents the corresponding XML element.
#  Example:
#  build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
#  returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag, content, key_value_elements):
    result = "<" + tag
    for key in key_value_elements.keys():
        result += " " + key + "=\"" + key_value_elements[key] + "\""
    result += "> " + content + " </" + tag + ">"
    return result


print(build_xml_element("a", "Hello there", {"href": " http://python.org ", "_class": " my-link ", "_id=": "some_id "}))
