# Contoh Implementasi Unit Testing dengan Pytest di Github Action

##### @djiwandou, Praktisi Mengajar, 13-Desember-2023, @UISI (Universitas Internasional Semen Indonesia)

Project ini menjelaskan bagaimana menjalankan unit testing secara otomatis menggunakan PyTest python dan Github Actions

## Requirements
* Python (3.10.10)

Untuk run di local 

Harap install dependencies melalui file `requirements.txt` 
```commandline
pip install -r requirements.txt
```
Kalau belum ada pip terinstall, harap menginstall pip dulu dengan mengikuti referensi online.

## How To Run the Unit Tests
Untuk menjalankan unit test bisa run command berikut
```commandline
pytest -v -s
```
## Hasil run di local
![rec_pytest](https://github.com/djiwandou/contoh-pytest-github-action/assets/24618908/72c939c9-767c-48c4-b147-15c27c3e58e5)

## Hasil run di github actions
![rec_github_actions](https://github.com/djiwandou/contoh-pytest-github-action/assets/24618908/d1962c73-256b-496d-9a8b-f2791155082f)


[![Coverage Status](coverage.svg)](https://github.com/djiwandou/contoh-pytest-github-action)
