FROM php:8.0-apache
# Cài đặt gói yelp
RUN apt-get update && apt-get install -y yelp
# Khởi động Apache
CMD ["apache2-foreground"]