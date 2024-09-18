from pathlib import Path
from rich import print
import glob
import yaml


def yaml_files(path):

    # Use glob to find all .yml files in the current directory
    yml_files = glob.glob(str(path / "*.yml"))

    return yml_files


def parse_file_name(file_name):
    pass


def read_yaml_file(file_name):
    with open(file_name, "r") as f:
        return yaml.safe_load(f)


# arista_eos_show_interfaces.yml

if __name__ == "__main__":

    current_dir = Path.cwd()
    file_list = yaml_files(current_dir)
    import pdbr

    pdbr.set_trace()
    print(file_list)

    for f_name in file_list:
        data = read_yaml_file(f_name)
        print(data)
        break

    ## Read and process each .yml file
    # for file_path in yml_files:
    # Create a Path object
    # path_object = Path(full_path)
    #
    ## Get the directory path
    # directory_path = path_object.parent
    #
    ## Get the filename
    # filename = path_object.name
