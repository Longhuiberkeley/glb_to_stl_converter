import os
import trimesh

def convert_glb_to_stl(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get all GLB files in the input directory
    glb_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.glb')]
    
    for glb_file in glb_files:
        try:
            # Load the GLB file
            input_path = os.path.join(input_dir, glb_file)
            mesh = trimesh.load(input_path)
            
            # Create output filename
            output_filename = os.path.splitext(glb_file)[0] + '.stl'
            output_path = os.path.join(output_dir, output_filename)
            
            # Export as STL
            mesh.export(output_path)
            print(f"Successfully converted {glb_file} to {output_filename}")
            
        except Exception as e:
            print(f"Error converting {glb_file}: {str(e)}")

if __name__ == "__main__":
    # Set your input and output directories
    input_directory = "glb_files"  # Directory containing GLB files
    output_directory = "stl_files"  # Directory where STL files will be saved
    
    convert_glb_to_stl(input_directory, output_directory)