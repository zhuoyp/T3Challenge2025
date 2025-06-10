How to prepare the Trauma THOMPSON Dataset for Training in MMAction


1. Download the Trauma THOMPSON Dataset from the Grand Challenge Website 
2. Run the extract_frames.py file after filling information about specific file paths 
3. Run the sort_frames.py file after filling in specific file paths 

For MMAction
4. Install MMAction using the instructions from this link: https://mmaction2.readthedocs.io/en/latest/get_started/installation.html
5. Run create_annotations.ipynb file to create MMAction Annotation File
6. Run training script with Config file

See https://mmaction2.readthedocs.io/en/latest/user_guides/config.html for further details on how to set up config files and training scripts