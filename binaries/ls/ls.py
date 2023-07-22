import glob
import os
from termcolor import cprint

def parse_paths_with_wildcards(paths_list):
    matched_files = []
    for path in paths_list:
        matched_files.extend(glob.glob(path))
    return matched_files

class LsCmd:
    def __init__(self, args):
        self.all = args.all
        if len(args.paths) == 0:
            self.paths = [os.getcwd()]
        else:
            self.paths = parse_paths_with_wildcards(args.paths)
        self.run()


    def _identify_color(self, item):
        color, attrs = ('white', [])
        if os.path.isdir(item):
            color, attrs = ('blue', ['bold'])
        elif os.access(item, os.X_OK):
            color, attrs = ('green', ['bold'])
        return color, attrs

    def run(self):
        
        for path in self.paths:
            if not os.path.exists(path):
                print(f"ls: cannot access '{path}': No such file or directory")
                continue

            items = os.listdir(path)
            items.sort(key=str.lower)
            
            print(f"{path}:") if len(self.paths) > 1 else None
            for item in items:
                color, attrs = self._identify_color(item)
                cprint(item, color, attrs=attrs, end='  ') if self.all == True or not item.startswith(".") else None
            print()
