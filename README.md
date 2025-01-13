
## Persyaratan

- Python 3.8 atau lebih baru
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Instalasi

1. Clone repositori ini:

    ```sh
    git clone https://github.com/username/repo-name.git
    cd repo-name/App
    ```

2. Install dependencies:

    ```sh
    pip install discord.py google-generativeai python-dotenv
    ```

3. Buat file [.env](http://_vscodecontentref_/1) di direktori [App](http://_vscodecontentref_/2) dan tambahkan API key dan token bot Anda:

    ```env
    GENAI_APIKEY='YOUR_API_KEY'
    CLIENT_TOKEN='YOUR_BOT_TOKEN'
    ```

## Menjalankan Bot

1. Jalankan bot dengan perintah berikut:

    ```sh
    python main.py
    ```

## Penggunaan

- Ketika bot aktif, Anda dapat mengirim pesan di Discord yang dimulai dengan `hana` diikuti dengan prompt Anda.
- Bot akan merespons dengan konten yang dihasilkan oleh model AI.

## Kontribusi

Silakan buat pull request atau buka issue untuk kontribusi atau masalah.

## Lisensi

Proyek ini dilisensikan di bawah MIT License.
