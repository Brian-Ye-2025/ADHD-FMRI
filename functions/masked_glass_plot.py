from nilearn.masking import compute_brain_mask
from nilearn.image import math_img

def masked_glass_plot(file_path, volume_index=0):
    #Converts 4D to 3D
    volume_img = index_img(file_path, volume_index)

    #Applies masking
    adhd_brain_mask = compute_brain_mask(volume_img)
    adhd_masked_img = math_img("img * mask", img=extracted1, mask=adhd_brain_mask)

    #Generates glass plot
    plot_glass_brain(adhd_masked_img, display_mode='ortho')
    plt.show()
