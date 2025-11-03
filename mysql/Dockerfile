FROM mysql:8.0

# 可被 compose 覆蓋
ENV MYSQL_ROOT_PASSWORD=a1478963A \
    MYSQL_DATABASE=app_db \
    MYSQL_USER=app_user \
    MYSQL_PASSWORD=app_user_password

# 自訂設定（若無此檔，請建立）
COPY ./config/my.cnf /etc/mysql/conf.d/my.cnf

EXPOSE 3306
