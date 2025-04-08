from nilearn.image import index_img

def extract_3d_volume(fmri_img_path, volume_index=0):
    #Extracts a moment from the 4th axis as marked by volume_index
    volume_img = index_img(fmri_img_path, volume_index)
    return volume_img
