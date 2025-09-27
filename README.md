# 🍕 PizzAi - AI-Based Pizza Ordering Web App



> **AI‑powered pizza ordering assistant built with Streamlit and Groq’s LLaMA 3 (`llama3‑70b‑8192`).**  
> The bot chats like a real server, takes complete orders, confirms delivery or pickup, summarises the bill, and can be extended with payment or POS hooks.

---

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-f06) ![Python](https://img.shields.io/badge/Built%20with-Pyhton-yellow) ![License](https://img.shields.io/badge/License-MIT-green) ![Made with ❤](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pizza-ai.streamlit.app)


## ✨ Features
- **Natural conversation** – greets, asks clarifying questions, and confirms the order.
- **Full menu handling** – pizzas (sizes & toppings), sides, and drinks with prices.
- **Delivery / pickup flow** – collects address when required.
- **Order summary** – repeats the basket and final total for confirmation.
- **Ultra‑low latency** – powered by **Groq API** inferencing LLaMA 3 at blazing speed.
- **Streamlit UI** – runs locally or can be deployed to Streamlit Community Cloud, Hugging Face Spaces, etc.

---

## 🖼️ Demo

| Chat Interface | Order Summary |
| -------------- | ------------- |
| ![Chat Screenshot](https://github.com/user-attachments/assets/8a48e6cd-b57f-4b16-9044-e48c6c4263ba) | ![Summary Screenshot](https://github.com/user-attachments/assets/af7e40d2-226d-4f5e-b287-bfbb0db5fb41) |


---

## 🏗️ Tech Stack
| Layer | Tech |
|-------|------|
| UI | [Streamlit](https://streamlit.io) + [streamlit‑chat](https://pypi.org/project/streamlit-chat/) |
| LLM | Groq API • **LLaMA 3 70B** |
| Secrets | `python‑dotenv` |
| Language | Python 3.9 + |

---

## 🚀 Quick Start

```bash
git clone https://github.com/choudaryhussainali/PizzAi-Bot.git
cd streamlit-pizza-order-bot
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
echo "GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" > .env
streamlit run pizza.py
````

Open **[http://localhost:8501](http://localhost:8501)** in your browser and start chatting!

---

## 📂 Project Structure

```
streamlit-pizza-order-bot/
├─ assets/              # images for the README / app
│  ├─ chat.png
│  └─ summary.png
├─ .env                 # ← your Groq API key (never commit!)
├─ pizza.py             # main Streamlit application
├─ requirements.txt     # Python dependencies
├─ README.md
└─ .gitignore
```

---

## 🔐 Environment Variables

| Variable       | Purpose                               |
| -------------- | ------------------------------------- |
| `GROQ_API_KEY` | Your secret key from the Groq Console |

Create a `.env` file in the repo root and add:

```dotenv
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🛠️ Extending

* **Add new menu items** – edit the system prompt in `pizza.py`.
* **Multilingual** – change the greeting messages or detect language automatically.
* **Payment integration** – hook into Stripe / PayPal after order confirmation.
* **Database logging** – store completed orders in PostgreSQL or Firebase.

---

## 👩‍💻 Contributing

1. Fork the repo and create your branch: `git checkout -b feature/awesome`.
2. Commit your changes: `git commit -am 'Add awesome feature'`.
3. Push the branch: `git push origin feature/awesome`.
4. Open a Pull Request – thanks! ❤️

Please run `black` and `flake8` before submitting.

---

## 📄 License

This project is proprietary and confidential. All rights reserved.

```
© 2025 HUSSAIN ALI. This code may not be copied, modified, distributed, or used without explicit permission.
```

---

## 📬 Contact

For questions or collaboration requests:

* 📧 Email: [choudaryhussainali@outlook.com](mailto:choudaryhussainali@outlook.com)
* 🌐 GitHub: [choudaryhussainali](https://github.com/choudaryhussainali)


---

## 🙌 Acknowledgements

* [Groq](https://groq.com) for the lightning‑fast LLM API
* Meta & TII for LLaMA 3
* The Streamlit community for an amazing developer experience

> Feel free to ⭐ the repo if you find it helpful, and enjoy your slice of AI‑powered pizza!

