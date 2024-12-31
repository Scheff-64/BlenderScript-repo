import bpy
import os
import tempfile
#import shutil


class FBXExporter:
    def __init__(self, custom_temp_dir, filename):
        self.custom_temp_dir = custom_temp_dir
        self.filename = filename
        self.temp_folder = None
        self.filepath = None

    def create_temp_folder(self):
        """Create a temporary folder for export."""
        self.temp_folder = tempfile.mkdtemp(dir=self.custom_temp_dir)
        self.filepath = os.path.join(self.temp_folder, self.filename)

    def export(self):
        """Export the selected mesh to FBX."""
        bpy.ops.export_scene.fbx(filepath=self.filepath,
                         use_selection=True,
                         check_existing=True,
                         apply_unit_scale=True,
                         object_types={'MESH'},
                         axis_forward='Z',
                         axis_up='Y')

    def get_filepath(self):
        """Return the file path of the exported FBX."""
        return self.filepath

    def clean_up(self):
        """Optional: Clean up the temporary folder."""
        # You can use shutil to remove the folder if desired
        # import shutil
        # shutil.rmtree(self.temp_folder)
        print(f"Exported FBX to: {self.filepath}")
        #print(f"Temporary folder {self.temp_folder} cleaned up.")

# using the class
if __name__=="__main__":
    custom_temp_dir = 'D:\BLENDER_IN_D\FBX_Exports'
    filename = "exported_model.fbx"
    # Create an instance of the FBXExporter class
    exporter = FBXExporter(custom_temp_dir, filename)

    # Create a temporary folder, export the model, and clean up
    exporter.create_temp_folder()
    exporter.export()
    print(f"Exported FBX to: {exporter.get_filepath()}")
    exporter.clean_up()
