import requests
import datetime

def sheet(number, name, mailid, age, gender, phone, tumorresponse, postprocess):
    SHEETY_ENDPOINT = 'https://api.sheety.co/7d7181fff6979ab29d38349a22c8d851/deepTumorResponces/sheet1'

    dt = datetime.datetime.now()
    formatted_date = dt.strftime("%d/%m/%Y")
    formatted_time = f"{dt.hour}:{dt.minute}:{dt.second}"

    # Extract postprocess data
    location = postprocess.get('location', 'N/A')
    width_mm = postprocess.get('width', 'N/A')
    height_mm = postprocess.get('height', 'N/A')
    area_mm2 = postprocess.get('area', 'N/A')

    # Handle non-numeric values
    if width_mm != 'N/A':
        width_mm = f"{width_mm:.2f} mm"
    if height_mm != 'N/A':
        height_mm = f"{height_mm:.2f} mm"
    if area_mm2 != 'N/A':
        area_mm2 = f"{area_mm2:.2f} mm²"

    parameters_sheety = {
        "sheet1": {
            "timestamp": f"{formatted_date} {formatted_time}",
            "id": number,
            "name": name,
            "mailid": mailid,
            "age": age,
            "gender": gender,
            "phone": phone,
            "tumorresponse": tumorresponse,
            "tumorlength": width_mm,
            "tumorwidth": height_mm,
            "tumorarea": area_mm2,
            "tumorlocation": location
        }
    }

    # Post data to Sheety
    response_sheet = requests.post(url=SHEETY_ENDPOINT, json=parameters_sheety)
    print(response_sheet.status_code)
    print(response_sheet.json())
    print(response_sheet.text)