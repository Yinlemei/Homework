#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os


def render(homeworks_entry):
    """
    Return rendered document string.
    Params:
        * homework_entry    (array)DirEntry of homeworks.
    """

    return '''
# Homework Summary
{homeworks}
    '''.format_map({
        "homeworks": "".join(map(lambda h:render_homework({
            "homework_name":
            h.name[9:],
            "users":
            "".join(map(lambda u: "    * [{name}](https://github.com/zmhab/Homework/tree/master/{h_name}/{name})\n".format(name=u,h_name=h.name), get_users(h)))
        }),homeworks_entry))
    })


def render_homework(homework):
    """
    Return rendered homework string.
    Params:
        * homework  (dict)
    """

    return '''
## {homework_name}
* Submited:
{users}
    '''.format_map(homework)

def get_users(homework_entry):
    """
    Return list of users' name.
    Params:
        * homework_entry    (DirEntry)DirEntry of homework.
    """

    users = []
    for u in os.scandir(homework_entry.path):
        if not u.name == ".schema":
            users.append(u.name)
    return users

def main():
    homeworksEntry = filter(
        lambda __: __.is_dir() and __.name.startswith("Homework"),
        os.scandir("."))
    doc = render(homeworksEntry)
    with open("Homework Summary.md","w",encoding="utf-8") as file:
        file.write(doc)

if __name__ == '__main__':
    main()