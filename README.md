<h1 align="center">
    Nautilus backspace
</h1>

<p align="center">
  Расширение для возврата назад в Nautilus по нажатию клавиши BackSpace
</p>

### Установка
```
Скопируйте файл Back.py в директорию:
EXTENSION_DIR = /usr/share/nautilus-python/extensions
или
EXTENSION_DIR = ~/.local/share/nautilus-python/extensions
```

### Зависимости

#### Fedora
```shell
sudo dnf update
sudo dnf install nautilus-python
```

#### Debian/Ubuntu
```shell
sudo apt update
sudo apt install python3-nautilus gir1.2-nautilus-4.0
```

#### Arch Linux
```shell
sudo pacman -Sy python-nautilus
```
