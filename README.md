# 🔐 CipherTool

A modern, user-friendly web application for encrypting and decrypting messages using the Triple DES (3DES) algorithm. Built with Streamlit and designed with a sleek dark theme interface.

![Triple DES Cipher Tool](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **🔑 Key Generation**: Generate cryptographically secure 128-bit or 192-bit encryption keys
- **🔒 Encryption**: Encrypt plain text messages with password protection
- **🔓 Decryption**: Decrypt encrypted messages using the correct password
- **📋 Copy to Clipboard**: Easy one-click copying with custom toast notifications
- **💾 Download Options**: Download generated keys and encrypted messages
- **🎨 Modern UI**: Beautiful dark-themed interface with smooth animations
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CipherTool.git
cd CipherTool
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

1. Run the application:
```bash
streamlit run streamlit_app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

3. Use the application:
   - **Generate Key**: Create a secure encryption key (128-bit or 192-bit)
   - **Encrypt**: Enter your message and password to encrypt
   - **Decrypt**: Paste encrypted message and password to decrypt

## 🔒 Security Notes

- **Never share your encryption keys** with anyone
- Store your keys in a **secure location**
- Use **strong passwords** for encryption
- Triple DES is considered legacy - for production use, consider **AES-256**
- This tool is for **educational and personal use**

## 🛡️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Streamlit
- **Encryption**: CryptoJS (Triple DES)
- **Icons**: Material Symbols
- **Fonts**: Space Grotesk

## 📁 Project Structure

```
CipherTool/
│
├── streamlit_app.py      # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── LICENSE              # MIT License
├── .gitignore           # Git ignore file
└── .streamlit/          # Streamlit configuration
    └── config.toml
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License

## 👨‍💻 Author

**Your Name**
- GitHub: @DevXplorer-ArJn

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing framework
- [CryptoJS](https://cryptojs.gitbook.io/) - For encryption functionality
- [Material Symbols](https://fonts.google.com/icons) - For beautiful icons
- [Google Fonts](https://fonts.google.com/) - For Space Grotesk font

## ⚠️ Disclaimer

This tool is provided for educational purposes only. The developers are not responsible for any misuse or damage caused by this program. Always ensure you have the right to encrypt/decrypt the data you're working with.

---

**Note**: Triple DES (3DES) is considered a legacy encryption algorithm. For new projects requiring strong encryption, consider using AES-256 instead.

Made with ❤️ and Python
