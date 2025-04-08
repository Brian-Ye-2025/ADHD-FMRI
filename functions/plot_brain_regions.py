def plot_brain_regions(region_names: list, aal_list_path):
    # Load the AAL atlas
    aal = nilearn.datasets.fetch_atlas_aal(version='SPM12')
    aal_img = nilearn.image.load_img(aal.maps)
    aal_affine = aal_img.affine
    aal_img_data = aal_img.get_fdata()
    
    # Load the region mapping
    region_df = pd.read_excel(aal_list_path, skiprows=2)
    region_df.columns = ["Region_Code", "Region_Name", "Index"]
    region_df = region_df.dropna().reset_index(drop=True)
    region_df["Region_Code"] = region_df["Region_Code"].astype(int)
    region_df["Index"] = region_df["Index"].astype(int)
    
    # Extract region codes
    region_codes = []
    for region_name in region_names:
        matched_row = region_df[region_df["Region_Name"] == region_name]
        if matched_row.empty:
            raise ValueError(f"Region name '{region_name}' not found in the atlas.")
        region_codes.append(matched_row["Region_Code"].values[0])
    
    # Extract the desired regions
    aal_img_data_regions = aal_img_data.copy()
    aal_img_data_regions[~np.isin(aal_img_data, region_codes)] = 0
    
    # Create new image
    regions_img = nilearn.image.new_img_like(aal_img, aal_img_data_regions, affine=aal_affine, copy_header=True)
    
    # Create the plot
    nilearn.plotting.plot_glass_brain(regions_img, colorbar=False, title=f"Regions: {', '.join(region_names)}")
    
    plt.show()
