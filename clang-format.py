#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import os.path

workspace = os.getcwd()


@click.command()
@click.option('--path', multiple=True, default=['platforms', 'source', 'test'],
              help='Paths to format, use `--path path1 --path path2`')
def code_format(path):
    for this_path in path:
        this_path = os.path.join(workspace, this_path)
        for root, dirs, files in os.walk(this_path):
            for name in files:
                all_suffixes = ["cc", "cpp", "cxx", "c", "h", "hpp"]
                this_suffix = os.path.splitext(name)[-1][1:]
                if this_suffix in all_suffixes:
                    local_path = root + '/' + name
                    print(local_path)
                    os.system("/usr/local/bin/clang-format -i %s -style=File" % local_path)


if __name__ == "__main__":
    code_format()
