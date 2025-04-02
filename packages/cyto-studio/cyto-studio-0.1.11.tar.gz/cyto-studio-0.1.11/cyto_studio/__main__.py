"""
cyto-studio reads zarr files and displays them
"""
import sys
import pkg_resources

try:
    from cyto_studio.n_space import CYTOSTUDIO
except:
    from cyto_studio import CYTOSTUDIO

def main():
    
    try:
        pkg_resources.get_distribution("opencv-python")
        print(
            "\n[cyto-studio] ⚠️ Detected 'opencv-python', which is incompatible with napari and PySide2.\n"
            "This can cause Qt-related crashes or weird behavior.\n"
            "\n👉 To fix this, run:\n"
            "    pip uninstall opencv-python\n"
            "    pip install opencv-python-headless\n"
            "\nThen re-run cyto-studio.\n"
        )
        sys.exit(1)
    except pkg_resources.DistributionNotFound:
        pass
    
    napari = CYTOSTUDIO()
    napari.main()

if __name__ == "__main__":
    main()