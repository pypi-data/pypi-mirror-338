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
    "2dCircularConvolution.sce",
    "2dLinearConvolution.sce",
    "BrightnessEnhance.sce",
    "BrightnessReduce.sce",
    "BtcImageCompression.sce",
    "CircularAsLineConvo.sce",
    "CircularCorrelation.sce",
    "ContrastManipulation.sce",
    "DFTgray.sce",
    "DialationErosion.sce",
    "EdgeDetection.sce",
    "GaussianFilterFun.sce",
    "GaussianFun.sce",
    "GrayLevelScaling.sce",
    "ImageAddSub.sce",
    "ImageMulDiv.sce",
    "KLTransformation.sce",
    "LinearAutoCorrelation.sce",
    "LinearCrossCorrelation.sce",
    "negativeImage.sce",
    "OpeningClose.sce",
    "RGBextract.sce",
    "SeperateImageRGB.sce",
    "Threshold.sce"
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
