#!/usr/bin/python3
"""Define json save function"""
import sys
import os
load_j = __import__("6-load_from_json_file").load_from_json_file
save_j = __import__("5-save_to_json_file").save_to_json_file


args = sys.argv

if len(args) == 1:
    args.clear()

if os.path.exists("add_item.json"):
    data = load_j("add_item.json")
    save_j(data + args[1:], "add_item.json")
else:
    save_j(args[1:], "add_item.json")
