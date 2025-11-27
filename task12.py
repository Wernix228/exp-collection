import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_repo_data():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория в формате owner/repo")
        return

    url = f"https://api.github.com/users/{repo_name}"
    #url = f"https://api.github.com/repos/{repo_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Выбираем нужные поля
        fields = ['company', 'created_at', 'email', 'id', 'name', 'url']

        selected_data = {field: data.get(field) for field in fields}

        filename = f"{repo_name.replace('/', ' ')}_info.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(selected_data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("Успех", f"Данные репозитория сохранены в файл {filename}")
    except requests.RequestException as e:
        messagebox.showerror("Ошибка запроса", f"Не удалось получить данные: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

root = tk.Tk()
root.title("GitHub Repo Info")

tk.Label(root, text="Введите пользователя (owner):").pack(padx=10, pady=5)
# tk.Label(root, text="Введите имя репозитория (owner/repo):").pack(padx=10, pady=5)
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)
btn = tk.Button(root, text="Получить данные", command=get_repo_data)
btn.pack(padx=10, pady=10)

root.mainloop()
