import nilearn.image
import pandas as pd
import nibabel as nib


def inspect_nifti_file(nifti_path):
    # Load the NIfTI image using NiLearn
    nii_img = nilearn.image.load_img(nifti_path)
    
    # Extract header and affine 
    nii_header = nii_img.header
    nii_affine = nii_img.affine
    
    # Get image shape and voxel size
    nii_shape = nii_img.shape
    nii_voxel_size = nii_header.get_zooms()
    
    # Print relevant details
    print("NIfTI File Details:")
    print(f"Shape: {nii_shape}")
    print(f"Voxel Size: {nii_voxel_size}")
    print("Affine Matrix:")
    print(nii_affine)
    
    return nii_shape, nii_voxel_size, nii_affine
