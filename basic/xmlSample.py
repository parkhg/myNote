# XML 처리하기
# 1. XML문서 생성하기
# 2. XML문서 파싱하기

# 1. XML문서 생성하기
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump, parse

#note = Element("note", date="2017.07.01")
note = Element("note")
note.attrib["date"] = "2018.07.02"

to   = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note,"from").text = "Jani"                 # Element 추가
SubElement(note,"heading").text = "Reminder"          # Element 추가
SubElement(note,"body").text = "Don't forget me"      # Element 추가

#----------------------------------------------------------------------
# XML정보 indent 설정
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem,level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
#----------------------------------------------------------------------

indent(note)
dump(note)          # 출력

# xml파일 저장
ElementTree(note).write("note.xml")


#---------------------------------------------------------------------
# xml파일 Read...

tree = parse("note.xml")
note = tree.getroot()

print(note)
print(note.get("date"))
print(note.get("foo","default"))
print(note.keys())
print(note.items())

from_tag  = note.find("from")
from_tags = note.findall("from")
from_text = note.findtext("from")

print(from_tag, from_tags, from_text)

childs = note.getiterator("from")
print(childs)
