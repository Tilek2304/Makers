sudo apt install git - установка системы контроля версий git

git --version - проверка версии 

git config --global user.email 'email' - настройка почты в git

git config --global user.name 'name'   - настройка имени в git

git config --list - проверка настроек

ssh-keygen - сгенерировали новый ключ

cat ~/.ssh/id_rsa.pub - получение ssh ключа

создаем репозиторий на GitHub 

переходим в папку с проектом

git init - для превращение папки в репозиторий

git remote add origin ssh: - создали переменную(origin) для хранение данных связи и присвоили ssh связь

git status - проверка сатуса файлов

git add file_name - отслеживание конкретных файлов
git add . - отслеживание всего, что не отслеживается 

git commit -m message - создание коммита с комментарием message
git commit - создание коммита

git push origin branch_name - отправка версии кода на github репозиторий где branch_name - имя ветки

