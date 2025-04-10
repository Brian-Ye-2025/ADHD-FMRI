## Introduction
In this section, we will show you how to use our functions to locate brain regions, check nifti file attributes, convert nift files from 4D to 3D and apply masks and generate glass brain plots

### Data 
The data we will use in the examples be the `rest.nii` file from patient 10020,  which is a rs-fMRI dataset for a control subject from the ADHD-200 Preprocessed sample from the International Neuroimaging Datasharing Initiative (INDI)
http://preprocessed-connectomes-project.org/adhd200/index.html

### Functions
Here, we will use two functions, `plot_brain_regions` and `inspect_nifti_file`.

`plot_brain_regions` is a function to plot the locations of different regions of the brain

`inspect_nifti_file` is a function to find the shape, voxel size and affine matrix of a nifti file.

`extract_3d_volume` is a function that converts 4D nifti files into 3D by selecting a specific index number

`masked_glass_plot` is a function that converts from 4D to 3D and plots a glass brain plot using masked data

Below are all the arguments in `plot_brain_regions`
```python
plot_brain_regions(regions_names: list, aal_list_path)
```

Below are all the arguments in `inspect_nifti_file`
```python
inspect_nifti_file(nifti_path)
```
Below are the arguments in `extract_3d_volume`
```python
extract_3d_volume(fmri_img_path, volume_index=0)
```

Below are the arguments in `masked_glass_plot`
```python
masked_glass_plot(file_path, volume_index=0)
```

### Application

We will first show `plot_brain_regions` apply the aal_labels file, containing the region names that will be searched in the function 

```python
plot_brain_regions(["Precentral_L", "Precentral_R", "Frontal_Sup_R"], aal_path)
```
![Image](https://github.com/user-attachments/assets/89b7a495-f23c-437b-b7cd-25c56f61f205)

For `inspect_nifti_file` input the file path of the nifti file, the example uses a sample rest.nii from ADHD-200

```python
inspect_nifti_file(file_path)
```
![Image](https://github.com/user-attachments/assets/e7ac069a-b94d-4b57-a74d-0328e7a5bd4b)


For `extract_3d_volume` input a 4D file and set which index of time is needed
```python
extract_3d_volume(file_path, volume_index=0)
```

For `masked_glass_plot` input the 4D image file path and choose a desired time index
```python
masked_glass_plot(file_path, 0)
```
![Image](https://github.com/user-attachments/assets/8d545196-4071-47dc-bbc0-84b00e63e3fb)
