#!/usr/bin/env python


import os
import shutil
import sys

try:
    from xml.etree import cElementTree as ET
except ImportError:
    from xml.etree import ElementTree as ET


def add_gui_manager(tomcat_users):
    role = ET.SubElement(tomcat_users, 'role')
    role.set('rolename', 'manager-gui')
    user = ET.SubElement(tomcat_users, 'user')
    user.set('username', 'admin')
    user.set('password', 'admin')
    user.set('roles', 'manager-gui')


def main():
    for xml_file in sys.argv[1:]:
        bk = os.path.join('/tmp', os.path.basename(xml_file) + '.bk')
        shutil.move(xml_file, bk)

        xml = ET.parse(bk)

        root = xml.getroot()
        added = False
        for tomcat_users in root.findall('.//tomcat-users'):
            add_gui_manager(tomcat_users)
            added = True

        if not added:
            tomcat_users = ET.SubElement(root, 'tomcat-users')
            add_gui_manager(tomcat_users)

        xml.write(xml_file)


if __name__ == '__main__':
    main()
