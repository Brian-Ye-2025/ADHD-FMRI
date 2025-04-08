# ADHD-FMRI
## Introduction
Data used is from the ADHD-200 Preprocessed initiative and contains neuroimaging data of 362 children and adolescents with ADHD and 585 control subjects. Functions are focused on exploring fMRI data from the ADHD-200 Sample. Data used in examples is at rest data (rest.nii )from patient 0010020

http://preprocessed-connectomes-project.org/adhd200/index.html

## Functions
`plot_brain_regions1` can be used to plot out selected brain regions from aal_labels

`inspect_nifti_file` is a function to find the shape, voxel size and affine matrix of a nifti file.

`extract_3d_volume` is a function that converts 4D nifti files into 3D by selecting a specific index number

`masked_glass_plot` is a function that converts from 4D to 3D and plots a glass brain plot using masked data
