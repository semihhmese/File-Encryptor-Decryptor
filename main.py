from tkinter import Tk, Label, Button, filedialog
from cryptography.fernet import Fernet

class FileEncryptorDecryptor:
    def __init__(self, master):
        self.master = master
        master.title("File Encryptor/Decryptor")

        self.label = Label(master, text="Dosya Şifreleme ve Çözme Uygulaması")
        self.label.pack()

        self.encrypt_button = Button(master, text="Dosya Şifrele", command=self.encrypt_file)
        self.encrypt_button.pack()

        self.decrypt_button = Button(master, text="Dosya Çöz", command=self.decrypt_file)
        self.decrypt_button.pack()

    def generate_key(self):
        # Rastgele bir anahtar oluştur
        return Fernet.generate_key()

    def load_key(self):
        # Anahtarı dosyadan oku
        try:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            return None

    def save_key(self, key):
        # Anahtarı dosyaya kaydet
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def encrypt_file(self):
        key = self.load_key()

        if key is None:
            key = self.generate_key()
            self.save_key(key)

        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as file:
                data = file.read()
                cipher_suite = Fernet(key)
                encrypted_data = cipher_suite.encrypt(data)

            with open(file_path, "wb") as file:
                file.write(encrypted_data)

            print(f"{file_path} dosyası şifrelendi.")
        else:
            print("Dosya seçilmedi.")

    def decrypt_file(self):
        key = self.load_key()

        if key is None:
            print("Anahtar bulunamadı. Lütfen önce bir dosya şifreleyin.")
            return

        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
                cipher_suite = Fernet(key)
                decrypted_data = cipher_suite.decrypt(encrypted_data)

            with open(file_path, "wb") as file:
                file.write(decrypted_data)

            print(f"{file_path} dosyası çözüldü.")
        else:
            print("Dosya seçilmedi.")

if __name__ == "__main__":
    root = Tk()
    app = FileEncryptorDecryptor(root)
    root.mainloop()
