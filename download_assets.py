import requests
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = {
    'V Kohli': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Virat_Kohli_in_PMO_New_Delhi.jpg/330px-Virat_Kohli_in_PMO_New_Delhi.jpg',
    'MS Dhoni': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/MS_Dhoni_%28Prabhav_%2723_-_RiGI_2023%29.jpg/330px-MS_Dhoni_%28Prabhav_%2723_-_RiGI_2023%29.jpg',
    'RG Sharma': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Prime_Minister_Of_Bharat_Shri_Narendra_Damodardas_Modi_with_Shri_Rohit_Gurunath_Sharma_%28Cropped%29.jpg/330px-Prime_Minister_Of_Bharat_Shri_Narendra_Damodardas_Modi_with_Shri_Rohit_Gurunath_Sharma_%28Cropped%29.jpg',
    'flag': 'https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/255px-Flag_of_India.svg.png'
}

for name, url in urls.items():
    filename = f"{name.replace(' ', '_')}.jpg"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(res.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed {filename}: {res.status_code}")
    except Exception as e:
        print(f"Error {filename}: {e}")
