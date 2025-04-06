from ccd_deidentification.deidentifier import CCDDeidentifier

def main():
    deidentifier = CCDDeidentifier()
    result = deidentifier.deidentify_ccd_xml("C:\\Users\\Alfred.Stangl\\repos\\personal\\ccd_deidentification\\tests\\ccda\\Arthur650_Johns824_18df1e20-2e60-6bde-73cf-345509346c3f.xml")
    print(result)
    mask_df = deidentifier.mask_map_to_data_frame()
    mask_df.head()
    deidentifier.reset()

if __name__ == "__main__":
    main()

