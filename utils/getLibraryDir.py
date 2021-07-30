def get_lib_dir(path, folder_delimiter, append_string="", no_of_rel_paths=1):
    return folder_delimiter.join((s_path := path.split(folder_delimiter))[:len(s_path)-no_of_rel_paths]) + append_string
