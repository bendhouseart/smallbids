import os
import pathlib
import shutil
import subprocess

# get this files, test folder, etc directories
this_files_path = pathlib.Path(__file__).resolve()
test_folder_path = this_files_path.parent
project_folder = test_folder_path.parent
bids_spec_path = pathlib.Path(os.path.join(project_folder, 'bids-specification'))


def test_make_getspec():
    # check to see if bids-specification submodule is already present
    exists = bids_spec_path.exists()
    if exists and 'smallbids/bids-specification' in bids_spec_path._str:
        # remove it if it does exist
        shutil.rmtree(bids_spec_path)

    # collect submodule and load it using make
    collect_submodule = subprocess.run(f'cd {project_folder} && make getspec', shell=True,
    capture_output=True)

    assert collect_submodule.returncode == 0
    assert bytes("Submodule path 'bids-specification': checked out", 'utf-8') in collect_submodule.stdout 
    assert bids_spec_path.is_dir()

def test_make_mkdocs():
    run_mkdocs = subprocess.run(f"cd {project_folder} && make mkdocs", shell=True, capture_output=True)
    assert run_mkdocs.returncode == 0

