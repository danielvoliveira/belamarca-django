# Bela Marca Store:

## Introduction:

This project was created for a beach wear store named like Bela Marca to show all products and informations about the brand.

The environment was created with Docker configuration using a container for run Django and other to Nginx.

To compile the assets was used Node.js, they are inside the *'./assets'* directory.

To make easier the updates of the project's client was chose the Django-CMS.

This project is componentized with 5 apps:

1) bannerapp: to center all kinds of banner plugins

2) faqapp: to center the faq plugin with common questions

3) formapp: to center the form plugins like newsletter and contact

4) genericapp: to center the generic plugins like header, footer and floating icons

5) productapp: to center the product functionalities like category, subcategory, attributes, prices and images

## Installation:

Access the directory with the following command:

```sh
cd ./belamarca-django
```

Compile and up the docker environment with the following command:

```sh
docker-compose build

docker-compose up -d
```

Access the bash with the following command:

```sh
docker exec -it belamarca-app-hlg bash
```

Create and run all migrations of the project using the following commands:

```sh
python manage.py makemigrations

python manage.py migrate
```

Collect all static files with the following command and type 'yes' to continue:

```sh
python manage.py collectstatic
```

Create your superuser with the following command:

```sh
python manage.py createsuperuser
```

After that, still inside the bash, install Node.js with the following command:

```sh
npm install
```
ou
```sh
npm install --legacy-peer-deps
```
ou
```sh
npm install --force
```

If you want a development mode run the following command:

```sh
npm run develop
```

Or if you want a production mode run the following command:

```sh
npm run build
```

Finally, access the application in browser with *http://localhost:8080*

And manage your personalized web application accessing *http://localhost:8080/admin*

# Upload of Products:

In this project we have a process to upload products with image, categories, subcategories, attributes and attributeoptions automatically.

To do this access the route "http://localhost:8080/produto/get_products_from_csv/" and check the upload status accessing the Docker log: <code>docker logs -f belamarca-app-hlg</code>.

Details:

- The default sheet for the products is inside the dir "productapp/static/products.csv";
- If you want to change the list of Products, ProductImages, Categories, Subcategories and AttributeOptions access the sheet and change what you need;
- All product images are inside the dir "media/products_images" and the prints are inside "media/products_images/prints";
- If you want to change the images send your new images to the product's images dir.
- The name of the images should be like the name inside image column "image_name" from products sheet.
- To change the prints images and hexadecimal colors from AttributeOptions access the default values inside "settings.PRODUCSTS_COLORS_HEXADECIMAL" and "settings.PRODUCSTS_PRINTS_IMAGES".

# Other information:

* The file *.env* in the root has the environment variables.

* All static files go to the directory "./static/webpack_bundles/"

* The logs output are printed in container *belamarca-django > belamarca-app-hlg*. To access the logs the command <code>docker logs -f belamarca-app-hlg</code>

* To stop and remove the docker build run <code>docker-compose rm --stop</code>

* To just stop the docker build run <code>docker-compose down</code>

## Superuser created from me:

* usr=belamarca
* pass=Bela@2022

# Other commands to know about:

Command to fix dependencies problems:
```sh
npm audit fix --force
```

Command to remove node_modules directory:
```sh
rm -rf node_modules
```

Command to clean cache from node:
```sh
npm cache clean --force
```

Command to compile webpack and generate 'webpack-stats.json' file:
```sh
npx webpack --config webpack.config.js
```