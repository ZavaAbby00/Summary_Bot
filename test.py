import requests

def check_api(domain_url, text_to_send):
    api_endpoint = f"{domain_url}/api/check"  # Gantilah "/api/check" dengan path API yang sebenarnya

    # Persiapkan data yang akan dikirim
    data = {
        "text": text_to_send
    }

    try:
        # Kirim permintaan POST ke API
        response = requests.post(api_endpoint, json=data)

        # Periksa apakah permintaan berhasil (kode status 200)
        if response.status_code == 200:
            # Tampilkan hasil respon dari API
            print("Response from API:")
            print(response.json())
        else:
            print(f"Failed to fetch API. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    domain_url = "https://summaryapi-image-nhz45gwa6a-et.a.run.app/palm2"  # Gantilah dengan domain yang sebenarnya
    text_to_send = "Hello"

    check_api(domain_url, text_to_send)