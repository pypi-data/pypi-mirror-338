import os
import shutil
from pathlib import Path
def build(folder_name):
  
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("Done")
    else:
        print(f"Folder '{folder_name}' already exists.")
    
    # Path to the current directory
    current_dir = Path(__file__).parent
    
    # List of .py files to copy
    py_files = [
  "add_delete_arrayuseState.js",
  "add_post.js",
  "add_remove_specific.js",
  "commandline_user.js",
  "countDown_useEffect.js",
  "counter_classcomp.js",
  "dataFetch_useEffect.js",
  "delete.js",
  "Eventhandle_handleinputchange.js",
  "focus_useref.js",
  "FormWithRef.js",
  "get_test.js",
  "http.js",
  "Incre_Decre_Re_usereducer.js",
  "increase_UseReducer.js",
  "keydown_eventhandler.js",
  "mongo_alluser.js",
  "mongo_collection.js",
  "mongo_conn.js",
  "mongo_delete.js",
  "mongo_getid.js",
  "mongo_insert.js",
  "mongo_update.js",
  "Mount.js",
  "nestedroute.js",
  "para_child_useImperative.js",
  "Patch_update.js",
  "props_classComp.js",
  "props_FunctionalComp.js",
  "read_files.js",
  "routing.js",
  "shopping_cart.js",
  "Unmount.js",
  "update_messState.js",
  "UpdateMount.js",
  "useState_Counter.js",
  "validation_useEffect.js",
  "Winresize_useEffect.js",
  "write_append_rename_files.js",
  "users.json"
]
 # Add the names of your .py files here
    
    # Iterate over the list of files and copy each to the new folder
    for file_name in py_files:
        source_file = current_dir / file_name
        destination_file = Path(folder_name) / file_name
        
        if source_file.exists():  # Check if the source file exists
            shutil.copy(source_file, destination_file)
        else:
            print(f"File '{file_name}' not found in the package directory.")
