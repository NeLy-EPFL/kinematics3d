from pathlib import Path
from tqdm import tqdm
import shutil

def find_synch_data_folder(full_path, synch_data_folder=Path("/mnt/upramdya_data/FH/gizem-grooming")):
    """Find the synchronization data folder for a given full path.
    The full path should be in the format:
        /mnt/upramdya_data/FH/250618_aJO-CsChr/Fly1
    """

    # Get the date and genotype from the full path
    date_genotype = full_path.split("/")[4]
    date = date_genotype.split("_")[0]
    genotype = date_genotype.split("_")[1]
    # Get the fly number from the full path
    fly_number = full_path.split("/")[-1]
    # Construct the path to the synch data folder
    synch_data_path = list(synch_data_folder.rglob(f"{date}*/{genotype}*/{fly_number}"))

    if len(synch_data_path) == 1:
        return synch_data_path[0]
    else:
        raise RuntimeError(
            f"Synch data folder not found for {full_path}. OR"
            f"Expected one folder, but found {len(synch_data_path)}."
        )

def copy_synch_data(synch_path, beh_path):
    """
    Copy the synch data from the synch path to the behavior path.
    Synch path should be in the format (output of find_synch_data_folder):
        '/mnt/upramdya_data/FH/gizem-grooming/250618_data/aJO-CsChr/Fly1'
    Behavior path should be in the format:
        '/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly1'
    """
    # Convert paths to Path objects        
    synch_path = Path(synch_path) if not isinstance(synch_path, Path) else synch_path
    beh_path = Path(beh_path) if not isinstance(beh_path, Path) else beh_path

    # Number of files in the synch path
    no_trials = len(list(synch_path.glob("trial*")))
    # Copy the synch data to the behavior path
    for i in range(1, no_trials + 1):
        synch_path_trial = list((synch_path / f"trial{i:03d}").glob("Sync*"))[0]
        beh_path_trial = list((beh_path).glob(f"{i:03d}_*"))[0] / "behData" / "syncData"

        # Copy synch data folder to the behavior path
        print(f"\nCopying {synch_path_trial} to {beh_path_trial}" )
        shutil.copytree(synch_path_trial, beh_path_trial, dirs_exist_ok=True)


if __name__ == "__main__":
    # Set up the directories 
    directories = {
        "AJO": [
            "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly2", # Ball pushing a lot 
            "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly3",
            "/mnt/upramdya_data/FH/250702_aJO-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250702_aJO-CsChr/Fly2",
        ],
        "ABN2": [
            "/mnt/upramdya_data/FH/250620_aBN2-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250620_aBN2-CsChr/Fly2",
            "/mnt/upramdya_data/FH/250620_aBN2-CsChr/Fly3",
            "/mnt/upramdya_data/FH/250714_aBN2-CsChr/Fly1",
        ],
        "ADN1": [
            "/mnt/upramdya_data/FH/250625_aDN1-CsChr/Fly2",
            "/mnt/upramdya_data/FH/250625_aDN1-CsChr/Fly3",
            "/mnt/upramdya_data/FH/250702_aDN1-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250702_aDN1-CsChr/Fly2",
            "/mnt/upramdya_data/FH/250714_aDN1-CsChr/Fly1",
        ]
    }

    for genotype, paths in directories.items():
        for path in tqdm(paths, desc=f"Processing {genotype} paths"):
            try:
                synch_path = find_synch_data_folder(path)
                copy_synch_data(synch_path, path)
            except RuntimeError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
