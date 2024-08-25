def categorize_tumor(width_mm, height_mm):
    # Initialize the result, description, what to do, and who to consult
    result = ""
    description = ""
    what_to_do = []
    who_to_consult = []
    
    if width_mm <= 20 and height_mm <= 20:
        result = "Small"
        description = "The tumor is relatively small and localized. It may be contained within a single area of the brain and not extensively affecting surrounding tissues."
        what_to_do = ["Consider surgical resection followed by radiation therapy or chemotherapy if needed."]
        who_to_consult = ["Neurosurgeon: For surgical evaluation and possible removal of the tumor."]
    
    elif width_mm > 20 and width_mm <= 40 and height_mm > 20 and height_mm <= 40:
        result = "Moderate"
        description = "The tumor is larger and may be starting to affect or displace nearby brain structures. It may present additional challenges for treatment."
        what_to_do = ["Obtain detailed MRI or CT scans to assess the tumor's impact on surrounding structures and brain function."]
        who_to_consult = ["Radiation Oncologist: To plan and oversee radiation therapy if indicated."]
    
    elif width_mm > 40 and height_mm > 40:
        result = "Large"
        description = "The tumor is quite large and may have invaded or displaced significant brain structures. It might be more complex to treat and may affect brain function significantly."
        what_to_do = ["Perform high-resolution MRI or CT scans to evaluate the full extent of the tumor, including its relationship with surrounding brain structures."]
        who_to_consult = ["Neuro-Oncologist: To create a tailored treatment plan that may involve multiple therapies and management strategies."]
    
    else:
        result = "Unknown"
        description = "The dimensions provided do not fit within the expected ranges for classification."
        what_to_do = ["Reevaluate the dimensions or consult with a specialist for further assessment."]
        who_to_consult = ["Consult with a healthcare professional for further evaluation and guidance."]

    print("Result:", result)
    print("Description:", description)
    print("What to Do:", what_to_do)
    print("Who to Consult:", who_to_consult)
    
    suggestions = {
        "result": result,
        "description": description,
        "what_to_do": what_to_do,
        "who_to_consult": who_to_consult
    }
    return suggestions