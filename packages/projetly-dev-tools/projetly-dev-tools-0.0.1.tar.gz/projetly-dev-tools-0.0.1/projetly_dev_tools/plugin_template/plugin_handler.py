import sys
import os
from string import Template, capwords



def projetly_plugin_create(module, subcommand, plugin_name):
    # print("hii...")

    plugin_name_caps = capwords(plugin_name)
    # print(plugin_name_caps + " -- " + plugin_name_caps)
    plugin_name_upper = plugin_name.upper()
    # print(plugin_name_upper + " -- " + plugin_name_upper)

    # source_path = (os.sep).join(["projetly_dev_tools", "plugin_template", "plugin"])
    source_path = (os.sep).join(["plugin_template", "plugin"])
    destination_path = "plugins"


    # Create plugin folder
    current_running_file_absolute_path = os.path.dirname(os.path.abspath(__file__))
    # print("current_running_file_absolute_path: ", current_running_file_absolute_path)
    # print("os.path.join(os.getcwd(): ", os.path.join(os.getcwd()))
    plugin_absolute_path = current_running_file_absolute_path.split(os.sep + "plugin_template")[0]
    # print("plugin_absolute_path: ", plugin_absolute_path)
    plugin_template_folder_path = os.path.join(plugin_absolute_path, source_path)
    # print("plugin_template_folder_path: ", plugin_template_folder_path)
    plugin_main_folder_path = os.path.join(os.path.join(os.getcwd()), destination_path, plugin_name)
    # print("plugin_main_folder_path: ", plugin_main_folder_path)
    is_plugin_folder_exist = os.path.exists(plugin_main_folder_path)
    # print("is_plugin_folder_exist: ", is_plugin_folder_exist)
    if not is_plugin_folder_exist:
        os.makedirs(plugin_main_folder_path)

    # Get files details
    files_path_list_source = []
    files_path_list = []

    # print(os.walk(plugin_template_folder_path))

    for (dirpath, dirnames, filenames) in os.walk(plugin_template_folder_path):
        # print("dirpath: ", dirpath)
        # print("dirnames: ", dirnames)
        # print("filenames: ", filenames)
        for dirname in dirnames:
            # print("dirname: ", dirname)
            folder_path = os.path.join(os.getcwd(), plugin_main_folder_path, dirname)
            # print("folder_path: ", folder_path)
            is_folder_exist = os.path.exists(folder_path)
            if not is_folder_exist:
                if not (dirname in ["__pycache__"]):
                    # print(f"Create {dirname} directory")
                    os.mkdir(folder_path)

        for filename in filenames:
            # print("filename: ", filename)
            files_path_source = os.path.join(os.getcwd(), dirpath, filename)
            # print("files_path_source: ", files_path_source)
            files_path_list_source.append(files_path_source)
            filename = filename.replace(".template", "")
            file_path_subfolder = files_path_source.split((plugin_template_folder_path+os.sep))[-1]
            # print("file_path_subfolder: ", file_path_subfolder)
            file_path_subfolder_list = file_path_subfolder.split(os.sep)
            # print("file_path_subfolder_list: ", file_path_subfolder_list)
            
            if len(file_path_subfolder_list) > 1:
                file_path = os.path.join(os.getcwd(), plugin_main_folder_path, file_path_subfolder_list[0], filename)
            else:
                file_path = os.path.join(os.getcwd(), plugin_main_folder_path, filename)
            # print("file_path: ", file_path)
            files_path_list.append(file_path)

    # print("\nfiles_path_list_source: ", files_path_list_source)
    # print("\nfiles_path_list: ", files_path_list)

    for index, file_path_source in enumerate(files_path_list_source):
        if file_path_source.find(".pyc") == -1:
            with open(file_path_source, "r") as fs:
                source_file_data = Template(fs.read())
                target_file_data = source_file_data.safe_substitute(
                    {
                        "plugin": plugin_name,
                        "plugin_caps": plugin_name_caps,
                        "plugin_upper": plugin_name_upper
                    }
                )

            # Write file
            source_file_path = files_path_list[index]
            with open(source_file_path, "a+") as fd:
                fd.write(target_file_data)
            source_file_path_split_list = source_file_path.split(os.sep)
            # print("source_file_path_split_list: ", source_file_path_split_list)
            # print("source_file_path_split_list[-1]: ", source_file_path_split_list[-1])
            if source_file_path_split_list[-1] == ".env":
                env_template_file = (os.sep).join(source_file_path_split_list[:-1]) + os.sep + ".env.template"
                # print("env_template_file: ", env_template_file)
                with open(env_template_file, "a+") as fd:
                    fd.write(target_file_data)

